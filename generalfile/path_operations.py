import pathlib
import appdirs
import os
import shutil
from send2trash import send2trash
import json
from distutils.dir_util import copy_tree
import time

from generallibrary import deco_cache

from generalfile.errors import *
from generalfile.decorators import deco_require_state, deco_preserve_working_dir


class _Path_Operations:
    """ File operations methods for Path. """
    _suffixIO = {"plain_text": ("txt", "md", ""), "spreadsheet": ("tsv", "csv")}
    timeout_seconds = 5
    dead_lock_seconds = 3

    def write(self, content=None, overwrite=False):
        """ Write to this Path.

            :param Path self:
            :param content:
            :param overwrite: """
        if not overwrite and self.exists():
            raise FileExistsError(f"Path '{self}' already exists and overwrite is 'False'.")

        with self.lock():
            self.parent().create_folder()

            temp_path = self.with_suffix(".temp")
            with open(str(temp_path), "w") as temp_file_stream:
                temp_file_stream.write(json.dumps(content))

            temp_path.rename(self.name(), overwrite=True)

    def read(self):
        """ Write to this Path.

            :param Path self: """
        with self.lock():
            with open(str(self), "r") as file_stream:
                return json.loads(file_stream.read())

    @deco_require_state(exists=True)
    def rename(self, name=None, stem=None, suffix=None, overwrite=False):
        """ Rename this single file or folder to anything.

            :param Path self:
            :param name:
            :param stem:
            :param suffix:
            :param overwrite:
            :return: """
        new_path = self
        for key, value in {"stem": stem, "suffix": suffix, "name": name}.items():
            if value is not None:
                new_path = getattr(new_path, f"with_{key}")(value)
        if new_path == self:
            return

        with self.lock(new_path):
            if overwrite:
                self._path.replace(str(new_path))
            else:
                self._path.rename(str(new_path))

    @deco_require_state(exists=True)
    def _copy_or_move(self, target_folder_path, overwrite, method):
        """ :param Path self: """
        target_folder_path = self.Path(target_folder_path)
        if target_folder_path.is_file():
            raise NotADirectoryError("parent_path cannot be a file")

        self_parent_path = self.absolute().parent() if self.is_file() else self.absolute()
        if self_parent_path == target_folder_path:
            return


        if self.is_file():
            filepaths = (self,)
        else:
            filepaths = tuple(self.get_paths_in_folder())

        target_filepaths = [target_folder_path / path.absolute().relative(self_parent_path) for path in filepaths]
        if not overwrite and any([target.exists(quick=True) for target in target_filepaths]):
            raise FileExistsError("Atleast one target filepath exists, cannot copy")

        with self.lock(target_folder_path):
            target_folder_path.create_folder()
            for path, target in zip(filepaths, target_filepaths):

                if method == "copy":
                    if path.is_file():
                        shutil.copy(str(path), str(target), follow_symlinks=False)  # Can clobber
                    else:
                        copy_tree(str(path), str(target))

                elif method == "move":
                    shutil.move(str(path), str(target))  # Can clobber if full target path is specified like we do

            if method == "move" and self.is_folder():
                self.delete()


    def copy(self, target_folder_path, overwrite=False):
        """ Copy files inside given folder or file to anything except it's own parent.

            :param Path self:
            :param target_folder_path:
            :param overwrite: """
        return self._copy_or_move(target_folder_path=target_folder_path, overwrite=overwrite, method="copy")

    def move(self, target_folder_path, overwrite=False):
        """ Move files inside given folder or file to anything except it's own parent.

            :param Path self:
            :param target_folder_path:
            :param overwrite: """
        return self._copy_or_move(target_folder_path=target_folder_path, overwrite=overwrite, method="move")

    def is_file(self):
        """ Get whether this Path is a file.

            :param Path self: """
        return self._path.is_file()

    def is_folder(self):
        """ Get whether this Path is a folder.

            :param Path self: """
        return self._path.is_dir()

    def exists(self, quick=False):
        """ Get whether this Path exists.

            :param Path self:
            :param quick: Whether to do a quick (case insensitive on windows) check. """
        if quick:
            return self._path.exists()
        else:
            try:
                path_list = self.get_paths_recursive(depth=0, include_self=True)
            except AttributeError:
                return False
            exists = False
            for foundPath in path_list:
                if foundPath == self:
                    exists = True
                elif str(foundPath).lower() == str(self).lower():
                    raise CaseSensitivityError(f"Same path with differing case not allowed: '{self}'")
            return exists

    def without_file(self):
        """ Get this path without it's name if it's a file, otherwise it returns itself.

            :param Path self: """
        if self.is_file():
            return self.parent()
        else:
            return self

    @deco_require_state(is_folder=True)
    def get_paths_in_folder(self):
        """ Get a generator containing every child Path inside this folder, relative if possible.

            :param Path self: """
        for child in self._path.iterdir():
            yield self.Path(child)

    @deco_require_state(quick_exists=True)
    def get_paths_recursive(self, depth=-1, include_self=False, include_files=True, include_folders=True):
        """ Get all paths that are next to this file or inside this folder.

            :param depth: Depth of -1 is limitless recursive searching. Depth of 0 searches only first level.
            :param include_self:
            :param include_files:
            :param include_folders:
            :param Path self: """
        if self.is_file():
            queued_folders = [self.parent()]
        elif self.is_folder():
            queued_folders = [self]
        else:
            raise AttributeError(f"Path {self} is neither file nor folder.")

        self_parts_len = len(queued_folders[0].parts())

        if include_self:
            yield self

        while queued_folders:
            for path in queued_folders[0].get_paths_in_folder():
                if path.is_file():
                    if include_files and path != self:
                        yield path
                elif path.is_folder():
                    if include_folders:
                        yield path

                    current_depth = len(path.parts()) - self_parts_len
                    if depth == -1 or current_depth < depth:
                        queued_folders.append(path)
            del queued_folders[0]

    def create_folder(self):
        """ Create folder with this Path unless it exists

            :param Path self: """
        if self.exists():
            return False
        else:
            self._path.mkdir(parents=True, exist_ok=True)
            return True

    def open_folder(self):
        """ Open folder to view it manually.

            :param Path self: """
        os.startfile(str(self.without_file()))

    @classmethod
    @deco_cache()
    def get_cache_dir(cls):
        """ Get cache folder.

            :param generalfile.Path cls: """
        return cls.Path(appdirs.user_cache_dir())

    @classmethod
    @deco_cache()
    def get_lock_dir(cls):
        """ Get lock folder inside cache folder.

            :param generalfile.Path cls: """
        return cls.Path.get_cache_dir() / "generalfile" / "locks"

    @classmethod
    def get_working_dir(cls):
        """ Get current working folder as a new Path.

            :param generalfile.Path cls: """
        return cls.Path(pathlib.Path.cwd())

    def set_working_dir(self):
        """ Set current working folder.

            :param Path self: """
        self.create_folder()
        os.chdir(str(self.absolute()))

    @deco_preserve_working_dir
    def delete(self):
        """ Delete a file or folder.
            :param Path self: """
        with self.lock():
            if self.is_file():
                os.remove(str(self))
            elif self.is_folder():
                shutil.rmtree(str(self), ignore_errors=True)

    @deco_preserve_working_dir
    def trash(self):
        """ Trash a file or folder
            :param Path self: """
        with self.lock():
            send2trash(str(self))

    @deco_require_state(is_folder=True)
    def delete_folder_content(self):
        """ Delete a file or folder
            :param Path self: """
        self.delete()
        self.create_folder()

    @deco_require_state(is_folder=True)
    def trash_folder_content(self):
        """ :param Path self: """
        self.trash()
        self.create_folder()

    @deco_require_state(exists=True)
    def seconds_since_creation(self):
        """ :param Path self: """
        return time.time() - os.path.getctime(str(self))

    @deco_require_state(exists=True)
    def seconds_since_modified(self):
        """ :param Path self: """
        return time.time() - os.path.getmtime(str(self))



import pathlib
import appdirs
import os
import shutil
from send2trash import send2trash
import json

from generallibrary import VerInfo, Timer, initBases, deco_cache, EmptyContext
from generalfile.errors import *

def deco_require_state(is_file=None, is_folder=None, exists=None, quick_exists=None):
    """ Decorator to easily configure and see which state to require. """
    def _decorator(func):
        def _wrapper(self, *args, **kwargs):
            """:param Path self:"""
            if is_file is not None:
                if self.is_file() != is_file:
                    raise AttributeError(f"Path {self} is_file check didn't match ({is_file}).")
            elif is_folder is not None:
                if self.is_folder() != is_folder:
                    raise AttributeError(f"Path {self} is_folder check didn't match ({is_folder}).")
            elif exists is not None:
                if self.exists() != exists:
                    raise AttributeError(f"Path {self} exists check didn't match ({exists}).")
            elif quick_exists is not None:
                if self.exists(quick=True) is not quick_exists:
                    raise AttributeError(f"Path {self} quick exists check didn't match ({quick_exists}).")

            return func(self, *args, **kwargs)
        return _wrapper
    return _decorator

def deco_preserve_working_dir(function):
    """ Decorator to preserve working dir if given function changes it somehow. """
    def _wrapper(*args, **kwargs):
        working_dir_path = Path.get_working_dir()
        result = function(*args, **kwargs)
        if working_dir_path != Path.get_working_dir():
            working_dir_path.set_working_dir()
        return result
    return _wrapper


class _Lock:
    """ A one-time-use lock used by Path.lock.
        Creates a lock for folder or path with these steps:
            Wait until unlocked.
            Create lock.
            Make sure only locked by self.
        A lock is inactive if it can be removed, as there's no Lock holding it's file stream.
        """
    def __init__(self, path, *other_paths):
        self.path = path
        self.all_abs_paths = [Path(p).absolute() for p in other_paths + (path, )]
        self.lock_file_stream = None

    def __enter__(self):
        if not self.path.owns_lock:
            self._attempt_lock_creation()
            self.path.owns_lock = True

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._close_and_remove_lock()
        self.path.owns_lock = False

    def _get_lock_str(self):
        return str(self.path.get_lock_dir() / self.path.absolute().get_alternative_path())

    def _attempt_lock_creation(self):
        path_absolute = self.path.absolute()
        timer = Timer()
        while timer.seconds() < self.path.timeout_seconds:
            if not self._is_locked():
                self._open_and_create_lock()
                affecting_locks = list(self._affecting_locks())
                if affecting_locks == [path_absolute]:
                    return
                elif path_absolute in affecting_locks:
                    self._close_and_remove_lock()  # Remove and try again to respect other locks
                else:
                    raise FileNotFoundError(f"Lock '{self.path}' failed to create.")
            # else:
                # print(path_absolute, list(self._affecting_locks()))
        raise TimeoutError(f"Couldn't lock '{self.path}' in time.")

    def _open_and_create_lock(self):
        if self.lock_file_stream is not None:
            raise AttributeError(f"A file stream is already opened for '{self.path}'.")

        self.lock_file_stream = open(self._get_lock_str(), "x")
        self.lock_file_stream.write("hello")

    def _close_and_remove_lock(self):
        if self.lock_file_stream is None:
            raise AttributeError(f"A file stream is not opened for '{self.path}'.")

        self.lock_file_stream.close()
        os.remove(self._get_lock_str())

    def _affecting_locks(self):
        path_absolute = self.path.absolute()
        for alternative_path in self.path.get_lock_dir().get_paths_in_folder():
            path = alternative_path.remove_start(self.path.get_lock_dir()).get_path_from_alternative()
            if path_absolute.startswith(path) or path.startswith(path_absolute):
                yield path

    def _is_locked(self):
        for _ in self._affecting_locks():
            return True
        return False


class _Path_ContextManager:
    """ Context manager methods for Path. """
    def __init__(self):
        self.owns_lock = False

    @staticmethod
    def _create_context_manager(path, *other_paths):
        """ :param Path path: """
        return EmptyContext() if path.startswith(Path.get_lock_dir()) else _Lock(path, *other_paths)

    def lock(self, *other_paths):
        """ Create a lock for this path unless path is inside `lock dir`.
            Optionally supply additional paths to prevent them from interfering as well as creating locks for them too.

            :param Path self: """
        other_paths = list(other_paths)
        for path in other_paths:
            paths_list = other_paths.copy()
            paths_list[paths_list.index(path)] = self  # Replace ´path´ with self
            self._create_context_manager(path, *paths_list)

        return self._create_context_manager(self, *other_paths)


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
    def _copy_or_move(self, target_folder_path, overwrite=False, copy=False):
        """ Copy this file or files inside given folder to anything except it's own parent.

            :param Path self:
            :param target_folder_path:
            :param overwrite:
            :param copy: """
        target_folder_path = Path(target_folder_path)
        if target_folder_path.is_file():
            raise NotADirectoryError("parent_path cannot be a file")

        self_parent_path = self.parent() if self.is_file() else self
        if self_parent_path == target_folder_path:
            return


        filepaths = (self,) if self.is_file() else self.get_paths_recursive(include_folders=False)
        target_filepaths = [target_folder_path / path.absolute().relative(self_parent_path) for path in filepaths]

        if not overwrite and any([target.exists(quick=True) for target in target_filepaths]):
            raise FileExistsError("Atleast one target filepath exists, cannot copy")

        with self.lock(target_folder_path):
            for path, target in zip(filepaths, target_filepaths):
                target.parent().create_folder()

                if copy:
                    shutil.copy(str(path), str(target), follow_symlinks=False)  # Can clobber
                else:
                    shutil.move(str(path), str(target))  # Can clobber if full target path is specified like we do
    # HERE ** See that this copy and move works


    def copy(self, target_folder_path, overwrite=False):
        """ Copy this file or files inside given folder to anything except it's own parent.

            :param Path self:
            :param target_folder_path:
            :param overwrite: """
        return self._copy_or_move(target_folder_path=target_folder_path, overwrite=overwrite, copy=True)

    def move(self, target_folder_path, overwrite=False):
        """ Copy this file or files inside given folder to anything except it's own parent.

            :param Path self:
            :param target_folder_path:
            :param overwrite: """
        return self._copy_or_move(target_folder_path=target_folder_path, overwrite=overwrite, copy=False)

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
                path_list = self.get_paths_recursive(include_self=True)
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
            yield Path(child)

    @deco_require_state(quick_exists=True)
    def get_paths_recursive(self, depth=0, include_self=False, include_files=True, include_folders=True):
        """ Get all paths that are next to this file or inside this folder.

            :param depth: Depth of -1 is limitless recursive searching. Depth of 0 which is default searches only first level.
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

    @staticmethod
    @deco_cache()
    def get_cache_dir():
        """ Get cache folder. """
        return Path(appdirs.user_cache_dir())

    @staticmethod
    @deco_cache()
    def get_lock_dir():
        """ Get lock folder inside cache folder. """
        return Path.get_cache_dir() / "generalfile" / "locks"

    @staticmethod
    def get_working_dir():
        """ Get current working folder as a new Path. """
        return Path(pathlib.Path.cwd())

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


class _Path_Strings:
    """ String operations for Path. """
    def __str__(self):
        """ :param Path self: """
        return self._str_path

    def __repr__(self):
        """ :param Path self: """
        return self.__str__()

    def __truediv__(self, other):
        """ :param Path self: """
        return Path(self._path / str(other))

    def __eq__(self, other):
        """ :param Path self: """
        return str(self) == str(other)

    def __hash__(self):
        """ :param Path self: """
        return hash(self._str_path)

    def get_alternative_path(self):
        """ Get path using alternative delimiter and alternative root for windows.

            :param Path self: """
        return Path(self.path_delimiter_alternative.join(self.parts()).replace(":", self.windows_base_alternative))

    def get_path_from_alternative(self):
        """ Get path from an alternative representation.

            :param Path self: """
        return Path(str(self).replace(self.path_delimiter_alternative, self.path_delimiter).replace(self.windows_base_alternative, ":"))

    def absolute(self):
        """ Get new Path as absolute.

            :param Path self: """
        if self.is_absolute():
            return self
        else:
            return Path(self._path.absolute())

    def relative(self, base=None):
        """ Get new Path as relative.

            :param Path self:
            :param base: Defaults to working dir. """
        if self.is_relative() and base is None:
            return self
        else:
            if base is None:
                base = self.get_working_dir()
            return Path(self._path.relative_to(str(base)))

    def is_absolute(self):
        """ Get whether this Path is absolute.

            :param Path self: """
        return self._path.is_absolute()

    def is_relative(self):
        """ Get whether this Path is relative.

            :param Path self: """
        return not self.is_absolute()

    def startswith(self, path):
        """ Get whether this Path starts with given string.

            :param Path self:
            :param str or Path path:"""
        return str(self).startswith(str(Path(path)))

    def endswith(self, path):
        """ Get whether this Path ends with given string.

            :param Path self:
            :param str or Path path:"""
        return str(self).endswith(str(Path(path)))

    def remove_start(self, path):
        """ Remove a string from the start of this Path.

            :param Path self:
            :param str or Path path:"""
        str_path = str(path)
        if not self.startswith(str_path):
            return self
        else:
            return Path(str(self)[len(str_path):])

    def remove_end(self, path):
        """ Remove a string from the end of this Path.

            :param Path self:
            :param str or Path path:"""
        str_path = str(path)
        if not self.endswith(str_path):
            return self
        else:
            return Path(str(self)[:-len(str_path)])

    def parent(self, index=0):
        """ Get any parent as a new Path.
            Doesn't convert to absolute path even if needed.

            :param Path self:
            :param index: Which parent, 0 is direct parent.
            :raises IndexError: If index doesn't exist.  """
        strParent = str(self._path.parents[index])
        if strParent == ".":
            strParent = ""
        return Path(strParent)

    def parts(self):
        """ Get list of parts building this Path as list of strings.

            :param Path self: """
        return str(self).split(self.path_delimiter)

    def name(self):
        """ Get name of Path which is stem + suffix.

            :param Path self: """
        return self._path.name

    def with_name(self, name):
        """ Get a new Path with new name which is stem + suffix.

            :param name: Name.
            :param Path self: """
        return Path(self._path.with_name(str(name)))

    def stem(self):
        """ Get stem which is name without last suffix.

            :param Path self: """
        return self._path.stem

    def with_stem(self, stem):
        """ Get a new Path with new stem which is name without last suffix.

            :param stem: Name without suffix.
            :param Path self: """
        return Path(self._path.with_stem(str(stem)))

    def suffix(self):
        """ Get suffix which is name without stem.

            :param Path self: """
        return self._path.suffix

    def with_suffix(self, suffix):
        """ Get a new Path with new suffix which is name without stem.

            :param suffix: Name without stem.
            :param Path self: """
        return Path(self._path.with_suffix(str(suffix)))

@initBases
class Path(_Path_ContextManager, _Path_Operations, _Path_Strings):
    """
    Immutable cross-platform Path.
    Wrapper for pathlib.
    Implements rules to ensure cross-platform compatability.
    Adds useful methods.
    """
    verInfo = VerInfo()
    path_delimiter = verInfo.pathDelimiter
    path_delimiter_alternative = "&#47;"  # So that we can represent a nested path with a single filename
    windows_base_alternative = "&#58;"  # Since we cannot have `:` as part of filename

    def __init__(self, path=None):
        self._str_path = self._scrub(str_path="" if path is None else str(path))
        self._path = pathlib.Path(self._str_path)

    def _scrub(self, str_path):
        str_path = self._replace_delimiters(str_path=str_path)
        str_path = self._invalid_characters(str_path=str_path)
        str_path = self._trim(str_path=str_path)
        return str_path

    def _replace_delimiters(self, str_path):
        str_path = str_path.replace("/", self.path_delimiter)
        str_path = str_path.replace("\\", self.path_delimiter)
        # str_path = str_path.replace(self.path_delimiter_alternative, self.path_delimiter)  # Don't remember why I commented this
        return str_path

    def _invalid_characters(self, str_path):
        # Simple invalid characters testing from Windows
        for character in '<>"|?*':
            if character in str_path:
                raise InvalidCharacterError(f"Invalid character '{character}' in '{str_path}'")
        if ":" in str_path:
            if not self.verInfo.pathRootHasColon:
                raise InvalidCharacterError(f"Path has a colon but '{self.verInfo.os}' doesn't use colon for path root: '{str_path}'")
            if str_path[1] != ":":
                raise InvalidCharacterError(f"Path has a colon but there's no colon at index 1: '{str_path}'")
            if len(str_path) >= 3 and str_path[2] != self.path_delimiter:
                raise InvalidCharacterError(f"Path has a colon but index 2 is not a delimiter: '{str_path}'")
            if ":" in str_path[2:]:
                raise InvalidCharacterError(f"Path has a colon that's not at index 1: '{str_path}'")
        if str_path.endswith("."):
            raise InvalidCharacterError(f"Path cannot end with a dot ('.').")
        return str_path

    def _trim(self, str_path):
        if not self.verInfo.pathRootIsDelimiter and str_path.startswith(self.path_delimiter):
            str_path = str_path[1:]
        if str_path.endswith(self.path_delimiter):
            str_path = str_path[0:-1]
        return str_path


















































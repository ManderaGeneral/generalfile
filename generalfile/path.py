
import pathlib
import appdirs
import os
import functools
import shutil
from send2trash import send2trash

from generallibrary import VerInfo, Timer, initBases, deco_cache, sleep
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


class ContextManager:
    """ Context manager methods for Path. """

    def __init__(self):
        self._file_stream = None

    def __enter__(self):
        """ Creates a lock for folder or path with these steps:
            Wait until unlocked.
            Create lock.
            Make sure only locked by self.

            :param Path self: """
        timer = Timer()
        while timer.seconds() < self.timeout_seconds:
            if not self._is_locked():
                self._open_and_create_lock()
                affecting_locks = list(self._affecting_locks())
                print(affecting_locks)
                if affecting_locks == [self]:
                    return
                elif self in affecting_locks:
                    self._close_and_remove_lock()  # Remove and try again to respect other locks
                else:
                    raise FileNotFoundError(f"Lock '{self}' failed to create.")
        raise TimeoutError(f"Couldn't lock '{self}' in time.")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ :param Path self: """
        self._close_and_remove_lock()

    def _get_lock_str(self):
        """ :param Path self: """
        return str(self.get_lock_dir() / self.absolute().get_alternative_path())

    def _open_and_create_lock(self):
        """ :param Path self: """
        if self._file_stream is not None:
            raise AttributeError(f"A file stream is already opened for '{self}'.")
        self._file_stream = open(self._get_lock_str(), "x")
        self._file_stream.write("hello")

    def _close_and_remove_lock(self):
        """ :param Path self: """
        if self._file_stream is None:
            raise AttributeError(f"A file stream is not opened for '{self}'.")

        self._file_stream.close()
        Path(self._get_lock_str()).delete()

    def _affecting_locks(self):
        """ :param Path self: """
        self_absolute = self.absolute()
        for alternative_path in self.get_lock_dir().get_paths_in_folder():
            path = alternative_path.remove_start # HERE **
            if self_absolute.startswith(path) or path.startswith(self):
                yield path

    def _is_locked(self):
        """ :param Path self: """
        for _ in self._affecting_locks():
            return True
        return False


class FileOperations:
    """ File operations methods for Path. """
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
                path_list = self.get_paths(include_self=True)
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
    def get_paths(self, depth=0, include_self=False, include_files=True, include_folders=True):
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
        with self:
            if self.is_file():
                os.remove(str(self))
            elif self.is_folder():
                shutil.rmtree(str(self))

    @deco_preserve_working_dir
    def trash(self):
        """ Trash a file or folder
            :param Path self: """
        with self:
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


class StrOperations:
    """ String operations for Path. """
    def __str__(self):
        """ :param Path self: """
        return str(self._path)

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
        return object.__hash__(self)

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
        return Path(self._path.absolute())

    def relative(self):
        """ Get new Path as relative.

            :param Path self: """
        return Path(self._path.relative())

    def is_absolute(self):
        """ Get whether this Path is absolute.

            :param Path self: """
        return self._path.is_absolute()

    def is_relative(self):
        """ Get whether this Path is relative.

            :param Path self: """
        return self._path.is_relative()

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
        """ Get list of parts building this Path as strings.

            :param Path self: """
        return str(self).split(self.path_delimiter)

    def name(self):
        """ Get name of Path.

            :param Path self: """
        return self._path.name

    def with_name(self, name):
        """ Get a new Path with new name.

            :param name: Name.
            :param Path self: """
        return Path(self._path.with_name(name))

    def stem(self):
        """ Get stem which is name without last suffix.

            :param Path self: """
        return self._path.stem

    def with_stem(self, stem):
        """ Get a new Path with new stem.

            :param stem: Name without suffix.
            :param Path self: """
        return Path(self._path.with_stem(stem))

    def suffix(self):
        """ Get suffix which is name without stem.

            :param Path self: """
        return self._path.suffix

    def with_suffix(self, suffix):
        """ Get a new Path with new suffix.

            :param suffix: Name without stem.
            :param Path self: """
        return Path(self._path.with_stem(suffix))

@initBases
class Path(ContextManager, FileOperations, StrOperations):
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
    _suffixIO = {"txt": ("txt", "md", ""), "tsv": ("tsv", "csv")}
    timeout_seconds = 12
    dead_lock_seconds = 3

    def __init__(self, path=None):
        str_path = self._scrub(str_path="" if path is None else str(path))

        self._path = pathlib.Path(str_path)
        self._file_stream = None

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


















































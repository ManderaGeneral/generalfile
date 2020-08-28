
import pathlib

import appdirs

import os

import functools

from generallibrary import VerInfo, Timer
from generalfile.errors import *

def decorator_require_state(is_file=None, is_folder=None, exists=None):
    """Decorator to easily configure and see which state to require."""

    def _decorator(func):
        def _wrapper(self, *args, **kwargs):
            """:param Path self:"""
            if is_file is not None:
                if self.is_file() != is_file:
                    raise AttributeError(f"Path {self} is_file check didn't match.")
            elif is_folder is not None:
                if self.is_folder() != is_folder:
                    raise AttributeError(f"Path {self} is_folder check didn't match.")
            elif exists is not None:
                if self.exists() != exists:
                    raise AttributeError(f"Path {self} exists check didn't match.")

            return func(self, *args, **kwargs)
        return _wrapper
    return _decorator

class Path:
    """
    Immutable cross-platform Path.
    Wrapper for pathlib.
    Implements rules to ensure cross-platform compatability.
    Adds useful methods.
    """
    path_delimiter = VerInfo().pathDelimiter
    path_delimiter_alternative = "^_^"
    _suffixIO = {"txt": ("txt", "md", ""), "tsv": ("tsv", "csv")}
    verInfo = VerInfo()
    timeout_seconds = 12
    dead_lock_seconds = 3

    def _scrub(self, str_path):
        str_path = self._replace_delimiters(str_path=str_path)
        str_path = self._invalid_characters(str_path=str_path)
        str_path = self._trim(str_path=str_path)
        return str_path

    def _replace_delimiters(self, str_path):
        str_path = str_path.replace("/", self.path_delimiter)
        str_path = str_path.replace("\\", self.path_delimiter)
        str_path = str_path.replace(self.path_delimiter_alternative, self.path_delimiter)
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
            if str_path[2] != self.path_delimiter:
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



    def __init__(self, path=None):
        str_path = self._scrub(str_path="" if path is None else str(path))

        self._path = pathlib.Path(str_path)
        self._file_stream = None

    def __str__(self):
        return str(self._path)

    def __repr__(self):
        return self.__str__()

    def __truediv__(self, other):
        return Path(self._path / str(other))

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return object.__hash__(self)

    def __enter__(self):
        """ Creates a lock for folder or path with these steps:
            Wait until unlocked.
            Create lock.
            Make sure only locked by self."""

        timer = Timer()
        while timer.seconds() < self.timeout_seconds:
            if not self._is_locked():
                self._create_lock()

                all_locks = self._all_locks()
                if all_locks == [self]:
                    return
                elif self in all_locks:
                    self._remove_lock()
                else:
                    raise FileNotFoundError(f"Lock '{self}' failed to create.")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._remove_lock()









        locks_path = self.get_lock_dir()
        absolute = self.absolute()
        timer = Timer()

        locked = False
        while not locked:
            for lock in locks_path.get_paths_in_folder:
                if absolute.startswith(lock):
                    break
            else:
                locked = True

            if timer.seconds() > self.timeout_seconds:
                raise TimeoutError(f"Couldn't lock {self}.")


    def get_alternative_str(self):
        """Get path as a string using alternative delimiter."""
        return self.path_delimiter_alternative.join(self.parts())

    def absolute(self):
        """Get new Path as absolute."""
        return Path(self._path.absolute())

    def relative(self):
        """Get new Path as relative."""
        return Path(self._path.relative())

    def is_absolute(self):
        """Get whether this Path is absolute."""
        return self._path.is_absolute()

    def is_relative(self):
        """Get whether this Path is relative."""
        return self._path.is_relative()

    def startswith(self, path):
        """Get whether this Path starts with given string."""
        return str(self).startswith(str(path))

    def endswith(self, path):
        """Get whether this Path ends with given string."""
        return str(self).endswith(str(path))

    def parent(self, index=0):
        """Get any parent as a new Path.
        Doesn't convert to absolute path even if needed.

        :raises IndexError: If index doesn't exist."""
        strParent = str(self._path.parents[index])
        if strParent == ".":
            strParent = ""
        return Path(strParent)

    def parts(self):
        """Get list of parts building this Path as strings."""
        return str(self).split(self.path_delimiter)

    def stem(self):
        """Get stem which is name without last suffix."""
        return self._path.stem

    def with_stem(self, stem):
        """Get a new Path with new stem."""
        return Path(self._path.with_stem(stem))

    # IO operations below

    def is_file(self):
        """Get whether this Path is a file."""
        return self._path.is_file()

    def is_folder(self):
        """Get whether this Path is a folder."""
        return self._path.is_dir()

    def exists(self):
        """Get whether this Path exists."""

        path_list = self.get_paths(include_self=True)
        exists = False
        for foundPath in path_list:
            if foundPath == self:
                exists = True
            elif str(foundPath).lower() == str(self).lower():
                raise CaseSensitivityError(f"Same path with differing case not allowed: '{self}'")
        return exists

    @decorator_require_state(is_folder=True)
    def get_paths_in_folder(self):
        """Get a generator containing every child Path inside this folder."""
        for child in self._path.iterdir():
            yield Path(child)

    @decorator_require_state(exists=True)
    def get_paths(self, depth=1, include_self=False, include_files=True, include_folders=True):
        """Get all paths that are next to this file or inside this folder."""
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
                    if include_files:
                        yield path
                elif path.is_folder():
                    if include_folders:
                        yield path

                    current_depth = len(path.parts()) - self_parts_len
                    if not current_depth or current_depth <= depth:
                        queued_folders.append(path)
            del queued_folders[0]

    @decorator_require_state(is_file=False)
    def create_folder(self):
        """Create folder with this Path unless it exists"""
        if self.exists():
            return False
        else:
            self._path.mkdir(parents=True, exist_ok=True)
            return True

    @staticmethod
    @functools.lru_cache()
    def get_cache_dir():
        """Get cache folder."""
        return Path(appdirs.user_cache_dir())

    @staticmethod
    @functools.lru_cache()
    def get_lock_dir():
        """Get lock folder inside cache folder."""
        return Path.get_cache_dir() / "generalfile" / "locks"

    @staticmethod
    def get_working_dir():
        """Get current working folder as a new Path."""
        return Path(pathlib.Path.cwd())

    def set_working_dir(self):
        """Set current working folder."""
        self.create_folder()
        os.chdir(str(self.absolute()))

    def delete(self):
        """."""
        # with self.lock():


    def trash(self):
        """."""

    def delete_folder_content(self):
        """."""

    def trash_folder_content(self):
        """."""















































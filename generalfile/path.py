
import pathlib

import os

from generallibrary import VerInfo
from generalfile.errors import *


class Path:
    """
    Immutable cross-platform Path.
    Wrapper for pathlib.
    Implements rules to ensure cross-platform compatability.
    Adds useful methods.
    """
    path_delimiter = VerInfo().pathDelimiter
    _suffixIO = {"txt": ("txt", "md", ""), "tsv": ("tsv", "csv")}
    verInfo = VerInfo()

    def _scrub(self, str_path):
        str_path = self._replace_delimiters(str_path=str_path)
        str_path = self._invalid_characters(str_path=str_path)
        str_path = self._trim(str_path=str_path)
        return str_path

    def _replace_delimiters(self, str_path):
        str_path = str_path.replace("/", self.path_delimiter)
        str_path = str_path.replace("\\", self.path_delimiter)
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

    def __str__(self):
        return str(self._path)

    def __repr__(self):
        return self.__str__()



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

    def get_paths_in_folder(self):
        """Get a generator containing every child Path inside this folder."""
        for child in self._path.iterdir():
            yield Path(child)

    def get_paths(self, depth=1, include_self=False, include_files=True, include_folders=True):
        """Get all paths that are next to this file or inside this folder."""
        queued_folders = []
        if self.is_file():
            queued_folders.append(self.parent())
        elif self.is_folder():
            queued_folders.append(self)

        if include_self:
            yield self

        parts_len = len(self.parts())

        while queued_folders:
            for path in queued_folders[0].get_paths_in_folder():
                if path.is_file():
                    if include_files:
                        yield path
                elif path.is_folder():
                    if include_folders:
                        yield path

                    if depth and len(absoluteSubPath.foldersList) - pathFoldersLen >= maxDepth:

            del queued_folders[0]


    def exists(self):
        """Get whether this Path exists."""
        exists = False

        path_list = self.get_paths(include_self=True)
        for foundPath in path_list:
            if foundPath == self:
                exists = True
            elif str(foundPath).lower() == str(self).lower():
                raise CaseSensitivityError(f"Same path with differing case not allowed: '{self}'")

        return exists

    def create_folder(self):
        """Create folder with this Path unless it exists"""
        if self.exists():
            return False
        else:
            self._path.mkdir(parents=True, exist_ok=True)
            return True

    def is_file(self):
        """Get whether this Path is a file."""
        return self._path.is_file()

    def is_folder(self):
        """Get whether this Path is a folder."""
        return self._path.is_dir()

    @classmethod
    def get_working_dir(cls):
        """Get current working directory as a new Path."""
        return Path(pathlib.Path.cwd())

    def set_working_dir(self):
        """Set current working directory."""
        self.create_folder()
        os.chdir(str(self.absolute()))

    def delete(self):
        """."""

    def trash(self):
        """."""

    def delete_folder_content(self):
        """."""

    def trash_folder_content(self):
        """."""















































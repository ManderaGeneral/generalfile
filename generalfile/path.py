
import mutapath

from generallibrary import VerInfo
from generalfile.errors import *


class Path:
    """
    Mutable cross-platform Path.
    Wrapper for mutapath which wraps pathlib.
    Implements rules to ensure cross-platform compatabilities.
    Adds useful methods.
    """
    pathDelimiter = VerInfo().pathDelimiter
    _suffixIO = {"txt": ("txt", "md", ""), "tsv": ("tsv", "csv")}
    verInfo = VerInfo()

    def _scrub(self, strPath):
        strPath = self._replaceDelimiters(strPath=strPath)
        strPath = self._invalidCharacters(strPath=strPath)
        strPath = self._trim(strPath=strPath)
        return strPath

    def _replaceDelimiters(self, strPath):
        strPath = strPath.replace("/", self.pathDelimiter)
        strPath = strPath.replace("\\", self.pathDelimiter)
        return strPath

    def _invalidCharacters(self, strPath):
        # Simple invalid characters testing from Windows
        for character in '<>"|?*':
            if character in strPath:
                raise InvalidCharacterError(f"Invalid character '{character}' in '{strPath}'")
        if ":" in strPath:
            if not self.verInfo.pathRootHasColon:
                raise InvalidCharacterError(f"Path has a colon but '{self.verInfo.os}' doesn't use colon for path root: '{strPath}'")
            if strPath[1] != ":":
                raise InvalidCharacterError(f"Path has a colon but there's no colon at index 1: '{strPath}'")
            if strPath[2] != self.pathDelimiter:
                raise InvalidCharacterError(f"Path has a colon but index 2 is not a delimiter: '{strPath}'")
            if ":" in strPath[2:]:
                raise InvalidCharacterError(f"Path has a colon that's not at index 1: '{strPath}'")
        if strPath.endswith("."):
            raise InvalidCharacterError(f"Path cannot end with a dot ('.').")
        return strPath

    def _trim(self, strPath):
        if not self.verInfo.pathRootIsDelimiter and strPath.startswith(self.pathDelimiter):
            strPath = strPath[1:]
        if strPath.endswith(self.pathDelimiter):
            strPath = strPath[0:-1]
        return strPath


    def __init__(self, path):
        strPath = self._scrub(strPath="" if path is None else str(path))

        self._path = mutapath.Path(strPath)

    def __repr__(self):
        return str(self._path)



    def stem(self):
        """Property for stem part of Path.
        Stem is name without last suffix."""
        return self._path.stem

    def with_stem(self, stem):
        return self._path.with_stem(stem)

















































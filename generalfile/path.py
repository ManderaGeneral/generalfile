
import pathlib

from generallibrary import VerInfo
from generalfile.errors import *


class Path:
    """
    Layer on top of pathlib's Path.
    Implements rules to ensure cross-platform compatabilities.
    Adds useful methods.
    """
    suffixDelimiter = "_"
    pathDelimiter = VerInfo().pathDelimiter
    _suffixIO = {"txt": ("txt", "md", ""), "tsv": ("tsv", "csv")}

    def _replaceDelimiters(self, strPath):
        strPath = strPath.replace("/", self.pathDelimiter)
        strPath = strPath.replace("\\", self.pathDelimiter)
        return strPath

    def __init__(self, path):
        verInfo = VerInfo()
        strPath = "" if path is None else str(path)

        strPath = self._replaceDelimiters(strPath=strPath)


        self._path = pathlib.Path(strPath)






        # Simple invalid characters testing from Windows
        for character in '<>"|?*':
            if character in strPath:
                raise InvalidCharacterError(f"Invalid character '{character}' in '{strPath}'")
        if ":" in strPath:
            if not verInfo.pathRootHasColon:
                raise InvalidCharacterError(f"Path has a colon but '{verInfo.os}' doesn't use colon for path root: '{strPath}'")
            if strPath[1] != ":":
                raise InvalidCharacterError(f"Path has a colon but there's no colon at index 1: '{strPath}'")
            if strPath[2] != self.pathDelimiter:
                raise InvalidCharacterError(f"Path has a colon but index 2 is not a delimiter: '{strPath}'")
            if ":" in strPath[2:]:
                raise InvalidCharacterError(f"Path has a colon that's not at index 1: '{strPath}'")

        if not VerInfo().pathRootIsDelimiter and strPath.startswith(self.pathDelimiter):
            strPath = strPath[1:]

        if strPath.endswith(self.pathDelimiter):
            strPath = strPath[0:-1]

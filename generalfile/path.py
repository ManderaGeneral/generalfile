
import pathlib


from generallibrary import VerInfo, initBases, TreeDiagram, Recycle, classproperty

from generalfile.errors import InvalidCharacterError
from generalfile.path_lock import Path_ContextManager
from generalfile.path_operations import Path_Operations
from generalfile.path_strings import Path_Strings
from generalfile.optional_dependencies.path_spreadsheet import Path_Spreadsheet
from generalfile.optional_dependencies.path_text import Path_Text
from generalfile.optional_dependencies.path_cfg import Path_Cfg


@initBases
class Path(TreeDiagram, Recycle, Path_ContextManager, Path_Operations, Path_Strings, Path_Spreadsheet, Path_Text, Path_Cfg):
    """ Immutable cross-platform Path.
        Built on pathlib and TreeDiagram.
        Implements rules to ensure cross-platform compatability.
        Adds useful methods.
        Todo: Add a proper place for all variables, add working_dir, sys.executable and sys.prefix to it.
        Todo: Raise suppressable warning if space in Path.
        Todo: Binary extension. """
    verInfo = VerInfo()
    _path_delimiter = verInfo.pathDelimiter
    Path = ...

    _recycle_keys = {"path": lambda path: Path._scrub(path)}

    def __init__(self, path=None, parent=None):
        path = self._scrub(str_path="" if path is None else path)
        self.path = self.data_keys_add(key="path", value=path, unique=True)

        self._path = pathlib.Path(self.path)

    copy_to = NotImplemented  # Maybe something like this to disable certain methods

    @classproperty
    def path_delimiter(cls):
        return cls._path_delimiter

    def spawn_parents(self):
        if not self._parents:
            path = None
            for pathlib_path in reversed(self._path.parents):
                path = self.Path(path="" if str(pathlib_path) == "." else str(pathlib_path), parent=path)
            self.set_parent(path)

    # def spawn_children(self):
    #     if not self._children and self.is_folder():
    #         for child in self._path.iterdir():
    #             self.Path(child, parent=self)

    def __str__(self):
        # return self.path
        return getattr(self, "path", "<Path not loaded yet>")

    def __repr__(self):
        return self.__str__()

    def __truediv__(self, other):
        """ :rtype: generalfile.Path """
        return self.Path(self._path / str(other))
    
    def __eq__(self, other):
        return self._scrub(self) == self._scrub(other)

    def __hash__(self):
        return hash(str(self))

    def __contains__(self, item):
        return self.path.__contains__(item)

    @classmethod
    def _scrub(cls, str_path):
        str_path = str(str_path)
        str_path = cls._replace_delimiters(str_path=str_path)
        str_path = cls._invalid_characters(str_path=str_path)
        str_path = cls._trim(str_path=str_path)
        str_path = cls._delimiter_suffix_if_root(str_path=str_path)
        return str_path

    @classmethod
    def _replace_delimiters(cls, str_path):
        str_path = str_path.replace("/", cls.path_delimiter)
        str_path = str_path.replace("\\", cls.path_delimiter)
        # str_path = str_path.replace(self.path_delimiter_alternative, self.path_delimiter)  # Don't remember why I commented this
        return str_path

    @classmethod
    def _invalid_characters(cls, str_path):
        # Simple invalid characters testing from Windows
        for character in '<>"|?*':
            if character in str_path:
                raise InvalidCharacterError(f"Invalid character '{character}' in '{str_path}'")
        if ":" in str_path:
            if not cls.verInfo.pathRootHasColon:
                raise InvalidCharacterError(f"Path has a colon but '{cls.verInfo.os}' doesn't use colon for path root: '{str_path}'")
            if str_path[1] != ":":
                raise InvalidCharacterError(f"Path has a colon but there's no colon at index 1: '{str_path}'")
            if len(str_path) >= 3 and str_path[2] != cls.path_delimiter:
                raise InvalidCharacterError(f"Path has a colon but index 2 is not a delimiter: '{str_path}'")
            if ":" in str_path[2:]:
                raise InvalidCharacterError(f"Path has a colon that's not at index 1: '{str_path}'")
        if str_path.endswith("."):
            raise InvalidCharacterError(f"Path cannot end with a dot ('.').")
        return str_path

    @classmethod
    def _trim(cls, str_path):
        if not cls.verInfo.pathRootIsDelimiter and str_path.startswith(cls.path_delimiter):
            str_path = str_path[1:]
        if str_path.endswith(cls.path_delimiter) and len(str_path) > 1:
            str_path = str_path[0:-1]
        return str_path

    @classmethod
    def _delimiter_suffix_if_root(cls, str_path):
        if len(str_path) == 2 and str_path[1] == ":":
            return f"{str_path}{cls.path_delimiter}"
        return str_path

    def view(self, only_last_part=True, indent=1, relative=False, custom_repr=None, spacer=" ", print_out=True):
        """ Override view to use default custom repr. """
        if not self.get_children():
            list(self.get_paths_recursive())

        if only_last_part and custom_repr is None:
            custom_repr = lambda path: path.parts()[-1]
        return TreeDiagram.view(self=self, indent=indent, relative=relative, custom_repr=custom_repr, spacer=spacer, print_out=print_out)

setattr(Path, "Path", Path)
















































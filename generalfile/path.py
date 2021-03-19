
import pathlib
import os


from generallibrary import VerInfo, initBases, TreeDiagram, Recycle, classproperty, deco_cache, hook

from generalfile.errors import InvalidCharacterError
from generalfile.path_lock import Path_ContextManager
from generalfile.path_operations import Path_Operations
from generalfile.path_strings import Path_Strings
from generalfile.optional_dependencies.path_spreadsheet import Path_Spreadsheet
from generalfile.optional_dependencies.path_text import Path_Text
from generalfile.optional_dependencies.path_cfg import Path_Cfg


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

    _recycle_keys = {"path": lambda path: Path.scrub("" if path is None else str(path))}
    # _recycle_keys = {"path": lambda path: hash(Path.scrub(path))}

    def __init__(self, path=None):  # Don't have parent here because of Recycle
        self.path = self.scrub(str_path="" if path is None else str(path))

        self._path = pathlib.Path(self.path)
        self._latest_listdir = set()

    # def __init_post__(self):
    #     self._generate_parent()

    copy_node = NotImplemented  # Maybe something like this to disable certain methods

    @classproperty
    def path_delimiter(cls):
        return cls._path_delimiter

    # def _generate_parent(self):
    def spawn_parents(self):
        if not self.get_parent(spawn=False) and self.path and not self.is_root():
            try:
                index = self.path.rindex(self.path_delimiter)
            except ValueError:
                index = 0
            self.set_parent(Path(path=self.path[:index]))

    def spawn_children(self):
        if self.is_folder():
            old_children = {path.name() for path in self.get_children(spawn=False)}
            new_children = set(os.listdir(self.path if self.path else "."))

            for name in old_children.symmetric_difference(new_children):
                path = Path(path=self / name)
                path.set_parent(self if name in new_children else None)

    def __str__(self):
        return getattr(self, "path", "<Path not loaded yet>")
        # return self.path

    def __repr__(self):
        return self.__str__()

    def __format__(self, format_spec):
        return self.path.__format__(format_spec)

    def __truediv__(self, other):
        """ :rtype: generalfile.Path """
        # print("here", self._recycle_instances)
        return self.Path(self._path / str(other))

    # @deco_cache()
    def __eq__(self, other):
        if isinstance(other, Path):
            other = other.path
        else:
            other = self._scrub("" if other is None else str(other))
        return self.path == other

    def __hash__(self):
        return hash(self.path)

    def __contains__(self, item):
        return self.path.__contains__(item)

    @classmethod
    def _scrub(cls, str_path):
        str_path = cls._replace_delimiters(str_path=str_path)
        str_path = cls._invalid_characters(str_path=str_path)
        str_path = cls._trim(str_path=str_path)
        str_path = cls._delimiter_suffix_if_root(str_path=str_path)
        return str_path

    @classmethod
    @deco_cache()
    def scrub(cls, str_path):
        return cls._scrub(str_path=str_path)

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
        if only_last_part and custom_repr is None:
            custom_repr = lambda path: path.parts()[-1]
        return TreeDiagram.view(self=self, indent=indent, relative=relative, custom_repr=custom_repr, spacer=spacer, print_out=print_out)

setattr(Path, "Path", Path)
# hook(Path.set_parent, Path._generate_parent, after=True)  # Doesn't respect remove_node















































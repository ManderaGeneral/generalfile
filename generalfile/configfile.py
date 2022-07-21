
from generallibrary import comma_and_or, Recycle, ObjInfo, deco_cache, AutoInitBases, DataClass
from generalfile import Path

from itertools import chain


class _ConfigFile_ReadWrite:
    _CFG_HEADER_NAME = "config"
    
    def read_hook(self): ...
    
    def _read_JSON(self):
        """ :param ConfigFile self: """
        return self._path.read()

    def _read_CFG(self):
        """ :param ConfigFile self: """
        return self._path.cfg.read()[self._CFG_HEADER_NAME]

    @deco_cache()
    def _read_config(self):
        """ :param ConfigFile self: """
        if self.exists():
            read_method = {"JSON": self._read_JSON, "CFG": self._read_CFG}[self._format]
            for key, value in read_method().items():
                if key in self.field_keys():
                    self.__dict__[key] = self._unserialize(key, value)  # Don't trigger __setattr__
            
            self.read_hook()

    def _write_JSON(self):
        """ :param ConfigFile self: """
        self._path.write(self.get_config_dict_serializable(), overwrite=True, indent=4)

    def _write_CFG(self):
        """ :param ConfigFile self: """
        config_dict = {self._CFG_HEADER_NAME: self.get_config_dict_serializable()}
        self._path.cfg.write(config_dict, overwrite=True)

    def write_config(self):
        """ :param ConfigFile self: """
        write_method = {"JSON": self._write_JSON, "CFG": self._write_CFG}[self._format]
        write_method()


class _ConfigFile_Serialize:
    @staticmethod
    def _has_serializers(value):
        return hasattr(value, "__dumps__") and hasattr(value, "__loads__")

    @classmethod
    def _serializable(cls, value):
        if value is not None and cls._has_serializers(value):
            return value.__dumps__()
        else:
            return value

    def _unserialize(self, key, value):
        if value is not None and key in self.get_custom_serializers():
            return self.get_custom_serializers()[key].__loads__(value)
        else:
            return value

    def _serializers_from_defaults(self):
        """ :param ConfigFile self: """
        return {key: type(value) for key, value in self.field_dict_defaults().items() if self._has_serializers(value=value)}

    def _serializers_from_annotations(self):
        """ :param ConfigFile self: """
        return {key: cls for key, cls in getattr(self, "__annotations__", {}).items() if self._has_serializers(value=cls)}

    @deco_cache()
    def get_custom_serializers(self):
        """ :param ConfigFile self: """
        combined = chain(
            self._serializers_from_defaults().items(),
            self._serializers_from_annotations().items(),
        )
        return {key: value for key, value in combined if key in self.field_keys()}

    def get_config_dict_serializable(self):
        """ :param ConfigFile self: """
        return {key: self._serializable(value) for key, value in self.field_dict().items()}




class ConfigFile(Recycle, DataClass, _ConfigFile_Serialize, _ConfigFile_ReadWrite, metaclass=AutoInitBases):
    """ Read config file when created.
        If value changes then write to file.
        Path must have support format suffix.
        Default value or annotation cls can define __dumps__ and __loads__.
        'name: str' will do nothing, must write 'name: str = None'
        Keys of dictionaries must be strings.

        Todo: Handle custom serializers within iterable for ConfigFile. """

    _supported_formats = {
        ".json": "JSON",
        ".cfg": "CFG",
    }

    _recycle_keys = {"path": lambda path: str(ConfigFile._scrub_path(path=path))}

    def __init__(self, path):
        self._path = self._scrub_path(path=path)
        self._format = self._supported_formats[self._path.suffix().lower()]

    def __repr__(self):
        return f"<{type(self).__name__} for '{self._path}'>"

    @classmethod
    def _scrub_path(cls, path):
        path = Path(path).absolute()
        assert path.suffix().lower() in cls._supported_formats, f"Path must end with {comma_and_or(*cls._supported_formats)}"
        return path

    def exists(self):
        return self._path.exists()

    def __setattr__(self, key, value):
        prev_value = getattr(self, key, ...)
        super().__setattr__(key, value)
        if key in self.field_keys():
            if prev_value != value:
                self.write_config()

    def __getattribute__(self, item):
        if item != "field_keys" and item in self.field_keys():
            self._read_config()
        return super().__getattribute__(item)

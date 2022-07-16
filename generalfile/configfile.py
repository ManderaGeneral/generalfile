from generallibrary import comma_and_or, Recycle, dumps, ObjInfo, deco_cache

from generalfile import Path

from generalpackager import LocalRepo



class ConfigFile(Recycle):
    _supported_formats = {
        ".json": Path,
        ".cfg": Path.cfg,
    }

    _recycle_keys = {"path": lambda path: str(ConfigFile._scrub_path(path=path))}

    def __init__(self, path):
        self.path = self._scrub_path(path=path)
        self._load_config()

    def _load_config(self):
        if self.exists():
            for key, value in self.path.read().items():
                self.__dict__[key] = value  # Don't trigger __setattr__

    @classmethod
    def _scrub_path(cls, path):
        path = Path(path).absolute()
        assert path.suffix().lower() in cls._supported_formats, f"Path must end with {comma_and_or(*cls._supported_formats)}"
        return path

    def exists(self):
        return self.path.exists()

    @property
    @deco_cache()
    def config_keys(self):
        """ Get a list of keys defined by subclass. """
        def filt(objinfo: ObjInfo):
            return objinfo.is_instance()
        objinfos = ObjInfo(type(self)).get_children(traverse_excluded=True, filt=filt, gen=True)
        return [objinfo.name for objinfo in objinfos]

    def config_dict(self):
        """ Get current metadata values as a dict. """
        return {key: getattr(self, key) for key in self.config_keys}

    def __setattr__(self, key, value):
        prev_value = getattr(self, key, ...)
        super().__setattr__(key, value)
        if key in self.config_keys and prev_value != value:
            self.path.write(self.config_dict(), overwrite=True, indent=4)


#     def load_metadata(self):
#         """ Read metadata path and load values. """
#         self.has_loaded_file = True
#         if self.exists():
#             for key, value in self.get_metadata_path().read().items():
#                 setattr(self, f"_{key}", value)
#
#             if self.extras_require:
#                 self.extras_require["full"] = list(set().union(*self.extras_require.values()))
#                 self.extras_require["full"].sort()
#
#             self.version = Ver(self.version)
#
#         if self.name is Ellipsis:
#             self.name = self.path.name()
#
#     def get_metadata_dict(self):
#         """ Get current metadata values as a dict. """
#         return {key: str(getattr(self, key)) if key == "version" else getattr(self, key) for key in self.metadata_keys}
#
#     def write_metadata(self):
#         """ Write to metadata path using current metadata values. """
#         self.get_metadata_path().write(self.get_metadata_dict(), overwrite=True, indent=4)
#
#
#     @load_metadata_before
#     def _metadata_getter(self, key):
#         return getattr(self, f"_{key}")
#
#     @load_metadata_before
#     def _metadata_setter(self, key, value):
#         """ Set a metadata's key both in instance and json file. """
#         if self.has_metadata() and value != getattr(self, f"_{key}", ...):
#             metadata = self.get_metadata_path().read()
#             metadata[key] = str(value) if key == "version" else value  # Todo: Decoupled JSON serialize instructions with custom dumps in lib.
#             self.get_metadata_path().write(metadata, overwrite=True, indent=4)
#         setattr(self, f"_{key}", value)
#
# for key in LocalRepo.metadata_keys:
#     value = getattr(LocalRepo, key)
#     setattr(LocalRepo, f"_{key}", value)
#     setattr(LocalRepo, key, property(
#         fget=lambda self, key=key: LocalRepo._metadata_getter(self, key),
#         fset=lambda self, value, key=key: LocalRepo._metadata_setter(self, key, value),
#     ))

from generalpackager.api.localrepo.base.metadata import Metadata

class Metadata_Python(Metadata):
    install_requires = []
    extras_require = {}

    def read_hook(self):
        extras_require = self.halt_getattr("extras_require")
        if extras_require:
            keys = [key for key in extras_require.values() if key != "full"]
            extras_require["full"] = list(set().union(*keys))
            extras_require["full"].sort()

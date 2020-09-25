

from generallibrary import deco_cache


class _Spreadsheet:
    def __init__(self, path_cls):
        import pandas
        self.pd = pandas
        self.path_cls = path_cls

    def write(self, df):
        print(self.path_cls.write)
        # with Path.write_context() as stream:
        #     pass


class _Path_Optional:
    @property
    def spreadsheet(self):
        return self._spreadsheet(self.__class__)

    @staticmethod
    @deco_cache()
    def _spreadsheet(path_cls):
        return _Spreadsheet(path_cls)


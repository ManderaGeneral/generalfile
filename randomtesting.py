from typing import Literal, get_args, get_origin
import inspect
from generallibrary import auto_deco

import dataclasses as dc


class DataClass(metaclass=auto_deco(dc.dataclass)):
    def fields(self):
        return dc.fields(self)

    def asdict(self):
        return dc.asdict(self)

    @property
    @deco_cache()
    def dict(self):
        return self.path.read(default={})


# from typing import Literal
#
# class ConfigFile(DataClass):
#     def __init__(self, fmt: Literal["JSON", "CFG"]):
#         """ :param  fmt: """
#         print("hi")
#
#
# a = ConfigFile(fmt="CFG")
#
# print(a)




# class SettingsFile:
#     def __init__(self, path):
#         pass







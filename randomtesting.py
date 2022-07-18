
from generalfile.configfile import ConfigFile

from generallibrary import Ver


class A(ConfigFile):
    name = "foo"
    ver = Ver(1.3)
    ver2: Ver = None  # Make this work too


a = A("foo.json")
a.name = "hi"


# print(a.get_config_dict())
a._write_config()

print(a.get_config_dict())




from generalfile.configfile import ConfigFile




class A(ConfigFile):
    name = "foo"


a = A("foo.json")
a.name = "hi"


# print(a.config_dict())




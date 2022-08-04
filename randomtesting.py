
from generalfile.configfile import ConfigFile


class A(ConfigFile):
    foo = "bar"


a = A("foo.cfg")


print(a.foo)

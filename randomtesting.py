
from generalfile.configfile import ConfigFile

from generallibrary import Ver

from itertools import chain

class A(ConfigFile):
    ver: Ver = None

a = A("foo.cfg")

# a.ver = Ver(1.3)

print(a.ver)
print(a.ver)

# a.ver = None


# print(a.ver)


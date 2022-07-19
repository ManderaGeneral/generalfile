
from generalfile.configfile import ConfigFile

from generallibrary import Ver

from itertools import chain

class A(ConfigFile):
    ver = Ver("1.2.4")

a = A("foo.cfg")

print(a.ver)

a.ver = a.ver.bump()
print(a.ver)


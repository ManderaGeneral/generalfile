from copy import copy

from generalfile import *
from generalfile.test.setup_workdir import setup_workdir

from generallibrary import Ver

from tomllib import load

# Path("test.ini").cfg.write({"section": {'test': ["hi", 5]}}, overwrite=True)
# print(Path("test.ini").cfg.read()["section"]["test"][1])


# dict_ = {'test': {'foo': 'bar', 'number': 2, 'hi': ['a', 'b', 3], "uh": None}}

# HERE ** Need to allow None values for ConfigFile etc

dict_ = {'test': {'foo': True, "x": None, "y": {"foo": "bar", "x": None}}}
Path("foo").cfg.write(dict_, overwrite=True)
print(Path("foo").cfg.read())



# Seems like list works without any change now
# https://stackoverflow.com/questions/335695/lists-in-configparser


# print(Path("test.ini").cfg.write({"hi": "foo"}))

# import configparser
#
# config = configparser.ConfigParser()

# print(load(Path("test.toml").text.read()))

# parser = configparser.ConfigParser()
# parser.read("test.ini", encoding="utf-8")
# print({section: dict(parser.items(section)) for section in parser.sections()})



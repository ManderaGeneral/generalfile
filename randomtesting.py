
from generalfile import Path
from generalfile.test.setUpWorkDir import setUpWorkDir
import pathlib
import mutapath
import appdirs
import time
import os
from pprint import pprint

import shutil

from distutils.dir_util import copy_tree

import random

from generallibrary import sleep





# setUpWorkDir()

# Path.get_lock_dir().open_folder()
# Path().open_folder()



# Path("fold/hello/test.txt").write(5)
# Path("test.txt").write(1)
# Path("fold/hello/another/test2.txt").write(2)



# Path("hi.txt").write()
# print(Path("hi.txt").seconds_since_creation())

with Path("test").lock():
    print(5)



# TODO: Replace dots in lock paths too
# TODO: Dryer: os.remove should only be exist inside Path.delete for example - Add parameter to methods that lock to not lock



# import functools
# class Test:
#     def __init__(self, a):
#         self.a = a
#
#     def foo(self):
#         return self.a.hi()
#
# class A:
#     @property
#     @functools.lru_cache()
#     def Test(self):
#         return Test(self)
#
#     def hi(self):
#         return 5
# a = A()
# print(id(a.Test))
# print(A().Test.foo())
# print(id(a.Test))

# IDEAS FOR HOW TO SEPERATE E.G. TSV FROM PLAIN

# Example: Path("hello.tsv").spreadsheet.write(pd.DataFrame())
# Only create once, if needed
# Reusable
# No need for paranthesis

# CONS: Hard to get list of options (spreadsheet / plain etc.)
#           Very long solution -> Could put them all in yet another object ( Path("hello.tsv").methods.spreadsheet.write(pd.DataFrame()) )
#           Inside Path.write/read we can list them all
# PROS: Can write specific docstrings for each different write and read method
#       All e.g. spreadsheet methods are inside that object




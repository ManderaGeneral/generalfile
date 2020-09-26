
from generalfile import Path
from generalfile.test.setup_workdir import setup_workdir
import pathlib
import mutapath
import appdirs
import time
import os
from pprint import pprint
import pandas as pd
import shutil

from distutils.dir_util import copy_tree

import random

from generallibrary import sleep




# Path.get_lock_dir().open_folder()



setup_workdir()

# Path().open_folder()
Path("hello.tsv").spreadsheet.write(pd.DataFrame([[1, 2, 3], [1, 2, 3]]))
print(Path("hello.tsv").spreadsheet.read())

Path("hello.tsv").spreadsheet.append([[4, 5, 6]])
print(Path("hello.tsv").spreadsheet.read())


# TODO: Make sure we have all functionality that generalfile has
# TODO: Decide on where to put e.g. CSV functionality


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



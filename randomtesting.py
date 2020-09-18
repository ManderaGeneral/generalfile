
# import generalfile
from generalfile import Path
from generalfile.test.setUpWorkDir import setUpWorkDir
import pathlib
import mutapath
import appdirs
import time
import os
from pprint import pprint

import shutil

import random


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










# Path().open_folder()
# Path.get_lock_dir().open_folder()


setUpWorkDir()
# path = Path("folder/test.txt")
# path.write(5)
# path.rename("hello.txt")
# print(Path("hello.txt").read())


Path("test.txt").write()


shutil.copy("test.txt", "test2.txt", follow_symlinks=False)


# print(pathlib.Path("folder/hello.txt"))

# print(list(generalfile.Path("randomtesting.py").get_paths()))
# print(appdirs.user_cache_dir())
# print(pathlib.Path("folder/file.txt.hi"))
# print(mutapath.Path("folder/file.txt"))
# print(generalfile.Path("folder/file.txt"))


# import generalfile
from generalfile import Path
from generalfile.test.setUpWorkDir import setUpWorkDir
import pathlib
import mutapath
import appdirs
import time
import os
from pprint import pprint


Path.get_lock_dir().open_folder()

setUpWorkDir()


path = Path("folder/test.txt")
path.write()
# path.rename("hello.txt")



# print(pathlib.Path("folder/hello.txt"))

# print(list(generalfile.Path("randomtesting.py").get_paths()))
# print(appdirs.user_cache_dir())
# print(pathlib.Path("folder/file.txt.hi"))
# print(mutapath.Path("folder/file.txt"))
# print(generalfile.Path("folder/file.txt"))


# import generalfile
from generalfile import Path
import pathlib
import mutapath
import appdirs
import time
import os

Path.get_lock_dir().open_folder()

Path.get_lock_dir().delete_folder_content()

with Path("hello"):
    time.sleep(3)



# print(list(generalfile.Path("randomtesting.py").get_paths()))
# print(appdirs.user_cache_dir())
# print(pathlib.Path("folder/file.txt.hi"))
# print(mutapath.Path("folder/file.txt"))
# print(generalfile.Path("folder/file.txt"))

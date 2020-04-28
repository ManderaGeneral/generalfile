"""
Random testing
"""
import pandas as pd
from generalfile import *
import os
import shutil
import generallibrary as lib

test.SetUpWorkDir.activate()
# File.openFolder("")




File.write("folder/folder2/test.txt")

# File.clearFolder("", delete=True)

# File.setWorkingDir(File.getWorkingDir().getParent())


lib.sleep(2)

shutil.rmtree(Path().getParent(2).addPath("hello"), ignore_errors=True)



# File.setWorkingDir("test/tests")




# df = pd.DataFrame({
#     "a": {"color": "red", "value": 5},
#     "b": {"color": "red", "value": 2}
# })
# File.write("df.tsv", df, overwrite=True)
# print(df)
# df = File.read("df.tsv")
# print(df)

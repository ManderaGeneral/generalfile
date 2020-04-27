"""
Random testing
"""
import pandas as pd
from generalfile import *



test.SetUpWorkDir.activate()

print(File.getWorkingDir())



# File.setWorkingDir("test/tests")




# df = pd.DataFrame({
#     "a": {"color": "red", "value": 5},
#     "b": {"color": "red", "value": 2}
# })
# File.write("df.tsv", df, overwrite=True)
# print(df)
# df = File.read("df.tsv")
# print(df)

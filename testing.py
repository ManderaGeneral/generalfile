"""
Random testing
"""
from generalfile import *
import pandas as pd


File.setWorkingDir("test/tests")


df = pd.DataFrame({
    "a": {"color": "red", "value": 5},
    "b": {"color": "red", "value": 2}
})

# df = pd.DataFrame([
#     {"color": "red", "value": 5},
#     {"color": "red", "value": 2}
# ])



FileTSV.write("df.tsv", df, overwrite=True)

print(df)

df = FileTSV.read("df.tsv")

print(df)

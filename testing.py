"""
Random testing
"""
from generalfile import *
import pandas as pd
from generallibrary import *



File.setWorkingDir("test/tests")


df = pd.DataFrame({
    "a": {"color": "red", "value": 5},
    "b": {"color": "red", "value": 2}
})



File.write("df.tsv", df, overwrite=True)
print(df)
df = File.read("df.tsv")
print(df)

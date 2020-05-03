"""
Random local testing
"""


from generalfile.base.classfile import File
from test.base.setUpWorkDir import SetUpWorkDir
import pandas as pd

SetUpWorkDir.activate()
# File.openFolder("")


# df = pd.DataFrame([["color", "value"], ["blue", 5], ["red", 3]])
df = pd.DataFrame()

File.write("df.tsv", df)

print(File.read("df.tsv"))

# File.tsvAppend("df.tsv", ["green", 8])
# File.tsvAppend("df.tsv", 8)
# File.tsvAppend("df.tsv", 8)




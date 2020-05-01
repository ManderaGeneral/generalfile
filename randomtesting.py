"""
Random local testing
"""


from generalfile.base.classfile import File
from test.base.setUpWorkDir import SetUpWorkDir
import pandas as pd

SetUpWorkDir.activate()
# File.openFolder("")


# df = pd.DataFrame({
#     "a": {"color": "red", "value": "5"},
#     "b": {"color": "blue", "value": "2"}
# })
#
# File.write("df.tsv", df)
# read = File.read("df.tsv")
#
# pd.testing.assert_frame_equal(df, read)


df = pd.DataFrame([
    [1, 2, 3],
    [4, 5, 6]
])


File.write("df.tsv", df, overwrite=True)
read = File.read("df.tsv")


print(df[0])
print(read[0])






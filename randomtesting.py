"""
Random local testing
"""


from generalfile.base.classfile import File
from test.base.setUpWorkDir import SetUpWorkDir
import pandas as pd

SetUpWorkDir.activate()
# File.openFolder("")



def dfInfo(df):
    print(df)
    print()
    print("keys: ", df.keys())
    print("index: ", df.index)
    print()

def test(name, obj):
    path = f"{name}.tsv"
    df = pd.DataFrame(obj)
    File.write(path, df, overwrite=True)
    read = File.read(path)
    print(name)
    print()
    dfInfo(df)
    # dfInfo(read)

    print()
    print("-----------------------")
    print()
    return read



# df = pd.DataFrame({
#     "a": {"color": "red", "value": "5"},
#     "b": {"color": "blue", "value": "2"}
# })
#
# File.write("df.tsv", df)
# read = File.read("df.tsv")
#
# pd.testing.assert_frame_equal(df, read)




test("1dd", {"a": {"color": "red", "value": 5},"b": {"color": "blue", "value": 2}})
test("2ld", [{"color": "red", "value": 5}, {"color": "blue", "value": 2}])
test("3dl", {"a": ["red", 5], "b": ["blue", 2]})
test("4ll", [["red", 5], ["blue", 2]])







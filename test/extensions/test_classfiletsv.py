"""
Tests for class FileTSV
"""
import unittest
import pandas as pd

from generalfile.base.classfile import File
from test.base.setUpWorkDir import SetUpWorkDir
from generallibrary.iterables import joinWithStr

def dfInfo(df):
    print(df)
    print()
    print("keys: ", File._indexIsNamed(df.columns), df.columns)
    print("index: ", df.index)
    # print("name", df.index.name)
    print()


class FileTSVTest(unittest.TestCase):
    def setUp(self):
        """Set working dir and clear folder"""
        SetUpWorkDir.activate()

    def compareFrames(self, df1, df2):
        """
        Compare two frames.
        Tried using panda's own but I cannot find a way to disable the type checking.
        Having issues with the dtype being object/str and str/float/int.
        Int indexes are also converted to strings, cannot find any way to keep the RangeIndex for columns

        :param pd.DataFrame df1:
        :param pd.DataFrame df2:
        """
        dfInfo(df1)
        dfInfo(df2)
        print("--------")
        self.assertEqual(df1.shape, df2.shape)
        self.assertTrue(df1.columns.equals(df2.columns))
        self.assertTrue(df1.index.equals(df2.index))

    def writeAndCompareObj(self, df):
        header, column = File.write("df.tsv", df, overwrite=True)
        read = File.read("df.tsv", header=header, column=column)
        # print(header, column)
        self.compareFrames(df, read)

    def doTestsOnDataFrame(self, df):
        self.writeAndCompareObj(df)
        self.writeAndCompareObj(df.T)

    def test_tsv(self):
        self.doTestsOnDataFrame(pd.DataFrame({"a": {"color": "red", "value": 5}, "b": {"color": "blue", "value": 2}}))
        self.doTestsOnDataFrame(pd.DataFrame([{"color": "red", "value": 5}, {"color": "blue", "value": 2}]))
        self.doTestsOnDataFrame(pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}))
        self.doTestsOnDataFrame(pd.DataFrame([[1, 2, 3], [4, 5, 6]]))

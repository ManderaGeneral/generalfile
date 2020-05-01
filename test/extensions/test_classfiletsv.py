"""
Tests for class FileTSV
"""
import unittest
import pandas as pd

from generalfile.base.classfile import File
from test.base.setUpWorkDir import SetUpWorkDir
from generallibrary.iterables import joinWithStr

class FileTSVTest(unittest.TestCase):
    def setUp(self):
        """Set working dir and clear folder"""
        SetUpWorkDir.activate()

    def compareFrames(self, df1, df2):
        """
        Compare two frames.
        Tried using panda's own but I cannot find a way to disable the type checking.
        Having issues with the dtype being object/str and str/float/int.
        Int indexes are also converted to strings, cannot find any way to keep the RangeIndex for keys()

        :param pd.DataFrame df1:
        :param pd.DataFrame df2:
        """
        self.assertEqual(joinWithStr(list(df1.keys()), ","), joinWithStr(list(df2.keys()), ","))
        self.assertEqual(df1.shape, df2.shape)

    def writeObj(self, df):
        File.write("df.tsv", df, overwrite=True)
        read = File.read("df.tsv")
        self.compareFrames(df, read)

    def doTestsWithObj(self, obj):
        df = pd.DataFrame(obj)
        self.writeObj(df)
        self.writeObj(df.T)

    def test_tsv(self):
        self.doTestsWithObj({
            "a": {"color": "red", "value": 5},
            "b": {"color": "blue", "value": 2}
        })
        self.doTestsWithObj({
            "a": [1, 2, 3],
            "b": [4, 5, 6]
        })
        self.doTestsWithObj([
            [1, 2, 3],
            [4, 5, 6]
        ])
        self.doTestsWithObj([
            {"color": "red", "value": 5},
            {"color": "blue", "value": 2}
        ])


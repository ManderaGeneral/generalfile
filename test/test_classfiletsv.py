"""
Tests for class FileTSV
"""

from .test_classfile import FileTest
from extensions.classfiletsv import *

class FileTSVTest(FileTest):
    """
    Inherit FileTest which sets up our working dir nicely.
    """
    def test__write_tsv(self):
        df = pd.DataFrame({
            "a": {"color": "red", "value": 5},
            "b": {"color": "red", "value": 2}
        })

    def test__read_tsv(self):
        pass


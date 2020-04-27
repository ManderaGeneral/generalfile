"""
Tests for class FileXXX
"""

from test.base.test_classfile import SetUpWorkDir
from generalfile import *

import unittest

class FileXXXTest(unittest.TestCase):
    def setUp(self):
        """Set working dir and clear folder"""
        SetUpWorkDir.activate()

    def test__write_XXX(self):
        pass

    def test__read_XXX(self):
        pass


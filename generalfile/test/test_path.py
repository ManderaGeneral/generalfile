
import unittest

from generalfile import Path
from generalfile.errors import *




class FileTest(unittest.TestCase):
    def test_path(self):
        self.assertRaises(InvalidCharacterError, Path, "hello:there")
        self.assertRaises(InvalidCharacterError, Path, "hello<")
        self.assertRaises(InvalidCharacterError, Path, "hello>")

    def test_addPath(self):
        self.assertEqual(Path("foo/bar"), Path("foo") / "bar")
        self.assertEqual(Path("foo/bar"), Path("foo") / Path("bar"))

    def test_properties(self):
        path = Path("test/foo.bar")

        self.assertEqual("test", path.parent)
        self.assertEqual("foo", path.stem)
        self.assertEqual(".bar", path.suffix)

    def test_write(self):
        self.assertEqual("test", Path("hello").write("foobar"))
        self.assertEqual("foobar", Path("test.txt").write("foobar"))
        self.assertEqual("foobar", Path("test.txt").write("foobar"))

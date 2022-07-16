
from generalfile.test.test_path import PathTest
from generalfile.configfile import ConfigFile


class TestConfigFile(PathTest):
    def test_suffix(self):
        class A(ConfigFile):
            name = "foo"
        self.assertRaises(AssertionError, A, path="hi")
        self.assertRaises(AssertionError, A, path="json")
        self.assertRaises(AssertionError, A, path="foo.json.test")
        A(path="foo.json")
        A(path="foos.JSON")
        A(path="foo.cfg")
        A(path="foos.CFG")
        A(path="foo.test.cfg")

    def test_name(self):
        class A(ConfigFile):
            name = "foo"
        a = A(path="foo.json")
        self.assertEqual("foo", a.name)

        a.name = "bar"
        self.assertEqual("bar", a.name)


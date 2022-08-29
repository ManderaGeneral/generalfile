from generalfile import Path
from generallibrary import Log

from generalpackager import Packager
from generalpackager.test.workingdir import WorkingDirTestCase

class TestPackager(WorkingDirTestCase):
    def test_relative_path_is_aesthetic(self):
        packager = Packager()
        self.assertEqual(False, packager.relative_path_is_aesthetic("setup.py"))
        self.assertEqual(True, packager.relative_path_is_aesthetic("README.md"))
        self.assertEqual(True, packager.relative_path_is_aesthetic(packager.localrepo.get_readme_path()))

    def test_filter_relative_filenames(self):
        packager = Packager()
        self.assertEqual(["setup.py"], packager.filter_relative_filenames("setup.py", aesthetic=None))
        self.assertEqual(["setup.py"], packager.filter_relative_filenames("setup.py", aesthetic=False))
        self.assertEqual([], packager.filter_relative_filenames("setup.py", aesthetic=True))

    def test_compare_local_to_github(self):
        packager = Packager()
        packager.compare_local_to_github()

    def test_compare_local_to_pypi(self):
        packager = Packager()
        packager.compare_local_to_pypi()

    def test_generate_setup(self):
        packager = Packager()
        text = packager.generate_setup()
        self.assertIn(str(packager.localrepo.metadata.version), text)
        self.assertIn(str(packager.localrepo.name), text)

    def test_generate_manifest(self):
        packager = Packager()
        text = packager.generate_manifest()
        self.assertIn("include metadata.json", text)

    def test_generate_git_exclude(self):
        packager = Packager()
        text = packager.generate_git_exclude()
        self.assertIn(".idea", text)

    def test_generate_license(self):
        packager = Packager()
        text = packager.generate_license()
        self.assertIn("Mandera", text)

    def test_generate_workflow(self):
        packager = Packager()
        text = packager.generate_workflow()
        self.assertIn("runs-on", text)

    def test_generate_readme(self):
        packager = Packager()
        text = str(packager.generate_readme())
        self.assertIn("pip install", text)

    def test_generate_personal_readme(self):
        packager = Packager()
        self.assertIsNotNone(packager.path)
        text = str(packager.generate_personal_readme())
        self.assertIn("generallibrary", text)

    def test_get_new_packager(self):
        a = Packager()
        b = a.get_new_packager()
        self.assertEqual(a.name, b.name)
        self.assertIsNot(a, b)
        self.assertIs(b, Packager())


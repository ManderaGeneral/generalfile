
from generallibrary import Ver
from generalpackager.api.localrepo.base.localrepo import LocalRepo
from generalpackager.test.workingdir import WorkingDirTestCase

class TestLocalRepo(WorkingDirTestCase):
    def test_metadata_exists(self):
        self.assertEqual(True, LocalRepo().metadata_exists())
        self.assertEqual(False, LocalRepo("doesntexist").metadata_exists())

    def test_load_metadata(self):
        self.assertEqual(True, LocalRepo().metadata.enabled)
        self.assertEqual("generalpackager", LocalRepo().name)
        self.assertIsInstance(LocalRepo().metadata.version, Ver)
        self.assertIsInstance(LocalRepo().metadata.description, str)
        self.assertIsInstance(LocalRepo().metadata.topics, list)
        self.assertIsInstance(LocalRepo().metadata.manifest, list)

        self.assertIsInstance(LocalRepo().targetted().metadata.install_requires, list)
        self.assertIsInstance(LocalRepo().targetted().metadata.extras_require, dict)

    def test_exists(self):
        self.assertEqual(True, LocalRepo().exists())
        self.assertEqual(True, LocalRepo.repo_exists(LocalRepo().path))

        self.assertEqual(False, LocalRepo("doesntexist").exists())

    def test_get_test_paths(self):
        self.assertLess(2, len(list(LocalRepo().get_test_paths())))
        self.assertIn(LocalRepo().get_test_path() / "test_local_repo.py", LocalRepo().get_test_paths())

    def test_text_in_tests(self):
        self.assertEqual(True, LocalRepo().text_in_tests("stringthatexists"))
        self.assertEqual(False, LocalRepo().text_in_tests("stringthat" + "doesntexist"))

    def test_get_package_paths(self):
        package_paths = list(LocalRepo().get_package_paths_gen())
        self.assertIn(LocalRepo().get_test_path(), package_paths)
        self.assertIn(LocalRepo().path / LocalRepo().name, package_paths)
        self.assertNotIn(LocalRepo().path, package_paths)

    def test_get_changed_files(self):
        local_repo = LocalRepo()
        version = local_repo.metadata.version
        local_repo.bump_version()
        self.assertNotEqual(local_repo.metadata.version, version)
        self.assertIn("metadata.json", local_repo.git_changed_files())
        local_repo.metadata.version = version
        self.assertEqual(local_repo.metadata.version, version)
































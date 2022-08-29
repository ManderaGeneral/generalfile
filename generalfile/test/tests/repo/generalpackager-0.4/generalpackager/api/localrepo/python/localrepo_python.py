
from generalpackager.api.localrepo.base.localrepo import LocalRepo
from generalpackager.api.localrepo.python.metadata_python import Metadata_Python

from generalfile import Path
from generallibrary import terminal, EnvVar, deco_require, Log


class LocalRepo_Python(LocalRepo):
    cls_target = LocalRepo.Targets.python
    cls_metadata = Metadata_Python

    @staticmethod
    def get_venv_path():
        """ Return an absolute path to the current VENV.

            :raises KeyError: If no VENV """
        return Path(EnvVar("VIRTUAL_ENV").value)

    def unittest(self):
        """ Run unittests for this repository. """
        terminal("-m", "unittest", "discover", str(self.get_test_path()), python=True)

    @deco_require(LocalRepo.exists)
    def pip_install(self):
        """ Install this repository with pip and -e flag. """
        with self.path.as_working_dir():
            Log().debug(f"Pip install for {self}")
            terminal("pip", "install", "-e", ".")

    @deco_require(LocalRepo.exists)
    def pip_uninstall(self):
        """ Uninstall this repository with pip."""
        terminal("-m", "pip", "uninstall", "-y", self.metadata.name, python=True)

    @deco_require(LocalRepo.exists)
    def create_sdist(self):
        """ Create source distribution. """
        with self.path.as_working_dir():
            terminal("setup.py", "sdist", "bdist_wheel", python=True)

    @deco_require(LocalRepo.exists)
    def upload(self):
        """ Upload local repo to PyPI.
            Todo: Make sure twine is installed when trying to upload to pypi. """
        if self.metadata.private:
            raise AttributeError("Cannot upload private repo.")

        self.create_sdist()
        with self.path.as_working_dir():
            terminal("-m", "twine", "upload", "dist/*", python=True)

    @deco_require(LocalRepo.exists)
    def generate_exe(self, file_path=None, suppress=False):
        """ Generate an exe file for target file_path python file. """
        if file_path is None:
            file_path = self.get_exetarget_path()
        assert file_path.exists()

        with self.path.as_working_dir():
            terminal("-m", "PyInstaller", file_path, "--onefile", "--windowed", python=True, suppress=suppress)
            # terminal("-m", "PyInstaller", file_path, "--onefile", "--windowed", "--name", self.name, python=True, suppress=suppress)  # Failed for some reason

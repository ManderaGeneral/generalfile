"""Just contains class for File handling tests"""


def setup_workdir():
    """ Class to set up working dir for tests, File extensions import this class.
        Set working dir and clear it after it's made sure it's correct path."""
    path = Path(__file__).parent() / "tests"

    if not path.endswith("test/tests"):
        raise EnvironmentError(f"Failed setting correct working dir, should be ..test/tests but it's {path}")

    # HERE ** Works now, problem was deleting working dir.

    path.delete_folder_content()
    path.set_working_dir()

from generalfile.path import Path

"""Just contains class for File handling tests"""
from generalfile import *

class SetUpWorkDir:
    """Class to set up working dir for tests, File extensions import this class."""
    workingDir = Path("test/tests").getAbsolute()
    if not workingDir.getParent().endsWithPath("test"):
        raise EnvironmentError(f"Failed setting correct working dir, should be ..test/tests but it's {workingDir}")

    @classmethod
    def activate(cls):
        """Set working dir and clear it after it's made sure it's correct path."""
        File.setWorkingDir(cls.workingDir)
        if File.getWorkingDir().endsWithPath("tests"):
            File.clearFolder("", delete=True)
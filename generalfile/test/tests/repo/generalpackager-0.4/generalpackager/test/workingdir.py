from unittest import TestCase
import generalpackager
from generalfile import Path

class WorkingDirTestCase(TestCase):
    _original_working_dir = Path.get_working_dir()

    @classmethod
    def setUpClass(cls):
        path = Path(generalpackager.__file__).get_parent(1, 1)  # type: Path
        path.set_working_dir()

    @classmethod
    def tearDownClass(cls):
        cls._original_working_dir.set_working_dir()
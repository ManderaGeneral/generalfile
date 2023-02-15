
from generalfile import *

from generalpackager import Venv
import sys

print(sys.path)
# print(Venv.get_active_venv().python_home_exe_path())
from generalfile.test.setup_workdir import setup_workdir

from generallibrary import Ver

# Path("hi").write()

# with Path("hi").as_renamed("hello") as path:
#     print(path, path.exists())


# print((Path("hi").as_working_dir(context=False)))

# with Path("hi").as_working_dir() as path:
#     print(path, Path.get_working_dir())

# print(Path.get_working_dir())






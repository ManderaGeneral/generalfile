
from generalfile import Path

from generalfile.test.setup_workdir import setup_workdir


# print(Path.get_lock_dir())

# with Path("helo").lock():
# with Path("/helo.txt").lock():


# with Path("/home/Mandera/python/generalfile/test/tests").lock():
#     print(5)

# setup_workdir()

# print(__file__)
# print(Path(__file__) / "tests")


path = Path("hello").absolute()
path.set_working_dir()
path.delete_folder_content()
print(Path.get_working_dir())


# TODO: get_working_dir raises error cus it doesn't exist in test_absolute
# TODO: Doesn't seem to able to remove dead locks

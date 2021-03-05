


from generalfile import Path
from generalfile.test.setup_workdir import setup_workdir
# setup_workdir()
# Path.get_working_dir().open_folder()
# Path.get_lock_dir().open_folder()

# from pprint import pprint

setup_workdir()

# Path().open_folder()

path = Path("base/test.txt")
path.write("hello")

target = Path("target/packed")

Path("base").pack(target)

target.unpack("base")



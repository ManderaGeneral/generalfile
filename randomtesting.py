
from generalfile import Path
from generalfile.test.setup_workdir import setup_workdir


# Path("generalfile/doesntexist").get_parent()

# print(Path("generalfile").get_children())
# print(Path("generalfile").get_children(filt=Path.exists))


# HERE ** Fix tests

setup_workdir()

Path("hi").write("hey")

# print(Path.get_lock_dir().get_children())

# Path.get_lock_dir().open_folder()

# Path("a/b").write("foo")
# Path("a").delete()
# print(Path("a").get_children())



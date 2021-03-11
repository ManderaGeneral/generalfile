
from generalfile import Path
from generalfile.test.setup_workdir import setup_workdir


Path.set_path_delimiter("/")
setup_workdir()

print(Path("hi").get_lock_path().from_alternative())  # HERE ** Why is lock dir using old delimiter

# Path("hi").write("hello")

# with Path("hi").lock():
#     pass

# Path.get_lock_dir().open_folder()


# print(id(Path()._children))
# print(id(Path()._children))

# print(Path().get_children())
# print(list(Path().get_paths_in_folder()))
# print(Path().get_children())
# print(path.get_children())


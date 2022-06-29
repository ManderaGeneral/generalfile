
from generalfile import Path
from generalfile.test.setup_workdir import setup_workdir

from generallibrary import TreeDiagram

# class A(TreeDiagram):
#     pass
# a = A()
# b = a.add_node()
# print(a.get_children())
# b.set_parent(None)
# print(a.get_children())


setup_workdir()
print(Path().empty())
Path("foo").write("bar")
print(Path().empty())
setup_workdir()
print(Path().empty())

print(Path().get_children())

# Path().open_folder()

# Path().delete()


from generalfile import Path
from generalfile.test.setup_workdir import setup_workdir


setup_workdir()

Path("a/b").write("foo")

Path("a").delete()

print(Path("a").get_children())



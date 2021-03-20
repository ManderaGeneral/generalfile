
from generalfile import Path
from generalfile.test.setup_workdir import setup_workdir


print(Path("C:/").parts())

Path("C:/").get_children(depth=1)

Path("C:/").view()

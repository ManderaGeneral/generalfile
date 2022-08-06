
from generalfile import *

from generalpackager import LocalModule


module = LocalModule("matplotlib")

print(module.path.get_parent_package())
print(module.path.get_parent_venv())

# print(Path().get_parent_package())
# print(Path("generalfile/optional_dependencies").get_parent_repo())




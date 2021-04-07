
from generalfile import Path
from generalfile.test.setup_workdir import setup_workdir



for path in Path().absolute().get_parents(-1):
    print(path)

# Path().absolute().get_parent().view(spawn=True, filt=lambda x: not x.name().startswith("."))


# path = "/foo/bar"
#
# try:
#     index = path.rindex("/")
# except ValueError:
#     index = 0
#
# print(path[:index + 1])

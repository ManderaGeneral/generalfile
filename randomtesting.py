
from generalfile import Path

from generalfile.test.setup_workdir import setup_workdir



# setup_workdir()
# Path("hello.txt").write("asdf")

# print(Path("hello.txt").seconds_since_modified())



# with Path("hello").lock():
#     with Path("hello").lock():
#         print(5)



a = open("test.txt", "x")
a.write("hello")

b = open("test.txt", "r")

print(b.read())

a.close()
b.close()

# TODO: Add locked_paths to Path cls, remove _is_locked_externally, remove owns_lock, remove *args for lock()
# TODO: Doesn't seem to able to remove dead locks

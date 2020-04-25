"""
Random testing
"""
import multiprocessing as mp

from generalfile import *


File.setWorkingDir("test/tests")
File.clearFolder("")

File.write("test.txt")

File.copy("", "aux")

# File.rename("test.txt", "aux")

# File.createFolder("aux")


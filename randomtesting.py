"""
Random local testing
"""

import pathlib
from generalfile import File, Path

# File.write("newfolder/test.txt", "foobar")  # Automatically creates new folder
# assert File.read("newfolder/test.txt") == "foobar"
# File.delete("newfolder")  # Delete entire folder

# assert File.getWorkingDir() == Path().getAbsolute()
# assert Path("C:/folder/test.txt").getPathWithoutFile() == "C:/folder"
# assert Path("folder/test.txt").setFilenamePure("foobar") == "folder/foobar.txt"


File.setWorkingDir("test/tests")
File.openFolder("")

File.write("hEllo/teSt.txt", overwrite=True)

print(File.exists("hEllo"))

# print(pathlib.Path(Path("hello").getAbsolute()).resolve(strict=True))




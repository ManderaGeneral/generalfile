"""
Random local testing
"""

from generalfile import File, Path


File.write("newfolder/test.txt", "foobar")  # Automatically creates new folder
assert File.read("newfolder/test.txt") == "foobar"
File.delete("newfolder")  # Delete entire folder

assert File.getWorkingDir() == Path().getAbsolute()
assert Path("C:/folder/test.txt").getPathWithoutFile() == "C:/folder"
assert Path("folder/test.txt").setFilenamePure("foobar") == "folder/foobar.txt"

File.openFolder("")  # Opens current working directory

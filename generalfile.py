"""
Module by Mandera
Generalfile is made for windows path and file management.
It's relatively easily extended with any filetype by inheriting the File baseclass.

TODO: Try another approach for backup by using "x" mode and not copying
done
TODO: Remove backup
TODO: Docstring and tests for rename
TODO: Catch if trying to use "CON" for example, either use "x" mode or check if exists
TODO: classfiletsv
TODO: Change suffix, "suffix" is apparently already used for filetype
TODO: Multiple dots are actually allowed
"""

from base.classfile import File, Path, PathList
from extensions.classfiletsv import FileTSV

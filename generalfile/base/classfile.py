"""
Base component of generalfile
"""
from send2trash import send2trash

import os

import shutil

import json

import pathlib

from generallibrary import Timer, VerInfo

from generalfile.extensions.classfiletsv import FileTSV
from generalfile.base.errors import *


class File(FileTSV):
    """
    File class exists so that FileTSV for example can inherit it.
    Method parameter 'path' takes a Path or a Str, Str is converted to Path.
    """
    caseSensitive = VerInfo().caseSensitive
    timeoutSeconds = 12
    deadLockSeconds = 3
    def __init__(self):
        raise UserWarning("No need to instantiate File, all methods are static or classmethods")

    @staticmethod
    def toPath(path, requireFiletype=None, requireExists=None):
        """
        Makes sure we're using Path class.
        Has built-in parameters to scrub.
        Uses Path.toPath() but it also has extra functionality to check whether path exists.

        :param str path: Resemble a filepath or folderpath
        :param requireFiletype: True, False or filetype ("txt" or "tsv")
        :param bool requireExists: Require file or folder to exist or not
        :return: Same Path or a new Path if a string was given
        :raises AttributeError: if requireFiletype is True and it's not a file and vice versa
        :raises TypeError: if requireFiletype is a specified filetype and doesn't match filetype
        :raises FileNotFoundError: if requireExists is True and file doesn't exist
        :raises FileExistsError: if requireExists is False and file exists
        """
        path = Path.toPath(path, requireFiletype)

        if requireExists is not None:
            exists = File.exists(path)
            if exists and not requireExists:
                raise FileExistsError("Path exists", path)
            if requireExists and not exists:
                raise FileNotFoundError("Path doesn't exist", path)
        return path

    @staticmethod
    def exists(path):
        """
        Works for both file and folder.

        :param str path: Resemble a filepath or folderpath
        :return: Whether file or folder exists or not
        :rtype: bool
        :raises PermissionError: Resolve can raise this
        """
        path = Path.toPath(path)
        path = File.getAbsolutePath(path)
        exists = False

        pathList = File.getPaths(path, includeBaseFolder=True)
        for foundPath in pathList:
            if foundPath == path:
                exists = True
            elif foundPath.lower() == path.lower():
                raise CaseSensitivityError(f"Same path with differing case not allowed: '{path}'")

        return exists

        # try:
        #     resolved = Path(str(pathlib.Path(path).resolve(strict=True)))  # Returns path with correct cases
        # except FileNotFoundError:
        #     return False
        # except PermissionError:
        #     return True
        #
        # if path == resolved:
        #     return True
        # elif not File.caseSensitive:
        #     raise CaseSensitivityError(f"Same path with differing case not allowed: '{path}'")
        #
        # return False

    @staticmethod
    def getWorkingDir():
        """
        :returns: Current working directory as absolute Path
        :raises FileNotFoundError: If doesn't exist
        """
        path = Path(os.getcwd())
        if not File.resolve(path):
            raise FileNotFoundError(f"Working dir {path} doesn't exist.")
        return path

    @staticmethod
    def setWorkingDir(path):
        """
        Sets new working directory, if a relative path is given then current working directory will be taken into account.

        :param str path: Path to folder
        :return: Absolute Path to new working directory
        """
        path = File.toPath(path, requireFiletype=False)
        path = File.getAbsolutePath(path)
        File.createFolder(path)
        os.chdir(path)
        return path

    @staticmethod
    def getAbsolutePath(path, basePath=None):
        """
        Gets absolute path based on absolute basePath unless path already is absolute.

        :param str path: Generic Path to be converted.
        :param str basePath: Optional base Path to a folder. Is converted to absolute using current work dir if it's relative.
        :return: Absolute Path
        """
        path = File.toPath(path)
        if path.isAbsolute:
            return path

        if basePath is None:
            basePath = File.getWorkingDir()
        else:
            basePath = File.toPath(basePath, requireFiletype=False)
            basePath = File.getAbsolutePath(basePath)
        return basePath.addPath(path)

    @staticmethod
    def getRelativePath(path, basePath=None):
        """
        Gets relative path based on basePath.
        If basePath is None then current working dir will be used.

        :param str path: Generic Path to be converted
        :param str basePath: Optional base Path to a folder. Is converted to absolute using current work dir if it's relative.
        :return: Relative Path
        :raises AttributeError: If basePath isn't a part of given Path
        """
        path = File.toPath(path)
        path = File.getAbsolutePath(path)

        if basePath is None:
            basePath = File.getWorkingDir()
        else:
            basePath = File.toPath(basePath, requireFiletype=False)
            basePath = File.getAbsolutePath(basePath)

        relativePath = path.removeFromStart(basePath)
        if relativePath.isAbsolute:
            raise AttributeError("Working directory '{}' is not part of path '{}' so we cannot get the relative path".format(File.getWorkingDir(), path))
        return relativePath

    @staticmethod
    def sameDestination(path1, path2):
        """
        Detects if two paths point to same folder or file based on current working directory by converting to absolute paths.
        Compares identifiers instead of strings directly, to ignore case.

        :param str path1: Generic Path
        :param str path2: Generic Path
        :return: Whether paths point to same destination or not.
        """
        path1 = File.toPath(path1)
        path2 = File.toPath(path2)

        path1 = File.getAbsolutePath(path1)
        path2 = File.getAbsolutePath(path2)

        return Path.identifier(path1) == Path.identifier(path2)

    @staticmethod
    def _read_txt(textIO):
        """
        Reads txt file from IO stream as JSON.
        This method is included in default File because they're needed for backup.

        :param io.TextIO textIO: From "with open(Path) as textIO"
        :return: serializable object or None
        """
        try:
            read = textIO.read()
        except:
            return None
        else:
            if read == "":
                return None
            return json.loads(read)

    @staticmethod
    def _write_txt(textIO, serializable):
        """
        Writes to txt file IO stream with JSON.
        This method is part of default File because they're needed for backup.

        :param io.TextIO textIO: From "with open(Path) as textIO"
        :param serializable: Any serializable object that json can use
        :return: json string (json.dumps)
        """
        jsonDumps = json.dumps(serializable)
        try:
            textIO.write(jsonDumps)
        except:
            return None
        else:
            if jsonDumps == "" or serializable is None:
                return None
            return jsonDumps

    @classmethod
    def read(cls, path, default=None, **kwargs):
        """
        Dynamic function that can read any document if methods exist for that filetype

        Generic read method:
            Only used dynamically by this method.

            Suffix has to match a filetype.

            Method has to take path as parameter and return a useful object for that filetype.

        txt:
            Takes: None

            Returns: Serializable object.

        tsv:
            Takes: (header: bool, column: bool) - Whether these index exists in file or not. Defaults to False.

            Returns: Pandas DataFrame

        :param str path: Path or Str
        :param default: What is returned as backup if reading fails or file doesn't exist
        :return: Useful object for that filetype (Dynamic)
        :raises EnvironmentError: if read method is missing for that filetype
        """
        path = File.toPath(path, requireFiletype=True)
        exists = File.exists(path)

        readMethod = getattr(cls, "_read_{}".format(path.filetype), None)
        if readMethod is None:
            raise EnvironmentError("Missing read method for filetype {}".format(path.filetype))
        if not exists:
            return default

        with open(path, "r") as textIO:
            read = readMethod(textIO, **kwargs)
        return default if read is None else read

    @classmethod
    def write(cls, path, writeObj=None, overwrite=False, debug=False, **kwargs):
        """
        Dynamic function that can write to any document if methods exist for that filetype.

        Can only lock and backup if file exists.

        Generic write method:
            Only used dynamically by this method.

            Suffix has to match a filetype.

            Method has to take path and useful object as parameter, return object is optional

        txt:
            Takes: Serializable object.

            Returns: Text string that is written to txt file.

        tsv:
            Takes: Pandas DataFrame

            Returns: (header: bool, column: bool) - Whether these index exists in file or not.

        :param bool overwrite: Set to False if overwriting shouldn't be allowed
        :param str path: Path or Str
        :param writeObj: A useful object that the dynamic write method can use
        :return: Whatever the write method returns
        :raises EnvironmentError: if write method is missing for that filetype
        :raises FileExistsError: if overwriting when overwrite is set to False
        """
        path = File.toPath(path, requireFiletype=True)
        exists = File.exists(path)

        writeMethod = getattr(cls, "_write_{}".format(path.filetype), None)
        if writeMethod is None:
            raise EnvironmentError("Missing write method for filetype {}".format(path.filetype))
        if exists and not overwrite:
            raise FileExistsError("Tried to overwrite {} when overwrite was False".format(path))

        if not exists:
            File.createFolder(path)

        pathNew = path.setSuffix("NEW")
        pathLock = path.setSuffix("LOCK")
        timer = Timer()

        while True:
            try:
                with open(pathLock, "x") as lockIO:
                    with open(pathNew, "w") as textIO:
                        writeReturn = writeMethod(textIO, writeObj, **kwargs)
                    File.delete(path)
                    File.rename(pathNew, path.filenamePure)
                    lockIO.close()
                    File.delete(pathLock)
            except FileExistsError:
                # PermissionError would have triggered if we couldn't delete lock
                try:
                    File.delete(pathLock)
                except PermissionError:
                    pass
            except (PermissionError, FileNotFoundError):
                pass
            else:
                break
            if timer.seconds() > File.timeoutSeconds:
                raise TimeoutError(f"Couldn't open {pathLock} for writing")
        if debug:
            print(timer.seconds(), File.timeoutSeconds)
        return writeReturn

    @staticmethod
    def rename(path, name):
        """
        Rename a file or folder. Cannot change filetype.

        :param str path: Generic path to folder or file that exists.
        :param name: New name of folder or file.
        :return: None
        :raises EnvironmentError: If new path exists
        :raises FileExistsError: Probably contains an invalid name such as CON, PRN, NUL or AUX or if used invalid name or exists
        """
        path = File.toPath(path, requireExists=True)
        if path.isFile:
            newPath = path.setFilenamePure(name).setSuffix(None)
        else:
            newPath = path.getParent().addPath(name)
        if File.exists(newPath):
            raise FileExistsError(f"New path {newPath} exists already")
        try:
            os.rename(path, newPath)
        except OSError:  # If dst exists and on POSIX.
            raise FileExistsError

    @staticmethod
    def copy(path, destPath, overwrite=False):
        """
        Copy and paste a file to file, file to folder or folder to folder.
        Creates new folders if needed.
        When copying folder it excludes the parent folder, simply add the folder name to the end of target Path if that's desired.

        :param str path: Path or Str
        :param str destPath: Path to folder or file
        :param bool overwrite: Allow overwriting or not
        :return: None
        :raises RecursionError: If paths are identical
        :raises FileExistsError: If trying to overwrite when not allowed or if used invalid name
        :raises AttributeError: If filetypes don't match
        :raises NotADirectoryError: If trying to copy folder to file
        """
        path = File.toPath(path, requireExists=True)
        path = File.getAbsolutePath(path)
        destPath = File.toPath(destPath)
        destPath = File.getAbsolutePath(destPath)

        if File.sameDestination(path, destPath):
            raise RecursionError("Identical paths")

        if path.isFile:
            if destPath.isFile:
                if path.filetype != destPath.filetype:
                    raise AttributeError("Filetypes don't match")
            elif destPath.isFolder:
                destPath = destPath.addPath(path.filenameFull)
            if File.exists(destPath):
                if not overwrite:
                    raise FileExistsError("Not allowed to overwrite")

            File.createFolder(destPath)
            try:
                shutil.copy(path, destPath, follow_symlinks=False)
            except FileNotFoundError:
                raise FileExistsError(f"{destPath} probably contains an invalid name such as CON, PRN, NUL or AUX")

        elif path.isFolder and destPath.isFolder:
            filePathList = File.getPaths(path, maxDepth=0).getFiles()
            relativePaths = filePathList.getRelative(path)
            absoluteDestPaths = relativePaths.getAbsolute(destPath)
            if not overwrite and any(absoluteDestPaths.exists()):
                raise FileExistsError("Atleast one file exists and not allowed to overwrite")

            for path1, path2 in zip(filePathList, absoluteDestPaths):
                File.copy(path=path1, destPath=path2, overwrite=overwrite)
        else:
            raise NotADirectoryError("Cannot copy folder to file")

    @staticmethod
    def createFolder(path):
        """
        Create folder(s) for path.
        If a filepath is given then the filename is ignored.

        :param str path: Path or Str
        :return: Whether any folders were created or not
        :raises FileExistsError: If used invalid name
        """
        path = File.toPath(path)
        path = File.getAbsolutePath(path)
        path = path.getPathWithoutFile()

        if File.exists(path):
            return False

        try:
            pathlib.Path(path).mkdir(parents=True, exist_ok=True)
        except NotADirectoryError:
            raise FileExistsError(f"{path} probably contains an invalid name such as CON, PRN, NUL or AUX")

        return True

    @staticmethod
    def clearFolder(path, delete=False):
        """
        Make a target folder empty of everything.

        :param str path: Path or Str
        :param bool delete: Whether to delete files or put them in trash
        :return: Whether folder existed or not
        """
        path = File.toPath(path)
        path = File.getAbsolutePath(path)
        path = path.getPathWithoutFile()

        if not File.exists(path):
            return False
        if delete:
            File.delete(path)
        else:
            File.trash(path)
        File.createFolder(path)
        return True

    @staticmethod
    def trash(path):
        """
        Puts a file or folder in trashcan.

        :param str path: Path inside working directory
        :return: Whether path exists or not
        """
        path = File.toPath(path)
        path = File.getRelativePath(path)
        workingDir = File.getWorkingDir()

        if not File.exists(path):
            return False
        send2trash(path)

        # Reset working dir because send2trash can change it if it removed part of it
        if File.getWorkingDir() != workingDir:
            File.setWorkingDir(workingDir)
        return True

    @staticmethod
    def delete(path):
        """
        Deletes a file or folder, skipping trashcan

        :param str path: Path or Str
        :return: Whether path exists or not
        """
        path = File.toPath(path)
        if not File.exists(path):
            return False

        workingDir = File.getWorkingDir()

        timer = Timer()
        if path.isFile:
            while True:
                try:
                    os.remove(path)
                except FileNotFoundError:
                    return False
                # Try again since it might just be being used by another process
                except PermissionError:
                    pass
                else:
                    break
                if timer.seconds() > File.timeoutSeconds:
                    raise TimeoutError(f"Couldn't delete {path}")
        elif path.isFolder:
            shutil.rmtree(path, ignore_errors=True)

        # If path is working dir then shutil.rmtree() only clears folder.
        # if not File.sameDestination(path, workingDir):
        #     while File.exists(path):
        #         sleep(0.001)

        # Reset working dir
        try:
            File.getWorkingDir()
        except FileNotFoundError:
            File.setWorkingDir(workingDir)

        return True

    @staticmethod
    def resolve(path):
        """
        Return whether the path exists with case sensitivity.
        Doesn't raise CaseSensitivityError like `exists` does.
        """
        path = File.toPath(path)
        path = File.getAbsolutePath(path)

        timer = Timer()
        while True:
            try:
                resolved = pathlib.Path(path).resolve(strict=True)
            except FileNotFoundError:
                return False
            except PermissionError:
                pass
            else:
                break
            if timer.seconds() > File.timeoutSeconds:
                raise TimeoutError(f"Couldn't resolve {path}")

        return path == resolved

    @staticmethod
    def getPaths(path=None, maxDepth=1, includeBaseFolder=False):
        """
        Get a PathList obj from a path containing absolute Paths to both files and folders inside path.
        PathList extends list class with some convenient Path functionality.

        :param path: Path to folder. File is ignored. Default is Path("") which reads current work dir.
        :param maxDepth: Maximum folder depth, 0 means no limit.
        :param includeBaseFolder: Whether to include given path or not.
        :return: PathList containing every absolute Paths in folder.
        """
        if path is None:
            path = Path("")
        path = File.toPath(path)
        path = path.getPathWithoutFile()
        path = File.getAbsolutePath(path)

        # if not File.exists(path):
        #     return PathList()

        pathFoldersLen = len(path.foldersList)

        folderPathsToSearch = PathList(path)

        pathList = PathList()

        if not File.resolve(path):
            return pathList

        if includeBaseFolder:
            pathList.append(path)

        while folderPathsToSearch:
            try:
                subPaths = os.listdir(folderPathsToSearch[0])
            except FileNotFoundError:
                pass
            else:
                for subPath in subPaths:
                    absoluteSubPath = folderPathsToSearch[0].addPath(subPath)
                    pathList.append(absoluteSubPath)
                    if absoluteSubPath.isFile:
                        continue
                    if maxDepth and len(absoluteSubPath.foldersList) - pathFoldersLen >= maxDepth:
                        continue
                    folderPathsToSearch.append(absoluteSubPath)

            del folderPathsToSearch[0]
        return pathList

    @staticmethod
    def getTimeModified(path):
        """
        Gets time of when file (or folder?) was last modified

        :param str path: Path or Str
        :return: Time or None if file wasn't found
        """
        path = File.toPath(path)
        if not File.exists(path):
            return
        try:
            return os.path.getmtime(path)
        except FileNotFoundError:
            return
        # except PermissionError:

    @staticmethod
    def getTimeCreated(path):
        """
        Gets datetime of when file (or folder?) was created.
        Can be innacurate it seems when re-creating files.

        :param str path: Path or Str
        :return: Datetime or None
        """
        path = File.toPath(path)
        if not File.exists(path):
            return
        try:
            return os.path.getctime(path)
        except FileNotFoundError:
            return

    @staticmethod
    def openFolder(path):
        """
        Open file explorer on given path, files are ignored

        :param str path: Generic path that exists
        """
        path = File.toPath(path, requireExists=True).getPathWithoutFile()
        os.startfile(path)



from generalfile.base.classpath import Path
from generalfile.base.classpathlist import PathList

"""
Extension for File to handle xxx files
"""
from base.classfile import File

class FileXXX(File):
    """
    Extension for File to handle xxx files
    """
    @staticmethod
    def _write_xxx(textIO, obj):
        path = File.toPath(textIO.name)
        textIO.write(str(obj))
        return obj

    @staticmethod
    def _read_xxx(textIO):
        return textIO.read()

# Replace xxx with filetype, has to match





class FileTSV(File):
    def scrubDictOfDicts(self, dictOfDicts, indexName):
        """
        dictOfDicts can be singular dict also
        """
        if isinstance(dictOfDicts, dict):
            if isinstance(lib.dictFirstValue(dictOfDicts), dict):
                return dictOfDicts
            else:
                return {dictOfDicts[indexName]: dictOfDicts}

        print(dictOfDicts)
        lib.error("dictOfDicts failed scrubbing, printed above")

    def tsvWrite(self, filepath, dictOfDicts, indexName):
        dictOfDicts = self.scrubDictOfDicts(dictOfDicts, indexName)
        filepath = self.yesTsv(filepath)
        self.createFolderPath(filepath)

        with open(filepath, 'w') as tsvfile:
            writer = csv.writer(tsvfile, delimiter = "\t", lineterminator = "\n")
            writer.writerow(list(lib.dictFirstValue(dictOfDicts, iterate = True).keys()))
            for index, subDict in dictOfDicts.items():
                writer.writerow(list(subDict.values()))
        return dictOfDicts

    def tsvAppend(self, filepath, dictOfDicts, indexName):
        """
        Write instead if file doesn't exist
        """
        filepath = self.yesTsv(filepath)

        if not self.exists(filepath):
            return self.tsvWrite(filepath, dictOfDicts, indexName)

        dictOfDicts = self.scrubDictOfDicts(dictOfDicts, indexName)

        with open(filepath, 'a') as tsvfile:
            writer = csv.writer(tsvfile, delimiter = "\t", lineterminator = "\n")
            for index, subDict in dictOfDicts.items():
                writer.writerow(list(subDict.values()))

        return dictOfDicts

    def tsvRowToDict(self, row):
        return {k: lib.strToDynamicType(v) for k, v in row.items()}

    def tsvRead(self, filepath, indexName):
        """
        Manually add index to each created dict
        Check for indexName duplicates, if there are any just use the last one
        row in reader is an iterator I think, it contains all values as strings, first row will be the labels
        """
        filepath = self.yesTsv(filepath)
        if not self.exists(filepath):
            return {}

        with open(filepath, 'r') as tsvfile:
            reader = csv.DictReader(tsvfile, delimiter = "\t")
            returnDict = {subDict[indexName]: subDict for subDict in map(self.tsvRowToDict, reader)}
            # returnDict = {subDict[indexName]: subDict for subDict in map(dict, reader)}  # Without casting, 3 times faster

        return returnDict

    def tsvUpdate(self, filepath, values, indexName):
        """
        See if row exists, insert new if it doesn't, update if it does
        Use pandas dataframe?
        """
        df = pd.read_csv(filepath)
        print(df.head(5))

    def yesTsv(self, filepath):
        # return "{}.tsv".format(self.noFiletypeEnding(filepath))
        return ""
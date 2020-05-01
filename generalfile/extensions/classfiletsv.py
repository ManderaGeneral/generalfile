"""
Extension for File to handle tsv files
"""
import csv
import pandas as pd
from generallibrary.types import typeChecker

class FileTSV:
    """
    Extension for File to handle tsv files
    """
    @classmethod
    def _write_tsv(cls, textIO, df):
        """

        :param generalfile.File cls: test
        :param textIO:
        :param pd.DataFrame df:
        :return:
        """
        typeChecker(df, pd.DataFrame)
        path = cls.toPath(textIO.name)
        df.to_csv(path, sep="\t", quoting=csv.QUOTE_NONNUMERIC)


    @classmethod
    def _read_tsv(cls, textIO):
        """
        Converts

        :param generalfile.File cls: test
        :param textIO:
        :rtype: pd.DataFrame
        """
        path = cls.toPath(textIO.name)
        df = pd.read_csv(path, sep="\t", index_col=0).convert_dtypes()
        return df

    # def tsvAppend(self, filepath, dictOfDicts, indexName):
    #     """
    #     Write instead if file doesn't exist
    #     """
    #     filepath = self.yesTsv(filepath)
    #
    #     if not self.exists(filepath):
    #         return self.tsvWrite(filepath, dictOfDicts, indexName)
    #
    #     dictOfDicts = self.scrubDictOfDicts(dictOfDicts, indexName)
    #
    #     with open(filepath, 'a') as tsvfile:
    #         writer = csv.writer(tsvfile, delimiter = "\t", lineterminator = "\n")
    #         for index, subDict in dictOfDicts.items():
    #             writer.writerow(list(subDict.values()))
    #
    #     return dictOfDicts:



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

        :param generalfile.File cls:
        :param textIO:
        :param pd.DataFrame df:
        :return:
        """
        typeChecker(df, pd.DataFrame)
        if not df.shape[0] or not df.shape[1]:
            raise AttributeError("DataFrame cannot be empty")

        if str(df.index[0]) == "0":
            withIndex = False
        else:
            withIndex = True

        path = cls.toPath(textIO.name)
        df.to_csv(path, sep="\t", index=False, header=False)


    @classmethod
    def _read_tsv(cls, textIO):
        """
        Converts

        :param generalfile.File cls:
        :param textIO:
        :rtype: pd.DataFrame
        """
        path = cls.toPath(textIO.name)
        # df = pd.read_csv(path, sep="\t").convert_dtypes()
        # df = pd.read_csv(path, sep="\t", index_col=False)
        df = pd.read_csv(path, sep="\t", index_col=0).convert_dtypes()
        return df

    @classmethod
    def tsvAppend(cls, path, obj):
        """

        :param generalfile.File cls:
        :param path:
        :param obj:
        """
        path = cls.toPath(path, requireFiletype="tsv", requireExists=True)

        with open(path, 'a') as tsvfile:
            writer = csv.writer(tsvfile, delimiter = "\t", lineterminator = "\n")
            writer.writerow(obj, )



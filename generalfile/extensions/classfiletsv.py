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

    @staticmethod
    def _indexIsNamed(index):
        """
        Simple version to see if a DataFrame index is named or not
        :param index: DataFrame's index (columns or index)
        """
        if str(index[0]) == "0" or str(index[0]) == "1":
            return False
        else:
            return True

    @classmethod
    def _write_tsv(cls, textIO, df):
        """
        Can write a bunch of different DataFrames to a TSV file.
        Doesn't support advanced pandas functionality.
        Should work with: Keys, Index and Transposed (8 combinations)
        If DataFrame has both keys and index then cell A1 becomes NaN

        :param generalfile.File cls: File inherits FileTSV
        :param textIO: Tsv file
        :param pd.DataFrame df: Generic df that's not empty
        """
        typeChecker(df, pd.DataFrame)
        if not df.shape[0] or not df.shape[1]:
            raise AttributeError("DataFrame cannot be empty")

        path = cls.toPath(textIO.name)
        useHeader = cls._indexIsNamed(df.columns)
        useIndex = cls._indexIsNamed(df.index)

        df.to_csv(path, sep="\t", header=useHeader, index=useIndex)

        return useHeader, useIndex


    @classmethod
    def _read_tsv_helper(cls, path, header, column):
        return pd.read_csv(path, sep="\t", header=header, index_col=column).convert_dtypes()

    @classmethod
    def _read_tsv(cls, textIO, header=False, column=False):
        """
        If any cell becomes NaN then the header and column parameters are overriden silently.

        Can read a bunch of different DataFrames to a TSV file.
        Doesn't support advanced pandas functionality.
        Should work with: Keys, Index, Transposed, Header, Column (32 combinations).
        DataFrame in file can have a NaN A1 cell.

        :param generalfile.File cls:
        :param textIO:
        :param bool header: Use headers or not, overriden if any top left cell is NaN
        :param bool column: Use columns or not, overriden if any top left cell is NaN
        :rtype: pd.DataFrame
        """

        path = cls.toPath(textIO.name)

        header = "infer" if header else None
        column = 0 if column else None

        df = cls._read_tsv_helper(path, header, column)

        # Get rid of empty cell (Happens if file was written with header=True, column=True)
        headerFalseColumnFalse = pd.isna(df.iat[0, 0])
        headerFalseColumnTrue = pd.isna(df.index[0])
        headerTrueColumnFalse = str(df.columns[0]).startswith("Unnamed: ")
        if headerFalseColumnFalse or headerFalseColumnTrue or headerTrueColumnFalse:
            header = "infer"
            column = 0
            df = cls._read_tsv_helper(path, header, column)
        else:
            # Get rid of name in index (Happens if file doesn't have an index and column=True)
            # Doesnt happen other way around for some reason, guess it's the internal order in pandas
            if df.index.name is not None:
                if header is None and column == 0:
                    df.index.rename(None, inplace=True)
                else:
                    header = None
                    column = None
                    df = cls._read_tsv_helper(path, header, column)

        if not cls._indexIsNamed(df.columns):
            df.columns = pd.RangeIndex(len(df.columns))
        if not cls._indexIsNamed(df.index):
            df.index = pd.RangeIndex(len(df.index))

        return df.convert_dtypes()

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



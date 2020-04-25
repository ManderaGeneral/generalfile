"""
Extension for File to handle tsv files
"""
from base.classfile import File

import csv
import pandas as pd
from generallibrary import typeChecker

class FileTSV(File):
    """
    Extension for File to handle tsv files
    """
    @staticmethod
    def _write_tsv(textIO, df):
        """

        :param textIO:
        :param pd.DataFrame df:
        :return:
        """
        typeChecker(df, pd.DataFrame)

        path = File.toPath(textIO.name)
        df.to_csv(path, sep="\t")

        # writer = csv.DictWriter(textIO, fieldnames=tuple(df.keys()), delimiter="\t", lineterminator="\n")
        # writer.writerows(df)

    @staticmethod
    def _read_tsv(textIO):
        path = File.toPath(textIO.name)
        df = pd.read_csv(path, sep="\t", index_col=0)
        return df

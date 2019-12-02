# pylint: disable=missing-docstring, invalid-name
import pandas as pd


class ExcelParser:

    def __init__(self, excel_file):
        self._xl = pd.ExcelFile(excel_file)
        self._prepods_list = self._xl.sheet_names

    def get_prepods_list(self):
        return self._prepods_list

    def get_prepod_df(self, prepod_name):
        if prepod_name not in self._prepods_list:
            raise Exception('No such prepod: {}'.format(prepod_name))
        return self._xl.parse(prepod_name, header=None)

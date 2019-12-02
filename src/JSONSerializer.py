# pylint: disable=missing-docstring, invalid-name
import json
from src.ExcelParser import ExcelParser
from src.Prepod import Prepod


class JSONSerializer:

    _xl = None
    _dates = []
    _date_dict = {}
    _prepods_dict = {}
    _prepods_list = []

    @staticmethod
    def serialize(excel_file):
        obj = JSONSerializer()

        obj._xl = ExcelParser(excel_file)
        obj._names_list = obj._xl.get_prepods_list()
        obj._prepods_dict = {}
        for name in obj._names_list:
            df = obj._xl.get_prepod_df(name)
            prepod = Prepod.df_parser(df)
            obj._prepods_dict[name] = prepod.get_pairs_dict()
            obj._dates += prepod.get_dates_list()

        for date in set(obj._dates):
            obj._date_dict[date] = {i: [] for i in range(1, 5)}

        for name in obj._names_list:
            for date in obj._prepods_dict[name]:
                for i, pair in enumerate(obj._prepods_dict[name][date]):
                    print(i, pair)
                    obj._date_dict[date][i+1].append(pair.to_list(name))
        return obj

    def dump(self, file):
        with open(file, 'w') as file:
            json.dump(self._prepods_dict, file)


if __name__ == '__main__':
    JSONSerializer.serialize(excel_file='../data.xlsx').dump('test.json')

# pylint: disable=missing-docstring, invalid-name
import json
from src.ExcelParser import ExcelParser
from src.Prepod import Prepod


class JSONSerializer:

    _xl_file = None
    _dates = []
    _date_dict = {}
    _prepods_pairs_dict = {}
    _names_list = []

    @staticmethod
    def serialize(excel_file):
        obj = JSONSerializer()

        obj._xl_file = ExcelParser(excel_file)
        obj._names_list = obj._xl_file.get_prepods_list()
        obj._prepods_pairs_dict = {}
        for prepod_name in obj._names_list:
            df = obj._xl_file.get_prepod_df(prepod_name)
            prepod = Prepod.df_parser(df)
            obj._prepods_pairs_dict[prepod_name] = prepod.get_pairs_dict()
            obj._dates += prepod.get_dates_list()

        for date in set(obj._dates):
            obj._date_dict[date] = {i: [] for i in range(1, 5)}

        for prepod_name in obj._names_list:
            for date in obj._prepods_pairs_dict[prepod_name]:
                for i, pair in enumerate(obj._prepods_pairs_dict[prepod_name][date]):
                    pair_list = pair.to_list(prepod_name)
                    obj._date_dict[date][i+1].append(pair_list) if pair_list else 0
        return obj

    def dump(self, file):
        with open(file, 'w') as file:
            json.dump(self._date_dict, file)

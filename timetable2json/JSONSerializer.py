# pylint: disable=missing-docstring, invalid-name, protected-access
import json
from timetable2json.ExcelParser import ExcelParser
from timetable2json.Prepod import Prepod


class JSONSerializer:

    _xl_file = None
    _dates = []
    _date_dict = {}
    _prepods_pairs_dict = {}
    _names_list = []

    @staticmethod
    def serialize(excel_file, log_file):
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

        with open(log_file, 'w') as logs:
            for prepod_name in obj._names_list:
                for date in obj._prepods_pairs_dict[prepod_name]:
                    for i, pair in enumerate(obj._prepods_pairs_dict[prepod_name][date]):
                        pair_list = pair.to_list(prepod_name)
                        if pair_list:
                            # logging the situation with 2 lessons during one pair
                            if pair.get_entry_value():
                                obj._date_dict[date][i+1].append(pair_list)
                            else:
                                logs.write('Skip %s\n' % pair.get_entry_value())
        return obj

    def dump(self, file, ensure_ascii):
        with open(file, 'w') as out:
            out.write(json.dumps(self._date_dict, indent=4, ensure_ascii=ensure_ascii))

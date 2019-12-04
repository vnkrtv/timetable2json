# pylint: disable=missing-docstring, bare-except, protected-access, invalid-name
import pandas as pd
from timetable2json.Lesson import Lesson


class Prepod:
    """
    Class representing the essence of a institute lecturer

    Fields:
    _df - pandas DataFrame from excel sheet list with lecturer's study pairs
    _dates - all dates from excel sheet list with lecturer's study pairs
    _pairs = dict with all lecturer's study pairs:
    {
        'date' [
            <Lesson_object>,
            ...
            ]
        'another_date': [ ... ],
        ...
    }
    """

    _df = pd.DataFrame()
    _dates = []
    _pairs = {}

    @staticmethod
    def df_parser(prepod_df):
        """
        Parses input pandas DataFrame from excel sheet list
        with lecturer's study pairs and return Prepod object
        :param prepod_df: pandas DataFrame (pd.DataFrame)
        :return: Prepod object (Prepod)
        """
        prepod = Prepod()
        prepod._df = prepod_df
        prepod._dates = []
        prepod._pairs = {}

        months = ['сентября', 'октября', 'ноября',
                  'декабря', 'января', 'февраля',
                  'марта', 'апреля', 'мая',
                  'июня', 'июля', 'августа']
        for col_num in prepod._df.columns:

            dates = []
            selected_rows = []
            rows_num = len(prepod._df.index) + 1

            for row_num, row in prepod._df.iterrows():
                cell = row[col_num]
                try:
                    if cell.split(' ')[1] in months:
                        dates.append(cell)
                        selected_rows.append(row_num + 1)
                except:
                    pass

            prepod._dates += dates
            selected_rows.append(rows_num)

            for i, date in enumerate(dates):
                pairs_df = prepod._df[col_num][selected_rows[i]:selected_rows[i + 1] - 1]
                pairs = pairs_df.replace(pd.np.nan, '')
                prepod._pairs[date] = [Lesson.cell_parser(pair) for pair in pairs]

        for date in prepod._pairs:
            prepod._pairs[date] = Prepod.parse_pairs(prepod._pairs[date])
        return prepod

    @staticmethod
    def parse_pairs(lessons_list) -> list:
        """
        Get list of Lessons and brings it to a common format
        :param lessons_list: list of Lessons
        :return: list of Lessons
        """
        pairs = lessons_list[:]
        if len(pairs) == 5:
            pairs[2] = pairs[2] if pairs[2].get_entry_value() else pairs[3]
            pairs[3] = pairs[4]
            pairs = pairs[:-1]
        if len(pairs) > 5:
            pairs[2] = pairs[2] if pairs[2].get_entry_value() else pairs[3]
            pairs[3] = pairs[4] if pairs[4].get_entry_value() else pairs[5]
            pairs = pairs[:4]
        return pairs

    def get_pairs_dict(self) -> dict:
        """
        Return dict with all lecturer's study pairs:
        {
            'date' [
                <Lesson_object>,
                ...
                ]
            'another_date': [ ... ],
            ...
        }
        :return: dict with all lecturer's study pairs (dict)
        """
        return self._pairs

    def get_dates_list(self) -> list:
        """
        Return all dates from excel sheet list with lecturer's study pairs
        :return: list of dates (list)
        """
        return self._dates

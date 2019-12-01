# pylint: disable=missing-docstring, protected-access, invalid-name, broad-except
import pandas as pd
from Lesson import Lesson


class Prepod:

    _df = pd.DataFrame()
    _dates = []
    _pairs = {}

    @staticmethod
    def prepod_df_parser(prepod_df):
        prepod = Prepod()
        prepod._df = prepod_df

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
                except Exception:
                    pass

            prepod._dates += dates
            selected_rows.append(rows_num)

            for i, date in enumerate(dates):
                pairs_df = prepod._df[col_num][selected_rows[i]:selected_rows[i + 1] - 1]
                pairs = pairs_df.replace(pd.np.nan, '')
                prepod._pairs[date] = [Lesson.cell_parser(pair) for pair in pairs]

        for date in prepod._pairs:
            if len(prepod._pairs[date]) == 5:
                pairs = prepod._pairs[date]
                pairs[2] = pairs[2] if pairs[2].get_entry_value() else pairs[3]
                pairs[3] = pairs[4]
                prepod._pairs[date] = pairs[:-1]
            if len(prepod._pairs[date]) == 6:
                pairs = prepod._pairs[date]
                pairs[2] = pairs[2] if pairs[2].get_entry_value() else pairs[3]
                pairs[3] = pairs[4] if pairs[4].get_entry_value() else pairs[5]
                prepod._pairs[date] = pairs[:-2]
        return prepod

    def get_pairs_dict(self):
        return self._pairs

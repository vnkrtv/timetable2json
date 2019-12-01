from Lesson import Lesson, pd


class Prepod:

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
                entry = row[col_num]
                if isinstance(entry, str):
                    if entry.split(' ')[1] in months:
                        dates.append(entry)
                        selected_rows.append(row_num + 1)

            prepod._dates += dates
            selected_rows.append(rows_num)

            for i in range(len(dates)):
                date = dates[i]
                pairs_df = prepod._df[col_num][selected_rows[i]:selected_rows[i + 1] - 1]
                pairs = pairs_df.replace(pd.np.nan, '')
                Prepod._pairs[date] = [Lesson.cell_parser(pair) for pair in pairs]

        return Prepod

    def get_dates(self):
        return self._dates


import json

with open('file', 'r') as file:
    data = json.load(file)
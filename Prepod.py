from Lesson import Lesson, pd


class Prepod:

    _dates = []
    _pairs = {}

    def __init__(self, prepod_df):
        self._df = prepod_df

        months = ['сентября', 'октября', 'ноября',
                  'декабря', 'января', 'февраля',
                  'марта', 'апреля', 'мая',
                  'июня', 'июля', 'августа']
        for col_num in self._df.columns:

            dates = []
            selected_rows = []
            rows_num = len(self._df.index) + 1

            for row_num, row in self._df.iterrows():
                entry = row[col_num]
                try:
                    if entry.split(' ')[1] in months:
                        dates.append(entry)
                        selected_rows.append(row_num + 1)
                except:
                    pass

            self._dates += dates
            selected_rows.append(rows_num)

            for i in range(len(dates)):
                date = dates[i]
                pairs_df = self._df[col_num][selected_rows[i]:selected_rows[i + 1] - 1]
                pairs = pairs_df.replace(pd.np.nan, '')
                self._pairs[date] = [Lesson(pair) for pair in pairs]

    def get_dates(self):
        return self._dates

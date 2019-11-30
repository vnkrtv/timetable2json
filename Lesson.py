import pandas as pd
"""
Упр. инф. безоп.: (асс.) лекция-2.2
ауд. 136
гр. * 7353; 7354
"""
COMP_CLASSES = ['122', '103']

class Lesson:

    _name = ''
    _type = ''
    _entry_value = ''
    _num = ''
    _classroom = ''
    _in_comp_class = False
    _groups = []

    def __init__(self, pair_str):
        self._entry_value = pair_str

        if len(pair_str.split(':')) < 2:
            raise Exception('Incorrect cell format')
        elif len(pair_str.split(':')) > 2:
            return

        buf_list = pair_str.split('\n')
        self._name, buf = buf_list[0].split(': ')
        self._type, self._num = buf.split('-')
        self._classroom = buf_list[1].split(' ')[1]
        self._in_comp_class = self._classroom in COMP_CLASSES
        tmp = buf_list[2].split('гр. ')[1]
        self._groups = tmp.split('; ')

    def __str__(self):
        return self._entry_value

    def get_entry_value(self):
        return self._entry_value

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_lesson_num(self):
        return self._num

    def is_in_computer_class(self):
        return self._in_comp_class

    def get_classroom(self):
        return self._classroom

    def get_groups(self):
        return self._groups

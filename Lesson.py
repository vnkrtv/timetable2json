import pandas as pd


COMP_CLASSES = ['122', '103']


class Lesson(object):

    _name = ''
    _type = ''
    _entry_value = ''
    _num = ''
    _classroom = ''
    _in_comp_class = False
    _groups = []

    @staticmethod
    def cell_parser(pair_str):
        lesson = Lesson()
        lesson._entry_value = pair_str

        if len(pair_str.split(':')) < 2:
            raise ValueError('Incorrect cell format')
        elif len(pair_str.split(':')) > 2:
            return lesson

        buf_list = pair_str.split('\n')
        lesson._name, buf = buf_list[0].split(': ')
        lesson._type, lesson._num = buf.split('-')
        lesson._classroom = buf_list[1].split(' ')[1]
        lesson._in_comp_class = lesson._classroom in COMP_CLASSES
        tmp = buf_list[2].split('гр. ')[1]
        lesson._groups = tmp.split('; ')

        return lesson

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

# pylint: disable=missing-docstring, invalid-name, protected-access, line-too-long, logging-not-lazy
import logging


COMP_CLASSES = ['122', '103', '113', '124', '20_УНЦ', '17_УНЦ']


class Lesson:
    """
    Class representing the essence of a study pair
    """

    _name = ''
    _type = ''
    _entry_value = ''
    _num = ''
    _classroom = ''
    _in_comp_class = False
    _groups = []

    @staticmethod
    def cell_parser(pair_str):
        """
        Parses input cell value from excel table and return Lesson object
        :param pair_str: cell value from excel table (str)
        :return: Lesson object (Lesson)
        """
        lesson = Lesson()
        lesson._entry_value = pair_str

        if len(pair_str.split(':')) != 2:
            logger = logging.getLogger("cell_parser")
            logger.info("Skipped %s" % pair_str)
            return lesson

        lesson._name, buf = pair_str.split(':')
        buf = buf.split('-')
        buf_type, buf_num = buf[0], buf[1]
        lesson._type = buf_type.split('\n')[-1].split(' ')[-1]
        lesson._num = buf_num.split('\n')[0].split(' ')[0]

        buf_list = pair_str.split('\n')
        lesson._classroom = buf_list[-2].split(' ')[-1]
        lesson._in_comp_class = lesson._classroom in COMP_CLASSES

        buf = buf_list[-1].split('гр. ')[1]
        lesson._groups = buf.split('; ')

        return lesson

    def __eq__(self, other):
        return self._entry_value == other._entry_value if isinstance(other, Lesson) else False

    def to_list(self, prepod_name) -> list:
        """
        Represents a study pair as a list
        :param prepod_name: prepod_name (str)
        :return: list representation of study pair (list)
        """
        return [prepod_name, self._groups, self._classroom, self._in_comp_class] if self._entry_value else []

    def get_entry_value(self) -> str:
        return self._entry_value

    def get_name(self) -> str:
        return self._name

    def get_type(self) -> str:
        return self._type

    def get_lesson_num(self) -> str:
        return self._num

    def is_in_computer_class(self) -> bool:
        return self._in_comp_class

    def get_classroom(self) -> str:
        return self._classroom

    def get_groups(self) -> list:
        return self._groups

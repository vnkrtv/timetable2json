# pylint: disable=missing-docstring, line-too-long, invalid-name
import unittest
from timetable2json.Lesson import Lesson


class TestLesson(unittest.TestCase):

    init_values = ['Безопасность ОС: ПЗ-17\nауд. 122\nгр. 7333',
                   '2780: ПЗ-6\nауд. КВАНТ-КК\nгр. 2780.2',
                   'Упр. инф. безоп.: (асс.) лекция-2.2\nауд. 136\nгр. * 7353; 7354\n2813: ПЗ-6.2\nауд. 20_УНЦ\nгр. 2813.1']

    def test_entry_value(self):
        for init_value in self.init_values:
            lesson = Lesson.cell_parser(init_value)
            self.assertEqual(init_value, lesson.get_entry_value())

    def test_to_list(self):
        lists = [
            ['Prepod name', ['7333'], '122', True],
            ['Prepod name', ['2780.2'], 'КВАНТ-КК', False],
            ['Prepod name', [], '', False]
        ]
        for (l, init_value) in zip(lists, self.init_values):
            lesson = Lesson.cell_parser(init_value)
            self.assertEqual(l, lesson.to_list(prepod_name='Prepod name'))

    def test_types(self):
        types = ['ПЗ', 'ПЗ', '']
        for (tp, init_value) in zip(types, self.init_values):
            lesson = Lesson.cell_parser(init_value)
            self.assertEqual(tp, lesson.get_type())

    def test_names(self):
        names = ['Безопасность ОС', '2780', '']
        for (name, init_value) in zip(names, self.init_values):
            lesson = Lesson.cell_parser(init_value)
            self.assertEqual(name, lesson.get_name())

    def test_nums(self):
        nums = ['17', '6', '']
        for (num, init_value) in zip(nums, self.init_values):
            lesson = Lesson.cell_parser(init_value)
            self.assertEqual(num, lesson.get_lesson_num())

    def test_classrooms(self):
        classrooms = ['122', 'КВАНТ-КК', '']
        for (classroom, init_value) in zip(classrooms, self.init_values):
            lesson = Lesson.cell_parser(init_value)
            self.assertEqual(classroom, lesson.get_classroom())

    def test_comp_classes_flag(self):
        in_comp_classes = [True, False, False]
        for (flag, init_value) in zip(in_comp_classes, self.init_values):
            lesson = Lesson.cell_parser(init_value)
            self.assertEqual(flag, lesson.is_in_computer_class())

    def test_groups(self):
        groups = [['7333'], ['2780.2'], []]
        for (groups, init_value) in zip(groups, self.init_values):
            lesson = Lesson.cell_parser(init_value)
            self.assertEqual(groups, lesson.get_groups())

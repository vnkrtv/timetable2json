import unittest
from Lesson import Lesson
from Prepod import Prepod
from ExcelParser import ExcelParser


class TestLesson(unittest.TestCase):

    entry_values = ['Безопасность ОС: ПЗ-17\nауд. 122\nгр. 7333',
                    '2780: ПЗ-6\nауд. КВАНТ-КК\nгр. 2780.2',
                    'Упр. инф. безоп.: (асс.) лекция-2.2\nауд. 136\nгр. * 7353; 7354\n2813: ПЗ-6.2\nауд. 20_УНЦ\nгр. 2813.1']
    names = ['Безопасность ОС', '2780', '']
    types = ['ПЗ', 'ПЗ', '']
    nums = ['17', '6', '']
    classrooms = ['122', 'КВАНТ-КК', '']
    in_comp_classes = [True, False, False]
    groups = [['7333'], ['2780.2'], []]

    def test_entry_value(self):
        for entry_value in self.entry_values:
            lesson = Lesson(entry_value)
            self.assertEqual(entry_value, lesson.get_entry_value())

    def test_names(self):
        for (name, entry_value) in zip(self.names, self.entry_values):
            lesson = Lesson(entry_value)
            self.assertEqual(name, lesson.get_name())

    def test_nums(self):
        for (num, entry_value) in zip(self.nums, self.entry_values):
            lesson = Lesson(entry_value)
            self.assertEqual(num, lesson.get_lesson_num())

    def test_classrooms(self):
        for (classroom, entry_value) in zip(self.classrooms, self.entry_values):
            lesson = Lesson(entry_value)
            self.assertEqual(classroom, lesson.get_classroom())

    def test_comp_classes_flag(self):
        for (flag, entry_value) in zip(self.in_comp_classes, self.entry_values):
            lesson = Lesson(entry_value)
            self.assertEqual(flag, lesson.is_in_computer_class())

    def test_groups(self):
        for (groups, entry_value) in zip(self.groups, self.entry_values):
            lesson = Lesson(entry_value)
            self.assertEqual(groups, lesson.get_groups())


class TestPrepod(unittest.TestCase):
    pass


class TestExcelParser(unittest.TestCase):
    pass

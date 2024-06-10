""" Оберіть від 3 до 5 різних домашніх завдань
- перетворюєте їх у функції (якщо це потрібно)
- створіть в папці файл homeworks.py куди вставте ваші функції з дз
- та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
-- імпорт та самі тести помістіть в окремому файлі - test_homeworks09.py
Код закомітьте в гіт, надайте посилання.
На оцінку впливає як якість тестів так і розмір тестового покриття.
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""

import unittest
from homeworks import calculate_average, find_longest_word, reverse_string

class TestHomeworks(unittest.TestCase):

    def test_calculate_average(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3)
        self.assertEqual(calculate_average([10, 20, 30]), 20)
        self.assertEqual(calculate_average([]), 0)
        self.assertEqual(calculate_average([1]), 1)
        self.assertAlmostEqual(calculate_average([1, 2, 2, 3, 4, 4, 5]), 3)

    def test_find_longest_word(self):
        self.assertEqual(find_longest_word(["apple", "banana", "cherry"]), "banana")
        self.assertEqual(find_longest_word(["a", "abc", "ab"]), "abc")
        self.assertEqual(find_longest_word([]), "")
        self.assertEqual(find_longest_word([""]), "")
        self.assertEqual(find_longest_word(["same", "size", "test"]), "same")

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("racecar"), "racecar")


if __name__ == '__main__':
    unittest.main(verbosity=2)

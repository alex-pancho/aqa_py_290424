""" Оберіть від 3 до 5 різних домашніх завдань
- перетворюєте їх у функції (якщо це потрібно)
- створіть в папці файл homeworks.py куди вставте ваші функції з дз
- та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
-- імпорт та самі тести помістіть в окремому файлі - test_homeworks09.py
Код закомітьте в гіт, надайте посилання.
На оцінку впливає як якість тестів так і розмір тестового покриття.
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""
from lesson_09.homeworks import calculator
from unittest import TestCase, main


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('3-1'), 2)

    def test_multi(self):
        self.assertEqual(calculator('4*4'), 16)

    def test_divide(self):
        self.assertEqual(calculator('10/5'), 2.0)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('abracadabra')
        self.assertEqual('Выражение должно содержать хотя бы один знак (+-/*)', e.exception.args[0])

    def test_two_equal_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+3*10')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator('2.2+3.0')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator('a+b')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as e:
            calculator('10/0')
        self.assertEqual('Запрещено делить на 0', e.exception.args[0])


if __name__ == '__main__':
    main()

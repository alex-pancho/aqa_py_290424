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
import homeworks

class TestFunctions(unittest.TestCase):

    def test_square(self):
        black_sea_square = 436_402
        azov_sea_square = 37_800
        actual_result = homeworks.square(black_sea_square, azov_sea_square)
        expected_result = 474_202
        self.assertEqual(actual_result, expected_result, f"The sum of {black_sea_square} and {azov_sea_square} should be {expected_result}")

    def test_computer_price(self):
        monthly_price = 1179
        number_of_months = 18
        actual_result = homeworks.computer_price(monthly_price, number_of_months)
        expected_result = 21222
        self.assertEqual(actual_result, expected_result, f"The total computer price should be {expected_result}")

    def test_diff_between_two_sets(self):
        set_1 = {1, 2, 3, 4, 5}
        set_2 = {4, 6, 5, 10}
        actual_result = homeworks.diff_between_two_sets(set_1, set_2)
        expected_result = {1, 2, 3, 6, 10}
        self.assertEqual(actual_result, expected_result, f"The symmetric difference between {set_1} and {set_2} should be {expected_result}")

    def test_unique_values_from_list(self):
        small_list = [3, 1, 4, 5, 2, 5, 3]
        actual_result = homeworks.unique_values_from_list(small_list)
        expected_result = {1, 2, 3, 4, 5}
        self.assertEqual(actual_result, expected_result, f"The unique values from the list {small_list} should be {expected_result}")

if __name__ == "__main__":
    unittest.main(verbosity=2)



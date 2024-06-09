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

class Test(unittest.TestCase):
        
    def test_average_valid(self):
        list = [1, 2, 3, 4, 5]
        actual_result = homeworks.average_of(list)
        expected_result = 3
        self.assertEqual(actual_result, expected_result, f"Average {list} is not equal {expected_result}")

    def test_average_with_string(self):
        with self.assertRaises(TypeError):
            list = [1, 2, 3, 4, 5, '5']
            homeworks.average_of(list)

    def test_average_empty(self):
        with self.assertRaises(ValueError):
            homeworks.average_of([])

    def test_sum_positive_numbers(self):
        list = [1,2,3,4]
        actual_result = homeworks.sum_of(list)
        expected_result = 10
        self.assertEqual(actual_result, expected_result, f"Sum of {list} not equal {expected_result}")

    def test_sum_negative_numbers(self):
        list = [-1, -2, -3, -4]
        actual_result = homeworks.sum_of(list)
        expected_result = -10
        self.assertEqual(actual_result, expected_result, f"Sum of{list} is not equal{expected_result}")
    
    def test_sum_mixed_numbers(self):
        list = [1, -2, -3, 4]
        actual_result = homeworks.sum_of(list)
        expected_result = 0
        self.assertEqual(actual_result, expected_result, f"Sum of{list} is not equal{expected_result}")

    def test_sum_empty_list(self):
        list = []
        actual_result = homeworks.sum_of(list)
        expected_result = 0
        self.assertEqual(actual_result, expected_result, f"Sum of empty list is not equal {expected_result}")        

    def test_max_numbers_valid(self):
        list = [1, 2, 3, 4]
        actual_result = homeworks.find_max(list)
        expected_result = 4
        self.assertEqual(actual_result, expected_result, f"Max numbers of{list} is not equal {expected_result}")

    def test_max_numbers_if_not_numbers(self):
        with self.assertRaises(TypeError):
            list = [1, 2, 3, '4']
            homeworks.find_max(list)

    def test_max_numbers_with_single_number(self):
        list = [1]
        actual_result = homeworks.find_max(list)
        expected_result = 1
        self.assertEqual(actual_result, expected_result, f"Max numbers of {list} is not equal {expected_result}")
    
if __name__ == "__main__":
    unittest.main(verbosity= 2)



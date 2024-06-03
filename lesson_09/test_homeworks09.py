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

class home_w_09(unittest.TestCase):
    def test_01_my_func(self):
       small_list = [3, 1, 4, 5, 2, 5, 3]
       actual_result = homeworks.find_elements(small_list)
       expected_result = set(small_list)
       self.assertCountEqual(expected_result, [1, 2, 3, 4, 5])

    def test_02_my_func(self):
      small_list = [3, 1, 4, 5, 2, 5, 3]
      actual_result = homeworks.find_elements(small_list)
      expected_result = actual_result[1]
      self.assertCountEqual(expected_result, [2, 4])

    def test_03_my_func(self):
      small_list = [3, 1, 4, 5, 2, 5, 3]
      actual_result = homeworks.find_elements(small_list)
      expected_result = actual_result[2]
      self.assertCountEqual(expected_result, [1, 3, 5])

    def test_04_my_func(self):
       big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
       has_negative_numbers = homeworks.check_list_properties(big_list)
       self.assertTrue(has_negative_numbers, f"check_list_properties retuned True for {big_list}")
    
    def test_05_my_func(self):
       big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
       has_duplicates = homeworks.check_list_properties(big_list)
       self.assertTrue(has_duplicates, f"check_list_properties retuned False for {big_list}")


    def test_06_my_func(self):
       add_dict = {"a": 1, "b": 2, "c": 2, "d": 3, 'size': 12}
       max_keys = homeworks.find_max_min_keys(add_dict)[0]
       self.assertEqual(max_keys, ['size'], "The maximum key must be 'size'")

   # Перевірка для порожнього словника 

    def test_07_my_func(self):
       add_dict = {}
       max_keys = homeworks.find_max_min_keys(add_dict)[0]
       self.assertEqual(max_keys, None, "For an empty dictionary, the maximum key should be None")

    def test_08_my_func(self):
       add_dict = {"a": 1, "b": 2, "c": 2, "d": 3, 'size': 12}
       min_keys = homeworks.find_max_min_keys(add_dict)[1]
       self.assertEqual(min_keys, ['a'], "The minimum key must be 'a'")

    # Перевірка для порожнього словника 

    def test_09_my_func(self):
       add_dict = {}
       min_keys = homeworks.find_max_min_keys(add_dict)[1]
       self.assertEqual(min_keys, None, "For an empty dictionary, the minimum key must be None")

    
    def test_10_my_func(self):
        a = 8
        b = 8
        actual_result = homeworks.sum_2(a, b)
        expected_result = 16
        self.assertEqual(actual_result, expected_result, f"Sum numbers {a}+{b} is not equal {expected_result}")


   


if __name__ == "__main__":
    unittest.main(verbosity=2)



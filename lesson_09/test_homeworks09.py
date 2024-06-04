""" Оберіть від 3 до 5 різних домашніх завдань
- перетворюєте їх у функції (якщо це потрібно)
- створіть в папці файл homeworks.py куди вставте ваші функції з дз
- та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
-- імпорт та самі тести помістіть в окремому файлі - test_homeworks09.py
Код закомітьте в гіт, надайте посилання.
На оцінку впливає як якість тестів так і розмір тестового покриття.
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""
import homeworks
import unittest

class HomeworkTest(unittest.TestCase):

    def test_01_sum_two_numbers(self):
        a = 1
        b = 10
        actual_result = 11
        expected_result = homeworks.sum_numbers(a, b)
        self.assertEqual(actual_result, expected_result, f"{a} + {b} is not equal {expected_result}")

    def test_02_sum_two_negative_numbers(self):
        a = -1
        b = -10
        actual_result = -11
        expected_result = homeworks.sum_numbers(a, b)
        self.assertEqual(actual_result, expected_result, f"{a} + {b} is not equal {expected_result}")
    def test_03_avg_func(self):
        number_list = [12, 35, 44, 38]
        actual_result = homeworks.avg_list(number_list)
        expected_result = float(32.25)
        self.assertEqual(actual_result, expected_result, f"The arithmetic mean {actual_result} in the list {number_list} is not equal {expected_result}")


    def test_04_avg_func_with_negative_number(self):
        number_list = [-5, 5]
        actual_result = homeworks.avg_list(number_list)
        expected_result = 0
        self.assertEqual(actual_result, expected_result, f"The arithmetic mean {actual_result} in the list")

    def test_05_even_numbers(self):
        list_with_numbers = [0, 2, 4]
        actual_result = homeworks.find_list_of_squares(list_with_numbers)
        expected_result = [0, 4, 16]
        self.assertEqual(actual_result, expected_result, f"a list of squares of even numbers from a list {list_with_numbers} is not equal {expected_result}")


    def test_06_not_even_numbers(self):
        list_with_numbers = [1, 3]
        actual_result = homeworks.find_list_of_squares(list_with_numbers)
        expected_result = []
        self.assertEqual(actual_result, expected_result,
                         f"a list of squares of even numbers from a list {list_with_numbers} is not equal {expected_result}")

    def test_07_lists_length(self):
        list_with_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual_result = len(homeworks.find_list_of_squares(list_with_numbers))
        expected_result = len([i for i in list_with_numbers if i % 2 == 0])
        self.assertEqual(actual_result, expected_result,
                         f"a list of squares of even numbers from a list {list_with_numbers} is not equal {expected_result}")


    def test_08_longest_word(self):
        any_list = ["a", "ab", "abcd"]
        actual_result = homeworks.longest_word(any_list)
        expected_result = "abcd"
        self.assertEqual(actual_result, expected_result,
                         f"the longest word from a list {any_list} is not equal {expected_result}")


    def test_09_empty_string(self):
        any_list = ['']
        actual_result = homeworks.longest_word(any_list)
        expected_result = ''
        self.assertEqual(actual_result, expected_result,
                         f"the longest word from a list {any_list} is not equal {expected_result}")

    def test_10_exception(self):
        message = "lalala"
        actual_result = homeworks.find_sum_numbers3(message)
        expected_result = "Не можу це зробити!"
        self.assertEqual(actual_result, expected_result,
                         f"The message must be '{expected_result}', but get '{actual_result}'")


if __name__ == "__main__":
    unittest.main(verbosity=2)
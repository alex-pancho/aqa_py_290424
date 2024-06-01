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

class MyTest(unittest.TestCase):

    def test_01_calc_words_uppercase(self):
        test_string = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. \
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. \
        It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."
        actual_result = homeworks.calc_words_uppercase(test_string)
        expected_result = 5
        self.assertEqual(actual_result, expected_result, f"The expected amount of words starting with uppercase is {expected_result}")

    def test_02_calc_words_uppercase(self):
        test_string = ""
        actual_result = homeworks.calc_words_uppercase(test_string)
        expected_result = 0
        self.assertEqual(actual_result, expected_result, f"The expected amount of words starting with uppercase is {expected_result}")

# And here I actually found out that my function is not working correctly :)
    def test_03_clac_words_uppercase(self):
        test_string = "LOrem IpSum is simply dummy text of the printing and typesetting industry."
        actual_result = homeworks.calc_words_uppercase(test_string)
        expected_result = 2
        self.assertEqual(actual_result, expected_result, f"The expected amount of words starting with uppercase is {expected_result}")

    def test_01_longest_word(self):
        actual_result = homeworks.longest_word("table", "computer", "wall", "cup")
        expected_result = "computer"
        self.assertEqual(actual_result, expected_result, f"The expected longest word is {expected_result}")

    def test_02_longest_word(self):
        actual_result = homeworks.longest_word("table", "computer", "wall", "cup", "approach")
        expected_result = "computer"
        self.assertEqual(actual_result, expected_result, f"The expected longest word is {expected_result}")

    def test_03_longest_word(self):
        with self.assertRaises(TypeError):
            homeworks.longest_word(1, 2, 3, 4, 5)

    def test_01_find_substring(self):
        str1 = "It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."
        str2 = "has survived"
        actual_result = homeworks.find_substring(str1, str2)
        expected_result = 3
        self.assertEqual(actual_result, expected_result, f"The expected position of the substring is {expected_result}")

    def test_02_find_substring(self):
        str1 = "It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."
        str2 = "is done"
        actual_result = homeworks.find_substring(str1, str2)
        expected_result = -1
        self.assertEqual(actual_result, expected_result, f"The expected position of the substring is {expected_result}")

    def test_03_find_substring(self):
        str1 = "It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."
        str2 = ""
        actual_result = homeworks.find_substring(str1, str2)
        expected_result = -1
        self.assertEqual(actual_result, expected_result, f"The expected position of the substring is {expected_result}")

    def test_04_find_substring(self):
        str1 = ""
        str2 = "has survived"
        actual_result = homeworks.find_substring(str1, str2)
        expected_result = -1
        self.assertEqual(actual_result, expected_result, f"The expected position of the substring is {expected_result}")

    def test_01_has_duplicates(self):
        test_list = [1, 4, 4, 5, 8, 0]
        actual_result = homeworks.has_duplicates(test_list)
        self.assertTrue(actual_result, f"List doesn't have duplicates")

    def test_02_has_duplicates(self):
        test_list = [1, 3, 4, 5, 8, 0]
        actual_result = homeworks.has_duplicates(test_list)
        self.assertFalse(actual_result, "List has duplicates")

    def test_03_has_duplicates(self):
        test_list = []
        actual_result = homeworks.has_duplicates(test_list)
        self.assertFalse(actual_result, "List has duplicates")

if __name__ == "__main__":
    unittest.main(verbosity=2)
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


class TestSumTwoNumbers:
    def test_positive_numbers(self):
        assert homeworks.sum_two_numbers(1, 2) == 3
        assert homeworks.sum_two_numbers(10, 20) == 30

    def test_negative_numbers(self):
        assert homeworks.sum_two_numbers(-1, -2) == -3
        assert homeworks.sum_two_numbers(-10, -20) == -30

    def test_mixed_sign_numbers(self):
        assert homeworks.sum_two_numbers(1, -2) == -1
        assert homeworks.sum_two_numbers(-10, 20) == 10

    def test_zero(self):
        assert homeworks.sum_two_numbers(0, 0) == 0
        assert homeworks.sum_two_numbers(0, 5) == 5
        assert homeworks.sum_two_numbers(5, 0) == 5

    def test_float_numbers(self):
        assert homeworks.sum_two_numbers(1.5, 2.5) == 4.0
        assert homeworks.sum_two_numbers(-1.5, -2.5) == -4.0
        assert homeworks.sum_two_numbers(1.5, -2.5) == -1.0


class TestCalculatePagesNeeded:
    def test_no_photos(self):
        assert homeworks.calculate_pages_needed(0, 1) == 0

    def test_one_photo_per_page(self):
        assert homeworks.calculate_pages_needed(5, 1) == 5
        assert homeworks.calculate_pages_needed(10, 1) == 10

    def test_multiple_photos_per_page(self):
        assert homeworks.calculate_pages_needed(10, 2) == 5
        assert homeworks.calculate_pages_needed(10, 5) == 2
        assert homeworks.calculate_pages_needed(10, 10) == 1

    def test_not_exact_division(self):
        assert homeworks.calculate_pages_needed(7, 2) == 4
        assert homeworks.calculate_pages_needed(13, 5) == 3
        assert homeworks.calculate_pages_needed(25, 4) == 7

    def test_photos_per_page_more_than_total_photos(self):
        assert homeworks.calculate_pages_needed(5, 10) == 1


class TestHasDuplicates:
    def test_empty_list(self):
        assert homeworks.has_duplicates([]) is False

    def test_no_duplicates(self):
        assert homeworks.has_duplicates([1, 2, 3, 4, 5]) is False
        assert homeworks.has_duplicates(['a', 'b', 'c', 'd']) is False

    def test_with_duplicates(self):
        assert homeworks.has_duplicates([1, 2, 3, 2, 5]) is True
        assert homeworks.has_duplicates(['a', 'b', 'a', 'd']) is True

    def test_all_duplicates(self):
        assert homeworks.has_duplicates([1, 1, 1, 1]) is True
        assert homeworks.has_duplicates(['a', 'a', 'a']) is True

    def test_mixed_data_types(self):
        assert homeworks.has_duplicates([1, '1', 2, '2', 2]) is True
        assert homeworks.has_duplicates([1, '1', 2, '2']) is False

    def test_large_list(self):
        large_list = list(range(10000)) + [9999]
        assert homeworks.has_duplicates(large_list) is True


class TestUniqueElements:
    def test_empty_list(self):
        assert homeworks.unique_elements([]) == []

    def test_no_duplicates(self):
        assert sorted(homeworks.unique_elements([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
        assert sorted(homeworks.unique_elements(['a', 'b', 'c', 'd'])) == ['a', 'b', 'c', 'd']

    def test_with_duplicates(self):
        assert sorted(homeworks.unique_elements([1, 2, 3, 2, 5])) == [1, 2, 3, 5]
        assert sorted(homeworks.unique_elements(['a', 'b', 'a', 'd'])) == ['a', 'b', 'd']

    def test_all_duplicates(self):
        assert sorted(homeworks.unique_elements([1, 1, 1, 1])) == [1]
        assert sorted(homeworks.unique_elements(['a', 'a', 'a'])) == ['a']

    def test_large_list(self):
        large_list = list(range(10000)) + [9999]
        assert sorted(homeworks.unique_elements(large_list)) == list(range(10000))


class TestReverseString:
    def test_empty_string(self):
        assert homeworks.reverse_string('') == ''

    def test_single_character(self):
        assert homeworks.reverse_string('a') == 'a'
        assert homeworks.reverse_string('1') == '1'

    def test_palindrome(self):
        assert homeworks.reverse_string('madam') == 'madam'
        assert homeworks.reverse_string('racecar') == 'racecar'

    def test_regular_string(self):
        assert homeworks.reverse_string('hello') == 'olleh'
        assert homeworks.reverse_string('world') == 'dlrow'

    def test_string_with_spaces(self):
        assert homeworks.reverse_string('hello world') == 'dlrow olleh'
        assert homeworks.reverse_string(' a b c ') == ' c b a '

    def test_string_with_special_characters(self):
        assert homeworks.reverse_string('123!@#') == '#@!321'
        assert homeworks.reverse_string('a!b@c#') == '#c@b!a'

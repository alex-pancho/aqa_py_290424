import unittest
import math
import homeworks
import pytest

class MyTest(unittest.TestCase):

    def test_01_sum_of_digits_positive(self):
        a = 1
        b = 2
        actual_result = homeworks.sum_digits(a,b)
        expected_result = 3
        self.assertEqual(actual_result, expected_result, f'The expected sum of digits -> {expected_result}')

    def test_02_sum_negative_numbers(self):
        result = homeworks.sum_digits(-3, -7)
        self.assertEqual(result, -10)

    def test_03_sum_mixed_numbers(self):
        result = homeworks.sum_digits(8, -3)
        self.assertEqual(result, 5)

    def test_04_sum_zero(self):
        result = homeworks.sum_digits(0, 0)
        self.assertEqual(result, 0)

    def test_01_average_with_different_numbers(self):
        result = homeworks.average(1, 2, 3, 4, 5)
        self.assertEqual(result, 3.0)

    def test_02_average_empty_arguments(self):
        with self.assertRaises(ZeroDivisionError):
            homeworks.average()

    def test_03_average_single_number(self):
        result = homeworks.average(10)
        self.assertEqual(result, 10.0)

    def test_04_average_string_value(self):
        with self.assertRaises(TypeError):
            homeworks.average('test')

    def test_01_area_with_positive_radius(self):
        result = homeworks.calculate_circle_area(5)
        self.assertAlmostEqual(result, 3.14 * 25, places=2)

    def test_02_area_with_zero_radius(self):
        result = homeworks.calculate_circle_area(0)
        self.assertAlmostEqual(result, 0.0, places=2)

    def test_03_area_with_large_radius(self):
        result = homeworks.calculate_circle_area(100)
        self.assertAlmostEqual(result, 3.14 * 10000, places=2)

if __name__ == "__main__":
    unittest.main(verbosity=2)
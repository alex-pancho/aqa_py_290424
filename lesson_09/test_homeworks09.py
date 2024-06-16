import unittest

from homeworks import (
    check_alien_color, process_alien_colors, add_pizza_toppings,
    calculate_sum_of_digits, calculate_total_sum, sum_of_numbers_in_string,
    multiplication_table, sum_two_numbers, calculate_average, reverse_string
)

class TestHomeworks(unittest.TestCase):

    def test_check_alien_color(self):
        self.assertEqual(check_alien_color('green'), "Гравець щойно заробив 5 балів.")
        self.assertEqual(check_alien_color('red'), "Колір прибульця не зелений.")

    def test_process_alien_color(self):
        result = process_alien_colors(['green', 'yellow', 'red'])
        self.assertEqual(result,[
            "Гравець щойно заробив 5 балів.",
            "Гравець щойно заробив 10 балів.",
            "Гравець щойно заробив 15 балів."
        ])

    def test_add_pizza_topings(self):
        result = add_pizza_toppings(['cheese', 'pepperoni', 'quit', 'mushrooms'])
        self.assertEqual(result, [
            "Ви додали cheese до вашої піци.",
            "Ви додали pepperoni до вашої піци."
        ])

    def test_calculate_total_sum(self):
        self.assertEqual(calculate_sum_of_digits("12345"), 15)
        self.assertEqual(calculate_sum_of_digits("0000"), 0)
        self.assertEqual(calculate_sum_of_digits("11111"), 5)

    def test_sum_of_numbers_in_string(self):
            self.assertEqual(sum_of_numbers_in_string("1,2,3,4"), 10)
            self.assertEqual(sum_of_numbers_in_string("1,2,3,4,50"), 60)
            self.assertEqual(sum_of_numbers_in_string("qwerty1,2,3"), "Не можу це зробити!")

    def test_multiplication_table(self):
            result = multiplication_table(3)
            self.assertEqual(result, [
                "3x1=3", "3x2=6", "3x3=9", "3x4=12", "3x5=15",
                "3x6=18", "3x7=21", "3x8=24"
            ])

    def test_sum_two_numbers(self):
            self.assertEqual(sum_two_numbers(5, 3), 8)
            self.assertEqual(sum_two_numbers(10, 15), 25)

    def test_calculate_average(self):
            self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3)
            self.assertEqual(calculate_average([10, 20, 30, 40, 50]), 30)
            self.assertEqual(calculate_average([]), 0)

    def test_reverse_string(self):
            self.assertEqual(reverse_string("Hello, World!"), "!dlroW ,olleH")
            self.assertEqual(reverse_string("Python"), "nohtyP")
            self.assertEqual(reverse_string("12345"), "54321")

if __name__ == '__main__':
        unittest.main()



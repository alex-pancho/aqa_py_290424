
# Функція 1
def check_alien_color(alien_color):
    if alien_color == 'green':
        return "Гравець щойно заробив 5 балів."
    else:
        return "Колір прибульця не зелений."

# Функція 2
def process_alien_colors(alien_colors):
    results = []
    for alien_color in alien_colors:
        if alien_color == 'green':
            results.append("Гравець щойно заробив 5 балів.")
        elif alien_color == 'yellow':
            results.append("Гравець щойно заробив 10 балів.")
        elif alien_color == 'red':
            results.append("Гравець щойно заробив 15 балів.")
    return results

# Функція 3
def add_pizza_toppings(toppings):
    results = []
    for topping in toppings:
        if topping.lower() == 'quit':
            break
        else:
            results.append(f"Ви додали {topping} до вашої піци.")
    return results

# Функція 4
def calculate_sum_of_digits(number_str):
    sum_of_digits = 0
    for digit in number_str:
        sum_of_digits += int(digit)
    return sum_of_digits

# Функція 5
def calculate_total_sum(numbers):
    total_sum = 0
    for number in numbers:
        if number == 0:
            break
        total_sum += number
    return total_sum

# Функція 6
def sum_of_numbers_in_string(s):
    try:
        numbers = s.split(',')
        total_sum = sum(int(num) for num in numbers)
        return total_sum
    except ValueError:
        return "Не можу це зробити!"

# Функція 7
def multiplication_table(number):
    results = []
    multiplier = 1
    while True:
        result = number * multiplier
        if result > 25:
            break
        results.append(f"{number}x{multiplier}={result}")
        multiplier += 1
    return results

# Функція 8
def sum_two_numbers(a, b):
    return a + b

# Функція 9
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# Функція 10
def reverse_string(s):
    return s[::-1]
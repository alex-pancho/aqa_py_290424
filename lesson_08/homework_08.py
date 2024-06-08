

def sum_of_numbers_in_string(s):
    try:
        numbers = s.split(',')
        total_sum = sum(int(num) for num in numbers)
        return total_sum
    except ValueError:
        return "Не можу цу зробити"

strings = [
    "1,2,3,4",
    "1,2,3,4,50",
    "qwerty1,2,3"
]

for string in strings:
    result = sum_of_numbers_in_string(string)
    print(result)
def sum_numbers_in_string(s):
    numbers = s.split(',')
    total_sum = 0
    for num in numbers:
        total_sum += int(num)
    return total_sum

list_of_strings = [
    "1,2,3,4",
    "1,2,3,4,50",
    "qwerty1,2,3"
    
]
for s in list_of_strings:
    try:
        result = sum_numbers_in_string(s)
        print(result)
    except ValueError as e:
        print(f"It ia impossible,because: {e}")
string_array = [
    '1,2,9,12,41',
    '1,2,3,5,50,71',
    'qwerty1,2,3,5',
    '2,5,1,txt,124']
# string_array2 = ['1,2,3,4,5', 'q,1,2', 'qqq']
# string_array3 = ['15', '1,2,3,5', '1,2,3']

def sum_of_numbers_in_string(s):
    """Функція для обчислення суми всіх чисел у рядку, розділених комами.
Якщо рядок містить нечислові символи, функція повертає "Не можу це зробити!"."""
    elements = s.split(',')
    total = 0
    try:
        for element in elements:
            if element.strip().isdigit():
                total += int(element)
            else:
                raise ValueError('Non-numeric value encountered')
        return total
    except ValueError:
        return 'Не можу це зробити!'
def process_strings(string_array):
    """Функція для обробки масиву рядків, що містять числа, розділені комами.
    Для кожного рядка в масиві викликає функцію sum_of_numbers_in_string(s) для обчислення суми чисел."""
    results = []
    for s in string_array:
        results.append(sum_of_numbers_in_string(s))
    return results

print(process_strings(string_array))




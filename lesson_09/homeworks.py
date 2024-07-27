def sum_two_numbers(a, b):
    """Функція обчислює суму двох чисел."""
    return a + b


def calculate_pages_needed(total_photos, photos_per_page):
    """Функція обчислює кількість сторінок, необхідних для вклеювання фотографій."""
    return (total_photos + photos_per_page - 1) // photos_per_page


def has_duplicates(lst):
    """Функція перевіряє, чи є в списку дублікати."""
    return len(lst) != len(set(lst))


def unique_elements(lst):
    """Функція повертає унікальні елементи зі списку."""
    return list(set(lst))


def reverse_string(s):
    """Функція приймає рядок та повертає його у зворотному порядку."""
    return s[::-1]
""" Сюди підготовані ф-ції вставити
"""
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_longest_word(words):
    if not words:
        return ""
    longest_word = max(words, key=len)
    return longest_word

def reverse_string(s):
    return s[::-1]
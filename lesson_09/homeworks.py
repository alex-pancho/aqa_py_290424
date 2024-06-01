""" Сюди підготовані ф-ції вставити
"""

def calc_words_uppercase(string_to_count_in):
    """Calculates the amount of words starting with the uppercase letter."""
    uppercase_letters_amount = 0
    for i in string_to_count_in:
        if i.isupper():
            uppercase_letters_amount = uppercase_letters_amount + 1

    return uppercase_letters_amount

def longest_word(*args):
    max_length = 0
    max_length_word = ""
    for arg in args:
        word_length = len(arg)
        if word_length > max_length:
            max_length = word_length
            max_length_word = arg

    return max_length_word

def find_substring(str1, str2):
    for i in range(0, len(str1)):
        for j in range(0, len(str2)):
            if i + j > len(str1) or str1[i + j] != str2[j]:
                break
            elif j == len(str2) - 1:
                return i

    return -1

def has_duplicates(list_to_check):
    """Returns True if list has duplicates."""
    if len(list_to_check) == 0:
        return False

    list_to_check_set = set(list_to_check)
    return len(list_to_check) != len(list_to_check_set)

""" Сюди підготовані ф-ції вставити
"""
def find_elements(lst):
    unique_elements = set(lst)
    unique_even_elements = {x for x in unique_elements if x % 2 == 0}
    unique_odd_elements = {x for x in unique_elements if x % 2 != 0}
    return list(unique_elements), list(unique_even_elements), list(unique_odd_elements)

small_list = [3, 1, 4, 5, 2, 5, 3]

unique_elements, unique_even_elements, unique_odd_elements = find_elements(small_list)


def check_list_properties(lst):
    has_duplicates = len(lst) != len(set(lst))
    has_negative_numbers = any(x < 0 for x in lst)
    return has_duplicates, has_negative_numbers

big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]

has_duplicates, has_negative_numbers = check_list_properties(big_list)


def find_max_min_keys(dictionary):
  if not dictionary:
      return None, None  
  max_value = max(dictionary.values())
  min_value = min(dictionary.values())

  max_keys = [key for key, value in dictionary.items() if value == max_value]
  min_keys = [key for key, value in dictionary.items() if value == min_value]

  return max_keys, min_keys

add_dict = {"a": 1, "b": 2, "c": 2, "d": 3, 'size': 12}
max_keys, min_keys = find_max_min_keys(add_dict)



def sum_2(a, b):
    return a + b
result = sum_2(8, 8)


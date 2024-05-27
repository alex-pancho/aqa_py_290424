list_01 = ["2, 5, 7, 11",
"abab12, 11, 18, c",
"1, 12, 33, 14",
"abetka, 1",
"1, 2, 3, 4",
"2, 5, !, ^"]

def sum_of_elements(arg: str):
    """Calculates the sum of all numbers in the string. If string contains non number raises the exception."""
    numbers = arg.split(", ")
    temp_sum = 0
    for i in numbers:
        i = int(i)
        temp_sum = temp_sum + i

    return temp_sum

def process_list(args):
    """Prints the sum of numbers in elements of the list."""
    for i in args:
        try:
            print(sum_of_elements(i))
        except ValueError:
            print("Cannot be done")

process_list(list_01)

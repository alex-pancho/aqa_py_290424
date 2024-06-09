""" Сюди підготовані ф-ції вставити
"""
def average_of(numbers):
    if len(numbers) == 0:
        raise ValueError("Empty input cant be calculated")
    for i in numbers:
        if not type(i) is int:
            raise TypeError("Only int allowed")
    
    return sum(numbers)/len(numbers)

def sum_of(numbers):
    return sum(numbers)

def find_max(numbers):
    for i in numbers:
        if not type(i) is int:
            raise TypeError("Only int allowed")
    return max(numbers)


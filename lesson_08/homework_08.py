#Вирішення 1
number_list = ["1,2,3,4",
    "1,2,3,4,50",
    "qwerty1,2,3"]
def find_sum_numbers(some_list):
    for element in some_list:
        try:
            result = 0
            for i in element.split(','):
                result = result + int(i)
            print(result)
        except ValueError:
            print("Не можу це зробити!")

find_sum_numbers(number_list)

print('-----')
#Вирішення 2
def find_sum_numbers(some_list):
    for element in some_list:
        try:
            list_int = list(int(item) for item in element.split(','))
            print(sum(list_int))
        except ValueError:
            print("Не можу це зробити!")

find_sum_numbers(number_list)
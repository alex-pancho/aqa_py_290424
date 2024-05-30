#Вирішення 1
number_list = ["1,2,3,4",
    "1,2,3,4,50",
    "qwerty1,2,3"]
def find_sum_numbers1(some_list):
    for element in some_list:
        try:
            result = 0
            for i in element.split(','):
                result = result + int(i)
            print(result)
        except ValueError:
            print("Не можу це зробити!")

find_sum_numbers1(number_list)

# #Вирішення 2
print('-----')
def find_sum_numbers2(some_list):
    for element in some_list:
        try:
            list_int = list(int(item) for item in element.split(','))
            print(sum(list_int))
        except ValueError:
            print("Не можу це зробити!")

find_sum_numbers2(number_list)
#
# #Вирішення 3
print('______')
def find_sum_numbers3(some_string):
    try:
        return sum(list(int(item) for item in some_string.split(',')))
    except ValueError:
        return "Не можу це зробити!"

for element in number_list:
    print(find_sum_numbers3(element))


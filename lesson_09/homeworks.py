""" Сюди підготовані ф-ції вставити
"""
# function 1
def square(black_sea_square, azov_sea_square):
    return black_sea_square + azov_sea_square
black_sea_square = 436_402
azov_sea_square = 37_800
total_square = square(black_sea_square, azov_sea_square)
print(f"The Black Sea and the Sea of Azov together cover {total_square} km2")


# function 2
def computer_price(monthly_price, number_of_months):
    """counting total computer price based on monthly payment and the number of months"""
    return monthly_price * number_of_months
monthly_price = 1179
number_of_months = 18
total_price = computer_price(monthly_price, number_of_months)
print(f"The total computer price is {total_price} UAH")

# function 3
def diff_between_two_sets(set_1, set_2):
    return(set_1.symmetric_difference(set_2))
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
diff = diff_between_two_sets(set_1, set_2)
formatted_diff = ', '.join(map(str, diff))
print(f"Unique numbers between 2 sets: {formatted_diff}.")

# function 4
def unique_values_from_list(small_list):
    return (set(small_list))
small_list = [3, 1, 4, 5, 2, 5, 3]
unique_values_output = unique_values_from_list(small_list)
formatted_unique_values_output = ', '.join(map(str, unique_values_output))
print(f"Unique values from the small_list are: {formatted_unique_values_output}.")
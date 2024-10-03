# START
import random

array_list_95_105: list[int] = [x for x in range(95, 106)]
print(array_list_95_105)
array_list_even_number: list[int] = [x for x in range(10, 20 + 1) if x % 2 == 0]
print(array_list_even_number)
array_list_True_False: list[bool] = [random.choice([True, False]) for _ in range(5)]
print(array_list_True_False)
array_list_10_random_number: list[int] = [random.randint(1, 100) for _ in range(10)]
print(array_list_10_random_number)
array_list_big_then_50: list[int] = [num for num in array_list_10_random_number if num > 50]
print(array_list_big_then_50)
array_list_random_big_then_50: list[int] = [num for num in [random.randint(1, 100) for _ in range(10)] if num > 50]
print(array_list_random_big_then_50)
string: str = input("enter a string? ")
array_list_string_no_t_and_no_spaces: list[str] = [s for s in string if s != 't' and s != ' ']
print(array_list_string_no_t_and_no_spaces)
array_list_random_numbers = [random.randint(10, 99) for _ in range(10)]
print(array_list_random_numbers)
array_list_units_digits = [num % 10 for num in array_list_random_numbers]
print(array_list_units_digits)

# END

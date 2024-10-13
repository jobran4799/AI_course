# START
import random

bool_list = [random.choice([True, False]) for _ in range(3)]

all_true = all(bool_list)
print(f"All elements are True: {all_true}")

any_true = any(bool_list)
print(f"At least one element is True: {any_true}")

all_false = not any(bool_list)
print(f"All elements are False: {all_false}")

any_false = not all(bool_list)
print(f"At least one element is False: {any_false}")

num_list = [random.randint(-2, 2) for _ in range(5)]
print(f"Random number list: {num_list}")

all_non_zero = all(num != 0 for num in num_list)
print(f"All numbers are non-zero: {all_non_zero}")

any_non_zero = any(num != 0 for num in num_list)
print(f"At least one number is non-zero: {any_non_zero}")

all_zero = all(num == 0 for num in num_list)
print(f"All numbers are zero: {all_zero}")

any_zero = any(num == 0 for num in num_list)
print(f"At least one number is zero: {any_zero}")

# END

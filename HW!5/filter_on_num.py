# START

import random

numbers = [random.randint(1, 100) for _ in range(50)]
print("Original list:", numbers)

print("Numbers greater than 50:", list(filter(lambda x: x > 50, numbers)))

print("Numbers divisible by 7:", list(filter(lambda x: x % 7 == 0, numbers)))

print("Two-digit numbers:", list(filter(lambda x: 10 <= x <= 99, numbers)))

print("Numbers with same tens and ones digits:",
      list(filter(lambda x: 10 <= x <= 99 and (x // 10) == (x % 10), numbers)))

print("Numbers where sum of digits is 9:", list(filter(lambda x: sum(map(int, str(x))) == 9, numbers)))

average = sum(numbers) / len(numbers)
print("Numbers greater than average:", list(filter(lambda x: x > average, numbers)))

half_of_max = max(numbers) / 2
print("Numbers greater than half of the max:", list(filter(lambda x: x > half_of_max, numbers)))

# END

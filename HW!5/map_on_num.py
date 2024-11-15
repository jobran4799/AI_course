# START
import random

numbers = [random.randint(-50, 50) for _ in range(20)]
print("Original list:", numbers)

print("Cubed numbers:", list(map(lambda x: x ** 3, numbers)))

print("Units digits:", list(map(lambda x: abs(x) % 10, numbers)))

print("Numbers in Fahrenheit:", list(map(lambda x: x * 9 / 5 + 32, numbers)))

print("Positive/Negative labels:", list(map(lambda x: "positive" if x > 0 else "negative", numbers)))

# END

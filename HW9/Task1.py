# START
temperatures: list[float] = []

while True:
    temp: float = float(input("Enter a temperature : "))

    if temp == -999:
        break
    if -50 <= temp <= 50:
        temperatures.append(temp)

additional_temps = [18.5, 39.1, -20.0]
temperatures.extend(additional_temps)

# Difference between extend and + between lists?
# Extend modifies the original list in place, while + creates a new list combining both lists.


print(f"max temperature: {max(temperatures)}")
print(f"min temperature: {min(temperatures)}")


is_18_5_in_list = 18.5 in temperatures
print(f"Is 18.5 in the list? {is_18_5_in_list}")

count_minus_20 = temperatures.count(-20.0)
print(f"How many times -20.0 appears: {count_minus_20}")

average_temp = sum(temperatures) / len(temperatures)
print(f"Average temperature: {average_temp}")

for temp in temperatures:
    print(temp)


index_39_1 = temperatures.index(39.1)
print(f"Index of 39.1: {index_39_1}")

del temperatures[0]

temperatures = [temp for i, temp in enumerate(temperatures) if i % 2 != 0]


if 18.5 in temperatures:
    temperatures.remove(18.5)

last_temp = temperatures.pop()
print(f"Last temperature: {last_temp}")

sorted_temperatures = temperatures.copy()
sorted_temperatures.sort()
print(f"Sorted temperatures: {sorted_temperatures}")


reverse_sorted_temperatures = temperatures.copy()
reverse_sorted_temperatures.sort(reverse=True)
print(f"Reverse sorted temperatures: {reverse_sorted_temperatures}")


print(f"Final temperatures list: {temperatures}")

# END

# START
import random

cities = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]

print("Sorted by length:", sorted(cities, key=lambda city: len(city)))

print("Sorted by word count:", sorted(cities, key=lambda city: len(city.split())))

print("Sorted by last letter:", sorted(cities, key=lambda city: city[-1]))

print("Sorted by reversed name:", sorted(cities, key=lambda city: city[::-1]))

print("Sorted by 'a' count:", sorted(cities, key=lambda city: city.lower().count('a')))

cities_data = [
    ["Tokyo", 5760, "Asia"],
    ["New York", 5690, "North America"],
    ["Paris", 2050, "Europe"],
    ["London", 2240, "Europe"],
    ["Sydney", 8780, "Australia"],
    ["Dubai", 1300, "Asia"],
    ["Shanghai", 4920, "Asia"]
]

print("Sorted by distance:", sorted(cities_data, key=lambda city: city[1]))

print("Sorted by distance (descending):", sorted(cities_data, key=lambda city: city[1], reverse=True))

print("Sorted by continent:", sorted(cities_data, key=lambda city: city[2]))

print("Sorted by continent and distance:", sorted(cities_data, key=lambda city: (city[2], city[1])))

numbers = [random.randint(1, 100) for _ in range(50)]
print("Original list:", numbers)

print("Sorted in ascending order:", sorted(numbers))

average = sum(numbers) / len(numbers)
print("Sorted by distance from average:", sorted(numbers, key=lambda num: abs(num - average)))
# END

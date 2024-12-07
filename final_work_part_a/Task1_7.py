# START
for num in range(12, 25):
    print(num, end=" ")
print()
for num in range(7, 32):
    if num % 2 != 0:
        print(num, end=" ")
print()
for num in range(10, -21, -1):
    if num % 2 == 0:
        print(num, end=" ")
print()
for num in range(1, 46):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz", end=" ")
    elif num % 3 == 0:
        print("Fizz", end=" ")
    elif num % 5 == 0:
        print("Buzz", end=" ")
print()


def calculate_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total



students = [
    {"id": 1, "first_name": "John", "last_name": "Doe", "age": 20, "country": "USA", "city": "New York"},
    {"id": 2, "first_name": "Jane", "last_name": "Smith", "age": 25, "country": "UK", "city": "London"}
]


# 1. Function to delete a property
def delete_property(students, prop_to_delete):
    for student in students:
        if prop_to_delete in student:
            del student[prop_to_delete]


# 2. Function to print each property
def print_properties(students):
    for student in students:
        for key, value in student.items():
            print(f"{key}: {value}")
        print("---")


# 3. Function to sort by age
def sort_by_age(students):
    return sorted(students, key=lambda x: x["age"], reverse=True)


our_pets = [
    {"animal_type": "cat", "names": ["Meowzer", "Fluffy", "Kit-Cat"]},
    {"animal_type": "dog", "names": ["Spot", "Bowser", "Frankie"]}
]


# 1. Print only animal type "cat"
def print_cats(pets):
    for pet in pets:
        if pet["animal_type"] == "cat":
            print(pet)


# 2. Print names of a specific animal type
def print_animal_names(pets, animal_type):
    for pet in pets:
        if pet["animal_type"] == animal_type:
            print(pet["names"])


# 3. Add a new name to all "names" arrays if not already present
def add_animal_name(pets, name_to_add):
    for pet in pets:
        if name_to_add not in pet["names"]:
            pet["names"].append(name_to_add)



# END

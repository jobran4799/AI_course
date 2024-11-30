# START

tuple_99: tuple[int] = (99,)

tuple_3_num: tuple[int, int, int] = 77, 88, 99


def get_tuple_length(tup):
    return len(tup)


def concatenate_tuples(tup1, tup2):
    return tup1 + tup2


def common_elements(tup1, tup2):
    return tuple(set(tup1) & set(tup2))


def unique_elements(tup1, tup2):
    return tuple(set(tup1) ^ set(tup2))


def get_element_at_index(tup, index):
    return tup[index] if 0 <= index < len(tup) else None


def reverse_tuple(tup):
    return tup[::-1]


def repeat_tuple(tup, n):
    return tup * n


def remove_number(tup, num):
    return tuple(item for item in tup if item != num)


def remove_duplicates(tup):
    lst: list[int] = []
    for item in tup:
        if not item in lst:
            lst.append(item)
    return tuple(lst) 


def get_indices_of_number(tup, num):
    return tuple(index for index, value in enumerate(tup) if value == num)


def collect_names_and_grades():
    names = []
    while True:
        name = input("Enter a name (or 'done' to finish): ")
        if name.lower() == "done":
            break
        names.append(name)

    grades = []
    while True:
        try:
            grade = int(input("Enter a grade (or -999 to finish): "))
            if grade == -999:
                break
            grades.append(grade)
        except ValueError:
            print("Please enter a valid number.")

    return tuple(zip(names, grades))


# 2. Difference between tuple and list
"""
- Tuple:
  - Immutable: Once created, its elements cannot be changed.
  - Faster and consumes less memory compared to lists.
  - Used when data integrity is crucial.

- List:
  - Mutable: Elements can be added, removed, or modified.
  - Preferred when frequent changes to the collection are needed.

Use tuple for fixed collections and list for dynamic collections.
"""

# 3. Explanation of mutable objects in tuples
"""
The code does not throw an error because the tuple itself is immutable, but the object inside the tuple (a dictionary) is mutable. 
Thus, while you cannot replace the dictionary with another object in the tuple, you can modify the dictionary's contents.

Example:

data_tuple = (
    {"name": "Alice", "age": 30, "city": "New York"},
    1000,
    "secret-code"
)
data_tuple[0]["age"] = 31  # This modifies the dictionary inside the tuple

data_tuple[0].clear()  # This clears all items from the dictionary inside the tuple

In summary, immutability of a tuple only applies to the tuple's structure, not the mutability of objects it contains.
"""

# END

# START
student = {
    'name': 'John',
    'age': 20,
    'hobbies': ['reading', 'games', 'coding'],
}


def print_student_data(student):
    for key, value in student.items():
        print(f"{key}: {value}")



def add_hobby(student, hobby):
    if hobby not in student['hobbies']:
        student['hobbies'].append(hobby)



add_hobby(student, 'swimming')
print_student_data(student)



def delete_hobby(student, hobby):
    if hobby in student['hobbies']:
        student['hobbies'].remove(hobby)



delete_hobby(student, 'games')
print_student_data(student)


student['family_name'] = 'Doe'
print_student_data(student)

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]


def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
    print()


print_matrix(matrix)

matrix = [
    [0, 1, 1],
    [0, 1, 0],
    [1, 0, 0]
]


def zero_count(matrix):
    count = 0
    for row in matrix:
        for element in row:
            if element == 0:
                count += 1
    return count


print(zero_count(matrix))

arr = [4, 2, 34, 4, 1, 12, 1, 4]


def find_dup(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)


print(find_dup(arr))

arr = [43, "what", 9, True, "cannot", False, "be", 3, True]


def reverse_array(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr


print(reverse_array(arr))

first_array = [4, 6, 7]
second_array = [8, 1, 9]


def sum_arrays(arr1, arr2):
    return [arr1[i] + arr2[i] for i in range(len(arr1))]


print(sum_arrays(first_array, second_array))


def is_palindrome(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]


print(is_palindrome("racecar"))  # True
print(is_palindrome("Java"))  # False

counter = 1
while counter < 100:
    print(counter)
    counter *= 2

counter = 900000
while counter > 50:
    print(counter)
    counter //= 2


def find_duplicates(arr):
    seen = []
    duplicates = []
    i = 0
    while i < len(arr):
        if arr[i] in seen and arr[i] not in duplicates:
            duplicates.append(arr[i])
        seen.append(arr[i])
        i += 1
    return duplicates


def find_duplicates(arr):
    seen = []
    duplicates = []
    i = 0
    while i < len(arr):
        if arr[i] in seen and arr[i] not in duplicates:
            duplicates.append(arr[i])
        seen.append(arr[i])
        i += 1
    return duplicates


def remove_duplicates(arr):
    unique = []
    i = 0
    while i < len(arr):
        if arr[i] not in unique:
            unique.append(arr[i])
        i += 1
    return unique


def remove_duplicates_skip_pete(arr):
    unique = []
    i = 0
    while i < len(arr):
        if arr[i].lower() != 'pete' and arr[i] not in unique:
            unique.append(arr[i])
        i += 1
    return unique


def find_consecutive_index(array):
    i = 1
    while i < len(array):
        if array[i] == array[i - 1]:
            return i
        i += 1
    return -1


array1 = [True, False, False, True, True, False]
array2 = [True, False, True, False, True, True]
array3 = [True, False, True, False, True, False]

print(find_consecutive_index(array1))  # 2
print(find_consecutive_index(array2))  # 5
print(find_consecutive_index(array3))  # -1


def get_valid_input(prompt, validation):
    while True:
        value = input(prompt)
        if validation(value):
            return value
        print("Invalid input. Try again.")


def is_valid_name(name):
    return len(name.split()) == 2 and all(word.isalpha() for word in name.split())


def is_valid_age(age):
    return age.isdigit() and 1 <= int(age) <= 130


def is_valid_email(email):
    return '@' in email and '.' in email


full_name = get_valid_input("Enter your full name: ", is_valid_name)
age = get_valid_input("Enter your age: ", is_valid_age)
email = get_valid_input("Enter your email: ", is_valid_email)

print(f"Name: {full_name}, Age: {age}, Email: {email}")

# END

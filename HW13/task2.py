#START

#part a
total_students = int(input("Enter the number of students: "))
students_per_class = 30
full_classes = total_students // students_per_class
remaining_students = total_students % students_per_class
print(f"Full classes: {full_classes}")
print(f"Students in the last class: {remaining_students}")

#part b
while True:
    try:
        number = int(input("Enter a number between 10 and 99: "))
        if 10 <= number <= 99:
            break
        else:
            print("Please enter a valid number between 10 and 99.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
tens = number // 10
units = number % 10
if units > tens:
    reversed_number = units * 10 + tens
    print(f"The reversed number is: {reversed_number}")
else:
    print(f"The number remains the same: {number}")

#part c
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
print("Prime numbers between 1 and 200:")
for number in range(1, 201):
    if is_prime(number):
        print(number, end=" ")
print()

#part d
answers_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
while True:
    answer = input("Enter an answer (a, b, c, d) or 'x' to exit: ").lower()
    if answer == 'x':
        break
    elif answer in answers_count:
        answers_count[answer] += 1
    else:
        print("Invalid input. Please enter 'a', 'b', 'c', 'd', or 'x' to exit.")
for answer, count in answers_count.items():
    print(f"Answer '{answer}': {count} responses")
most_frequent = max(answers_count, key=answers_count.get)
least_frequent = min(answers_count, key=answers_count.get)
print(f"The most frequent answer is '{most_frequent}' with {answers_count[most_frequent]} responses.")
print(f"The least frequent answer is '{least_frequent}' with {answers_count[least_frequent]} responses.")

#END
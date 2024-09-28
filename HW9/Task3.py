# START
array: list[int] = []

for i in range(101):
    array.insert(i, 0)

while True:
    user_input: int = int(input("Enter a a number between 0-10 or -999 for exit : "))

    if user_input == -999:
        break

    if user_input < 0 or user_input > 100:
        continue

    array[user_input] += 1

for i in range(101):
    print(f"the time {i} have been entered is {array[i]}")

# END

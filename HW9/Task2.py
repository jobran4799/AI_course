# START
array: list[int] = []

while True:
    user_input: int = int(input("Enter a a number between 0-10 or -999 for exit : "))

    if user_input == -999:
        break

    if user_input < 0 or user_input > 10:
        continue

    array.append(user_input)
    print("Statistics: ", end="")
    for i in range(11):
        count: int = array.count(i)
        if count > 0:
            print(f"[ {i} ]: {count} ", end="")
    print()

# END

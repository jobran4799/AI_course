# START
array: list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
while True:
    number: int = int(input("enter a number: "))
    if number == -999:
        break
    is_inserted = False
    for i in range(len(array)):
        if number < array[i]:
            array.insert(i, number)
            is_inserted = True
            break
    if not is_inserted:
        array.append(number)

print(array)

# END

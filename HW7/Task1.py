# START
positive: int = 0
negative: int = 0
zeros: int = 0
divide_in_seven: int = 0
last_positive = None
last_negative = None
for _ in range(10):
    num: int = int(input("give a number: "))
    if num == -9999:
        print("Exiting loop without statistics.")
        break
    if -1000 > num > 1000:
        continue
    if num == 0:
        zeros += 1
    elif num > 0:
        positive += 1
        last_positive = num
    else:
        negative += 1
        last_negative = num
    if num % 7 == 0:
        divide_in_seven += 1
else:

    print(f"Positive numbers: {positive}")
    print(f"Negative numbers: {negative}")
    print(f"Zeroes entered: {zeros}")
    print(f"Numbers divisible by 7: {divide_in_seven}")
    print(f"Last positive number: {last_positive if last_positive is not None else 'None'}")
    print(f"Last negative number: {last_negative if last_negative is not None else 'None'}")

# END

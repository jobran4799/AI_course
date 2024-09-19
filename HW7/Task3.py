# START
num: int = int(input("give a number: "))
if num % 2 == 1:
    for i in range(1, num + 1, 2):
        space: int = num - 1
        print(" " * (num-i), end=" ")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    for i in range(num - 2, 0, -2):
        print(" " * (num-i), end=" ")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
else:
    print("the number is not odd")

# END

# START
print("part a")
num: int = int(input("what is the number?"))
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
for i in range(num - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("part b")
number: int = int(input("what is the number?"))
space: int = number
for star in range(1, number + 1, 2):
    space = space - 1
    print(' ' * space + '*' * star)
print()

# END

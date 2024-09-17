# START
print("part a")
index: int = 0
while True:
    num: int = int(input("what is the number?"))
    if num % 11 == 0:
        break
    if num % 7 == 0:
        index += 1
    else:
        print(index)
        break

# END

# START
import random

number_to_guss: int = random.randint(1, 100)
index: int = 0

while True:
    num: int = int(input("pick a number"))
    if num == number_to_guss:
        print("BINGO")
        break
    elif num > number_to_guss:
        print("your number is to big")
    else:
        print("your number is to small")

# END

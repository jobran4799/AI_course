# START
print("part a")
while True:
    height: float = float(input("what is your height ?"))
    if 0.4 <= height <= 2.5:
        print("your height is perfect")
        break
    print("wrong input?")

print("part b")
first_num: int = int(input("what is your first_number ?"))
second_num: int = int(input("what is your second_number ?"))
if first_num > second_num:
    for i in range(first_num, second_num - 1, -1):
        print(i, end=" ")
else:
    for i in range(first_num, second_num + 1):
        print(i, end=" ")
print()

print("part c")
attempts: int = 3
while attempts > 0:
    pi: float = float(input("what is the value of pi?"))
    if pi == 3.14:
        print("you are correct")
        break
    else:
        print("your answer is noy correct! try again")
        attempts -= 1
        print(f"you have {attempts} attempts left")
if attempts == 0:
    print("pie is 3.14")

print("part d")
while True:
    first_num: float = float(input("what is your first_number ?"))
    is_first_num_valid: bool = 0 <= first_num <= 10
    second_num: float = float(input("what is your second_number ?"))
    is_second_num_valid: bool = 10 < second_num <= 60
    third_num: float = float(input("what is your third_number ?"))
    is_third_num_valid: bool = 60 < third_num <= 100

    if is_first_num_valid and is_second_num_valid and is_third_num_valid:
        is_average: bool = (first_num + second_num + third_num) / 3 == second_num
        if is_average:
            print(f"your numbers are wright")
            break
    print("try agin!")

# END

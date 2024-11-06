# START

# part1
# part 1.a
num1: int = int(input("enter a number?"))
num2: int = int(input("enter a number?"))
min_num: int = min(num1, num2)
for i in range(3):
    print(min_num, end=" ")
print()

# part 1.b

num1b: int = int(input("enter a number?"))
num2b: int = int(input("enter a number?"))
average_b: float = (num1b + num2b) / 2
print(average_b)

# part 1.c
num1c: int = int(input("enter a number?"))
num2c: int = int(input("enter a number?"))
num3c: int = int(input("enter a number?"))
max_num: int = max(num3c, num2c, num1c)
print(max_num)

# part 1.d
num1d: int = int(input("enter a number?"))
hours_d: int = num1d // 60
minute_d = num1d % 60
print(f"{hours_d} hours(s) and {minute_d} minute(s)")

# part 1.e
num1e: int = int(input("enter a number?"))
print(num1e % 10)

# part 1.f
num1f: int = int(input("enter a number?"))
print((num1f // 10) % 10)

# part 1.g
num1g: int = int(input("enter a number?"))
sum_numg: int = (num1g % 10) + (num1g // 10)
print(sum_numg)

# part 1.h
num1h: int = int(input("enter a number?"))
reversed_num: int = (num1h % 10) * 10 + (num1h // 10)
print(reversed_num)

# part 1.i
num1i: int = int(input("enter a number?"))
is_even: bool = num1i % 2 == 0
if is_even:
    print("even")
else:
    print("odd")

# part 1.j
num1j: int = int(input("enter a number?"))
if 6000 < num1j < 12000:
    print(f"the amount that should pay is {(num1j - 6000) * (10 / 100)}")
elif 12000 < num1j < 18000:
    print(f"the amount that should pay is {(num1j - 12000) * (20 / 100)}")
elif 18000 < num1j < 25000:
    print(f"the amount that should pay is {(num1j - 18000) * (30 / 100)}")
elif 25000 < num1j < 35000:
    print(f"the amount that should pay is {(num1j - 25000) * (40 / 100)}")
elif 35000 < num1j < 50000:
    print(f"the amount that should pay is {(num1j - 35000) * (45 / 100)}")
elif num1j > 50000:
    print(f"the amount that should pay is {((num1j - 50000) * (51 / 100))}")
else:
    print(f"no payment for you")

# part 1.k
age_k: int = int(input("enter your age?"))
high_k: int = int(input("enter your high?"))

if 8 < age_k < 18 and high_k > 115:
    print("you are allow to git in")
elif age_k > 18 and high_k > 100:
    print("you are allow to git in")
else:
    print("you are not allow to git in")

# part 2

# part 2.a
top_a: int = int(input("enter a number?"))
for i in range(1, top_a + 1):
    print(i, end=" ")
print()

# part 2.b
num1_2b: int = int(input("enter a number?"))
num2_2b: int = int(input("enter a number?"))

if num1_2b > num2_2b:
    for i in range(num2_2b, num1_2b + 1):
        print(i, end=" ")
else:
    for i in range(num1_2b, num2_2b + 1):
        print(i, end=" ")

# part 2.c
num1_2c: int = int(input("enter a number?"))
for i in range(0, num1_2c + 1, 2):
    print(i, end=" ")

# part d
max_2d: int = int(input("enter a max number?"))
den_2d: int = int(input("enter a divider number?"))
for i in range(0, max_2d + 1):
    if i % den_2d == 0:
        print(i, end=" ")

# part 3
# part 3.a
sum_3a: int = 0
num1_3a: int = int(input("enter a max number?"))
if num1_3a == -99:
    print(None)
else:
    while True:
        if num1_3a == -99:
            break
        sum_3a += num1_3a
        num1_3a = int(input("enter a max number?"))
    print(sum_3a)

# part 3.b
num1_3b: int = int(input("enter a number?"))
highest: int = 0
lowest: int = 1000
if num1_3b == -99:
    print(None)
else:
    while True:
        if num1_3b < 1:
            break
        if num1_3b > highest:
            highest = num1_3b
        elif num1_3b < lowest:
            lowest = num1_3b
        num1_3b = int(input("enter a number?"))
    print(f"the highest number is {highest} and the lowest number is {lowest}")

# part 3.c
max_num = int(input("enter a number?"))
index: int = 1
for i in range(2, 6):
    num1_3c: int = int(input("enter a number?"))
    if max_num < num1_3c:
        max_num = num1_3c
        index = i
print(f"the index of the higest number is {index}")

# part 3.d
num1_3d = int(input("enter a number?"))
num2_3d = int(input("enter a number?"))
mult_num_3d: int = 0
while num1_3d > 0:
    mult_num_3d += num2_3d
    num1_3d -= 1
print(mult_num_3d)

# part 3.e
num2_3e = int(input("enter pais?"))
num1_3e = int(input("enter power?"))
mult_num_3e: int = 1
while num1_3e > 0:
    mult_num_3e *= num2_3e
    num1_3e -= 1
print(mult_num_3e)

# part 3.f

num1_3f = int(input("enter a number?"))
num2_3f = int(input("enter a one digit number?"))
while num1_3f > 0:
    one_digit: int = num1_3f % 10
    if num2_3f == one_digit:
        print(True)
        break
    num1_3f = num1_3f // 10
else:
    print(False)

# part 3.g
num1_3g: int = int(input("enter a number?"))
num2_3g: int = int(input("enter a number?"))
run_on: int = max(num2_3g, num1_3g) // 2

for i in range(run_on, 0, -1):
    if num2_3g % i == 0 and num1_3g % i == 0:
        print(f"the max number that divides both is {i}")
        break

# part 3.h
num1_3h: int = int(input("enter a number?"))
is_prime = True
index: int = 2
if num1_3h == 2:
    print(True)
else:
    for i in range(2, (num1_3h // 2)):
        if num1_3h % index == 0:
            is_prime = False
            break
    print(is_prime)

# part 4

# part 4.a
temperatures_4a: list[float] = []
num_temps: int = 12
for i in range(num_temps):
    while True:
        try:
            temp = float(input(f"enter the temperature for month {i + 1}: "))
            if temp < -5 or temp > 40:
                print("wrong data")
                exit()

            if len(temperatures_4a) >= 1 and temperatures_4a[-1] == 0 and temp == 0:
                print("Consecutive zeros detected, please enter a valid temperature.")
                continue

            temperatures_4a.append(temp)
            break
        except ValueError:
            print("Invalid input, please enter a numeric value.")

if len(temperatures_4a) == num_temps:
    print("correct data")
    print(f"Average temperature for the year: {(sum(temperatures_4a) / num_temps):.2f}")
    print(f"Highest temperature: {max(temperatures_4a)}")
    print(f"Lowest temperature: {min(temperatures_4a)}")
else:
    print("Error: Not enough valid temperatures entered.")


# part 4.b
dic_4b: list[int] = [0, 0, 0, 0]
list_for_in_favor: list[int] = []
vote_subject = input(f"enter the subject: ")
last_vote_against: int = 0
for i in range(44):
    while True:
        try:
            vote_4b = int(input(f"enter your choose (1 in favor,2 for against ,3 for abstained, 4 for veto): "))
            match vote_4b:
                case 1:
                    dic_4b[0] += 1
                    list_for_in_favor.append(i+1)
                    break
                case 2:
                    dic_4b[1] += 1
                    last_vote_against = i+1
                    break
                case 3:
                    dic_4b[2] += 1
                    break
                case 4:
                    dic_4b[3] += 1
                    print(f" the country with the number {i+1} choose veto!")
                    exit()
                case _:
                    print("not a valid number try agin")
        except ValueError:
            print("Invalid input, please enter a numeric value.")

print(f"the number of the country's choose to vote in favor is {dic_4b[0]}")
print(f"the number of the country's choose to vote against is {dic_4b[1]}")
print(f"the number of the country's choose to vote abstained is {dic_4b[2]}")
print(f"first country choose to vote in favor is {list_for_in_favor[0]}")
print(f"last country choose to vote agnist is {last_vote_against}")



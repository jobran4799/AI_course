# START

while True:
    number_to_choose_task: int = int(input("""choose the number of the task:
                                           1 number less or bigger then 10
                                           2 three numbers the sum less or bigger the 100
                                           3 two float numbers and print the bigger float part
                                           4 check your age
                                           5 print the middel number of three digit number
                                           6 print all the numbers between 1 and number
                                           7 print all the even numbers between the two numbers
                                           8 print all the numbers that divided by 3,5 or 15 
                                           9 print all the numbers that divided by 7
                                           10 print the sum of negative numbers (0 for stop)
                                           11 print the numbers in revers (enter 10 numbers)
                                           12 print all the prime numbers (0 for stop)
                                           13 print the average and the numbers above the average (enter 5 numbers)
                                           14 print the result of divide two numbers
                                           15 print if the sum of digits of the number divided by 3
                                           16 print if the word is palindrome
                                           17 for stop
                                           task number : """))

    match (number_to_choose_task):
        case 1:
            # part a
            print("part 1a")
            number: int = int(input("enter a number? "))
            if number > 10:
                print(number - 10)
            else:
                print(number * 10)
        case 2:
            # part b
            print("part 1b")
            number1b: int = int(input("enter a number? "))
            number2b: int = int(input("enter a number? "))
            number3b: int = int(input("enter a number? "))
            sum_num = number3b + number2b + number1b
            if sum_num > 100:
                print(sum_num)
            else:
                print("the sum of the numbers is less then 100")
        case 3:
            # part c
            print("part 1c")
            number1c: float = float(input("enter a number? "))
            number2c: float = float(input("enter a number? "))
            number1c_float: float = number1c - int(number1c)
            number2c_float: float = number2c - int(number2c)

            if number1c_float > number2c_float:
                print(number1c_float)
            elif number2c_float > number1c_float:
                print(number2c_float)
            else:
                print("they are equal")
        case 4:
            # part d
            print("part 1d")
            number1d: int = int(input("enter your age? "))
            if 0 < number1d < 120:
                print(number1d)
            else:
                print("the number is not valid")
        case 5:
            # part e
            print("part 1e")
            number1e: int = int(input("enter a number between 100-999? "))
            print((number1e // 10) % 10)
        case 6:
            # part f
            print("part 1f")
            number1f: int = int(input("enter a number ? "))
            for i in range(1, number1f, -1):
                print(i)
        case 7:
            print("part 1g")
            number1g: int = int(input("enter a number ? "))
            number2g: int = int(input("enter a second number ? "))
            for i in range(number1g, number2g + 1):
                if i % 2 == 0:
                    print(i, end=" ")
            print()
        case 8:
            print("part 1h")
            number1h: int = int(input("enter a number ? "))
            for i in range(1, number1h):
                if i % 3 == 0 or i % 5 == 0:
                    print(i, end=" ")
            print()
        case 9:
            print("part 1i")
            number1i: int = int(input("enter a number ? "))
            for i in range(1, number1i):
                if i % 7 == 0:
                    print(i, end=" ")
            print()
        case 10:
            print("part 1j")
            sum1j: int = 0
            while True:
                number1j: int = int(input("enter a number ? "))
                if number1j == 0:
                    break
                if number1j < 0:
                    sum1j += number1j
            print(sum1j)
        case 11:
            print("part 1k")
            number1k: list[int] = []
            for i in range(0, 10):
                number1k.append(int(input("enter a number ? ")))
            for j in range(len(number1k) - 1, -1, -1):
                print(number1k[j], end=" ")
            print()
        case 12:
            print("part 1l")
            count1l: int = 0
            while True:
                number1l: int = int(input("enter a number ? "))
                isprime: bool = True
                if number1l == 0:
                    break
                mid1l = number1l // 2
                for i in range(1, mid1l):
                    if number1l % i == 0:
                        isprime = False
                        break
                if isprime:
                    count1l += 1
            print(f"the count of prime numbers is {count1l}")
        case 13:
            print("part 1m")
            number1m: list[int] = []
            sum1m = 0
            for i in range(0, 5):
                number1m.append(int(input("enter a number ? ")))
            for i in range(0, 5):
                sum1m += number1m[i]
            average1m = sum1m / 5
            print(f"the average is {average1m}")
            print("the numbers above the average are :", end=" ")
            for j in range(0, len(number1m)):
                if number1m[j] > average1m:
                    print(number1m[j], end=" ")
            print()
        case 14:
            print("part 1n")
            number1n: int = int(input("enter a number ? "))
            number2n: int = int(input("enter a number ? "))
            count1n: int = 0
            if number1n > number2n:
                while number1n >= number2n:
                    count1n += 1
                    number1n -= number2n
            else:
                while number2n >= number1n:
                    count1n += 1
                    number2n -= number1n
            print(count1n)
        case 15:
            print("part 1o")
            number1o: int = int(input("enter a number ? "))
            sum1o: int = 0
            while number1o > 0:
                last_dig: int = number1o % 10
                sum1o += last_dig
                number1o = number1o // 10
            if sum1o % 3 == 0:
                print(" the number is divided by 3")
            else:
                print(print(" the number is not divided by 3"))
        case 16:
            print("part 1p")
            string: str = input("enter a word ? ")
            index: int = 0
            istrue: bool = True
            index_str_from_end: int = len(string) - 1
            while index < (len(string) // 2):
                if string[index] != string[index_str_from_end]:
                    istrue = False
                    break
                index += 1
                index_str_from_end -= 1
            if istrue:
                print("the word is palindrome")
            else:
                print("the word is not palindrome")
        case 17:
            break
        case _:
            print("the number you choose is not valid please choose number between 1-17")

    # END

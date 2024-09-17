# START
num: int = int(input("what is the number?"))
string: str = ''
if num % 5 == 0:
    string += "Fizz "
if num % 3 == 0:
    string += "Buzz"
print(string)

# END

# START

str1 = " day-fun "
print(str1.strip())

print("hello".isalpha())

print("777".isdigit())

print(" ".isspace())

char_list = ['N', 'I', 'N', 'J', 'A', ]
print("".join(char_list))

print("*".join(char_list))

print("e" in "hELLo".lower())

word = input("enter a string?")
letter_list = [char.upper() for char in word if char.isalpha()]
print(letter_list)
# END

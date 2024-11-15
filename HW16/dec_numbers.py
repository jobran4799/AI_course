# START
cubes = {num: num ** 3 for num in range(1, 21)}
print("Cubes dictionary:", cubes)

num = int(input("Enter a number: "))
if num in cubes:
    print(f"The cube of {num} is {cubes[num]}")
else:
    print("Number does not exist in the dictionary.")

# END

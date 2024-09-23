# START
array: list = []
for i in range(1, 101):
    array.append(i)
print(f"first number: {array[0]}")
print(f"last number: {array[-1]}")
print(f"length of  list: {len(array)}")
print(f"in index 3-12 : {array[2:12]}")
print(f"from 80-100 : {array[79:]}")
print(f"from 0-17 : {array[:18]}")
print(f"list in revers : {array[::-1]}")
print(f"even number : {array[1::2]}")
print(f"number in 3 : {array[3:100:3]}")
print(f"number in 7 : {array[7:100:7]}")
print(f"number in 10 : {array[10:101:10]}")
print(f"number reverse by 3 : {array[99:65:-3]}")
array.insert(50, 999)
print("List after inserting 999 in the center:", array)
array.pop(100)
print("List after removing 100:", array)

# END

#START
#Q1a
print("Q1a")
num_of_slice: int = int(input("how many slices are?"))
num_of_slice_per_one = num_of_slice//4

if num_of_slice%4 == 0:
    print(f"each one got {num_of_slice_per_one}")
else:
    print(f"each one got {num_of_slice_per_one} and remaind {num_of_slice%4}")

#Q1b
print("Q1b")
num_of_friends: int = int(input("how many friends are?"))
num_of_slice: int = int(input("how many slices are?"))

num_of_slice_per_one = num_of_slice//num_of_friends

if num_of_slice%num_of_friends == 0:
    print(f"each one got {num_of_slice_per_one}")
else:
    print(f"each one got {num_of_slice_per_one} and remaind {num_of_slice%num_of_friends}")
#END
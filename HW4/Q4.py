# START
print("part a")
for i in range(10, 21):
    print(i)
print("part b")
for i in range(10, 21):
    if i % 2 == 0:
        print(i)
print("part c")
num_of_gap: int = int(input("please enter the gap?"))
i = 10
while i < 20:
    print(i)
    i += num_of_gap

# END

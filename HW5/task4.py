# START
pab: int = 10
times: int = 0
while pab > 0:
    age: int = int(input("what is your age?"))
    if age > 17:
        pab -= 1
    times += 1
print(f"you took {times} attempts to finish all the amount")
# END

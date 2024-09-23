# START
array_length: list = []
average = 0
highest_length = None
lowest_length = None
above_2_meter: int = 0
while True:
    length: float = float(input(" enter a number: "))

    if length == -999:
        break
    if length < 1.60 or length > 3.0:
        continue

    array_length.append(length)
    average += length
    if highest_length is not None:
        if highest_length < length:
            highest_length = length
    else:
        highest_length = length
    if lowest_length is not None:
        if lowest_length > length:
            lowest_length = length
    else:
        lowest_length = length
    if length > 2.0:
        above_2_meter += 1

print(f"number of players: {len(array_length)-1}")
print(f"highest_length: {highest_length}")
print(f"lowest_length: {lowest_length}")
print(f"average : {average / (len(array_length)-1)}")
print(f"number of player taller then 2 meters: {above_2_meter}")

average = average / (len(array_length)-1)
count: int = 0
for i in range(len(array_length)):
    if array_length[i] > average:
        count += 1
print(f"number of players above the average: {count}")

# END

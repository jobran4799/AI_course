# START
good_results = []
highest_score = 0
world_record = 6.23
world_record_holder = None

for _ in range(7):
    athlete_name = input("Enter the athlete's name: ")
    jump_result = float(input("Enter the athlete's jump result (in meters): "))

    if jump_result < 5.80:  # Ignore results below 5.80
        continue

    good_results.append(jump_result)

    if jump_result > highest_score:
        highest_score = jump_result

    if jump_result > world_record:
        world_record = jump_result
        world_record_holder = athlete_name

if good_results:
    average_result = sum(good_results) / len(good_results)
else:
    average_result = 0

print(f"Number of good results: {len(good_results)}")
print(f"Average of good results: {average_result:.2f} meters")
print(f"Highest jump: {highest_score:.2f} meters")

if world_record_holder:
    print(f"New world record: {world_record:.2f} meters by {world_record_holder}")
else:
    print("No new world record.")
# END

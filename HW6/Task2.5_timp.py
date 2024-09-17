# START

sum_temperature: int = 0
for _ in range(5):
    while True:
        temperature: int = int(input("what is the temperature?"))
        if -50 < temperature < 45:
            sum_temperature += temperature
            break

print(sum_temperature/5)

# END

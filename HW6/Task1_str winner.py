# START
import random

first_player: str = input("enter first name?")
second_player: str = input("enter second name?")
third_player: str = input("enter third name?")
forth_player: str = input("enter forth name?")
winner: str = random.choice([first_player, second_player, third_player, forth_player])
print(f"{winner} is the winner")

# END

#START

games_name = ["Grand Theft Auto V", "Fortnite", "The Elder Scrolls V: Skyrim", "Dark Souls", "Overwatch"]

print("Games with names longer than 8 letters:", list(filter(lambda x: len(x) > 8, games_name)))

print("Games starting with F:", list(filter(lambda x: x.startswith('F'), games_name)))

print("Games with exactly two words in their name:", list(filter(lambda x: len(x.split()) == 2, games_name)))

print("Games containing the letter V:", list(filter(lambda x: 'V' in x, games_name)))


#END
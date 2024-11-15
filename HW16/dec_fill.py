# START

text = """
This chocolate cake is rich, moist, and full of delicious chocolate flavor.
To make the cake, you will need chocolate, flour, sugar, eggs, and butter.
After baking the chocolate cake, let the cake cool before adding the chocolate frosting.
"""

words = text.lower().replace('.', '').replace(',', '').split()
word_count: dict[str, int] = dict()
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print("Word counts:", word_count)
most_frequent_word = max(word_count, key=word_count.get)
print("Most frequent word:", most_frequent_word)

letters = [char for char in text.lower() if char.isalpha()]
letter_count: dict[str, int] = dict()
for c in letters:
    letter_count[c] = letter_count.get(c, 0) + 1
print("Letter counts:", letter_count)
least_frequent_letter = min(letter_count, key=letter_count.get)
print("Least frequent letter:", least_frequent_letter)
# END

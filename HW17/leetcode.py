def length_of_last_word(s: str) -> int:
    words = s.split()
    print(words)
    return len(words[-1])


print(length_of_last_word("Hello World"))  # Output: 5
print(length_of_last_word("   fly me   to   the moon  "))  # Output: 4
print(length_of_last_word("luffy is still joyboy"))  # Output: 6
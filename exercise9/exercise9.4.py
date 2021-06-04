def uses_only(word, letters):
    """Write a function named uses_only that takes a word and a string of letters, and
that returns True if the word contains only letters in the list."""
    for letter in letters:
        if letter not in word:
            return False
    return True


print(uses_only('banana', 'abn'))
print(uses_only('banana', 'xy'))

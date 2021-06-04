def uses_all(word, letters):
    """Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once."""
    for letter in letters:
        if not(letter in word):
            return False
    return True


print(uses_all('banana', 'abn'))
print(uses_all('banana', 'xy'))

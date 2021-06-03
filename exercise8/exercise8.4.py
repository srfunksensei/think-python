def find(word, letter, start):
    """Modify find so that it has a third parameter, the index in word where it should start looking."""
    if start > len(word):
        return -1

    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


print(find('banana', 'a', 0))
print(find('banana', 'm', 0))
print(find('banana', 'a', 2))
print(find('banana', 'a', 22))

def find(word, letter, start):
    """Modify find so that it has a third parameter, the index in word where it should start looking."""
    if start >= len(word):
        return -1

    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


def count(word, search_letter):
    """Rewrite this function so that instead of traversing the string, it uses the threeparameter
version of find from the previous section."""
    letter_count = 0
    start_position = 0
    while True:
        start_position = find(word, search_letter, start_position)
        if start_position < 0:
            break
        letter_count += 1
        start_position += 1
    print(letter_count)


count('banana', 'a')
count('banana', 'm')

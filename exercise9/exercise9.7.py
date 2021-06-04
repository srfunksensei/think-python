def is_triple_double(word):
    """Give me a word with three consecutive double letters."""
    if len(word) < 6:
        return False

    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            i = i + 1 - 2 * count
            count = 0
    return False


print(is_triple_double('bookkeeper'))
print(is_triple_double('aggressiveness'))

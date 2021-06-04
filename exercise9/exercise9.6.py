def is_abecedarian(word):
    """Write a function called is_abecedarian that returns True if the letters in a word
appear in alphabetical order (double letters are ok)."""
    if len(word) == 0:
        return false

    letter_ord = word[0]
    index = 1
    while index < len(word):
        next_letter_ord = word[index]
        if letter_ord > next_letter_ord:
            return False
        letter_ord = word[index]
        index += 1
    return True


print(is_abecedarian('abcdeefgh'))
print(is_abecedarian('bcdaefgh'))

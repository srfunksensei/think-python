def rotate_letter(letter, step):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    char_ord = ord(letter) - start
    letter_index = (char_ord + step) % 26 + start
    return chr(letter_index)


def rotate_word(word, step):
    """returns a new string that contains the letters from the original string “rotated” by the given amount"""
    result = ""
    for c in word:
        result += rotate_letter(c, step)
    return result


print(rotate_word('CHEER', 33))
print(rotate_word('cheer', 7))
print(rotate_word('MELON', -36))
print(rotate_word('melon', -10))



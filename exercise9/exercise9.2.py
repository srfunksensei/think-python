def has_no_e(word):
    """Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it."""
    return not('e' in word)


def print_no_e_words():
    fin = open('exercise9_1.txt')

    num_no_e_words = 0
    total_words = 0

    for line in fin:
        word = line.strip()
        total_words += 1
        if has_no_e(word):
            print(word)
            num_no_e_words += 1

    if total_words > 0:
        print(str(int(num_no_e_words / total_words * 100)) + "/100%")


print_no_e_words()
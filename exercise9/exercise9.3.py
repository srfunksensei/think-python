from pip._vendor.distlib.compat import raw_input


def avoid(word, letters):
    """Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters"""
    for letter in letters:
        if letter in word:
            return True
    return False


print(avoid('banana', 'a'))
print(avoid('banana', 'xy'))


def which_words_avoid(file, letters):
    total_words = 0

    fin = open(file)
    for line in fin:
        word = line.strip()
        total_words += 1
        if avoid(word, letters):
            print(word)
            total_words += 1
    return total_words


prompt = 'Enter file with words to check: '
file = raw_input(prompt)
prompt = 'Enter forbidden letters: '
avoid_letters = raw_input(prompt)

which_words_avoid(file, avoid_letters)
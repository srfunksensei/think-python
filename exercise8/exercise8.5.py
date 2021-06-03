def count(word, search_letter):
    """Encapsulate this code in a function named count, and generalize it so that it accepts
the string and the letter as arguments"""
    letter_count = 0
    for letter in word:
        if letter == search_letter:
            letter_count = letter_count + 1
    print(letter_count)


count('banana', 'a')
count('banana', 'm')

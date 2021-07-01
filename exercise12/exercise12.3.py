def most_frequent(word):
    """Write a function called most_frequent that takes a string and prints the letters
in decreasing order of frequency"""
    d = dict()
    for letter in word:
        d[letter] = d.setdefault(letter, 0) + 1

    a = []
    for letter, freq in d.items():
        a.append((freq, letter))

    a.sort(reverse=True)

    res = []
    for freq, letter in a:
        res.append(letter)
    return res


print(most_frequent("mmiiiilan"))

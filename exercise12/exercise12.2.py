import random


def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))
    t = t[::-1]
    res = []
    for length, word in t:
        res.append(word)
    return res


def sort_by_length_random(words):
    """Modify this example so that words with the same length appear in random order."""
    t = []
    for word in words:
        t.append((len(word), word))
    random.shuffle(t)
    res = []
    for length, word in t:
        res.append(word)
    return res


print(sort_by_length(["milan", "jovan", "maksa"]))
print(sort_by_length_random(["milan", "jovan", "maksa"]))
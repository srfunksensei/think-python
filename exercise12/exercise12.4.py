# 1
def anagrams(word_list):
    """Write a program that reads a word list from a file and prints all the sets of
words that are anagrams."""
    d = dict()
    for word in word_list:
        key = ''.join(sorted(word))
        if key not in d.keys():
            d.setdefault(key, [])
        d[key].append(word)
    return d


print(anagrams(['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled', 'retainers', 'ternaries']))


# 3
def filter_by_length(anagrams_dictionary, word_len):
    d = dict()
    for key, values in anagrams_dictionary.items():
        if len(key) == word_len:
            d[key] = values
    return d

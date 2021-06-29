def make_dict_with_words(file_name):
    """Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn’t matter what the values are."""
    words2dict = dict()
    fin = open(file_name)
    for line in fin:
        key = line.strip()
        if key not in words2dict:
            words2dict[key] = key
    return words2dict

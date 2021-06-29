def histogram(s):
    """Use get to write histogram more concisely"""
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def print_hist(h):
    """Modify print_hist to print the keys and their values in alphabetical order"""
    keys = list(h.keys())
    keys.sort()
    for c in keys:
        print(c, h[c])


h = histogram('parrot')
print(print_hist(h))

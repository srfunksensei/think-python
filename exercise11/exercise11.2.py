def histogram(s):
    """Use get to write histogram more concisely"""
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


print(histogram('brontosaurus'))

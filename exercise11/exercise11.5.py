def invert_dict(d):
    """more concise version of invert_dict with setdefault"""
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, [])
        inverse[val].append(key)
    return inverse


inverse = invert_dict({'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1})
print(inverse)

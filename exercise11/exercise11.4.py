def histogram(s):
    """Use get to write histogram more concisely"""
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def reverse_lookup(d, v):
    """Modify reverse_lookup so that it builds and returns a list of all keys that map to
v, or an empty list if there are none"""
    result = []
    for k in d:
        if d[k] == v:
            result.append(k)
    return result


h = histogram('parrot')
k = reverse_lookup(h, 2)
print(k)
k = reverse_lookup(h, 3)
print(k)


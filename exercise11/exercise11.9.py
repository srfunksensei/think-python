def has_duplicates(array):
    """Use a dictionary to write a faster, simpler version of has_duplicates"""
    d = dict()
    for elem in array:
        if elem in d:
            return True
        d.setdefault(elem, 1)
    return False


print(has_duplicates([1, 2, 3, 4, 1]))
print(has_duplicates([1, 2, 3, 4, 9]))

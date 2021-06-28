from bisect import bisect_left


def bisect(array, value):
    """Write a function called bisect that takes a sorted list and a target value and returns the index of
the value in the list, if it’s there, or None if it’s not."""
    i = bisect_left(array, value)
    if i != len(array) and a[i] == value:
        return i
    return 'None'

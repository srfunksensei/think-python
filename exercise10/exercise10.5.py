def chop(array):
    """Write a function called chop that takes a list, modifies it by removing the first and
last elements, and returns None."""
    if len(array) < 2:
        return ''
    del array[0]
    del array[len(array) - 1]
    return 'None'


test_array = [1, 2, 3, 4]
print(chop(test_array))
print(test_array)

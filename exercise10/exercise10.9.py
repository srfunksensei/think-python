def remove_duplicates(array):
    """Write a function called remove_duplicates that takes a list and returns a new
list with only the unique elements from the original."""
    copy_array = array[:]
    copy_array.sort()

    to_return_array = copy_array[:]

    val = copy_array[0]
    for i in range (1, len(array)):
        if val == copy_array[i]:
            to_return_array.remove(val)
        val = copy_array[i]

    return to_return_array


print(remove_duplicates([1, 1, 2, 1, 2, 3, 4, 3, 5]))

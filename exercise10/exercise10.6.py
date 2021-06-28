def is_sorted(array):
    """Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that
the elements of the list can be compared with the relational operators <, >, etc."""
    copy_array = array[:]
    copy_array.sort()

    return copy_array == array


print(is_sorted([1, 2, 3, 4]))
print(is_sorted([4, 2, 1, 3]))

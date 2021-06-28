def nested_sum(array):
    """Write a function called nested_sum that takes a nested list of integers and add up
the elements from all of the nested lists"""
    total = 0
    for elem in array:
        total += sum(elem)
    return total


print(nested_sum([[1, 2], [3, 4], [5, 6]]))

def middle(array):
    """Write a function called middle that takes a list and returns a new list that contains
all but the first and last elements. So middle([1,2,3,4]) should return [2,3]."""
    if len(array) < 2:
        return []
    return array[1:len(array) - 1]


print(middle([1, 2, 3, 4]))

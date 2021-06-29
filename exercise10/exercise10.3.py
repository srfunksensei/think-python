def cumulative_sum(array):
    """Write a function that takes a list of numbers and returns the cumulative sum; that
is, a new list where the ith element is the sum of the first i + 1 elements from the original list. For
example, the cumulative sum of [1, 2, 3] is [1, 3, 6]."""
    res = []
    val = 0
    for elem in array:
        val += elem
        res.append(val)
    return res


print(cumulative_sum([1, 2, 3]))

def sumall(*args):
    """Write a function called sumall that takes any number of arguments and returns their sum."""
    total = 0
    for elem in args:
        total += elem
    return total


print(sumall(1,2,3))

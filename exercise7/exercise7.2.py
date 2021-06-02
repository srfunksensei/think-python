def square_root(a):
    """returns an estimate of the square root of a"""
    x = a - 1
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return x


print(square_root(4))
print(square_root(9))
print(square_root(16))

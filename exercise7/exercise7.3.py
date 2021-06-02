import math


def square_root(a):
    """returns an estimate of the square root of a"""
    x = a - 1
    if x > 0:
        while True:
            y = (x + a/x) / 2
            if y == x:
                break
            x = y
    return x


def test_square_root(a):
    """test_square_root that prints a table like this:
    The first column is a number, a; the second column is the square root of a computed with the function
from exercise 7.2; the third column is the square root computed by math.sqrt; the fourth column is
the absolute value of the difference between the two estimates"""
    function_square_root = square_root(a)
    math_square_root = math.sqrt(a)
    print(a, function_square_root, math_square_root, abs(function_square_root - math_square_root))


a = 1
while a < 10:
    test_square_root(a)
    a = a + 1

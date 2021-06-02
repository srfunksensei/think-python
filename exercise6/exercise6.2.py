def hypotenuse(a, b):
    """write a function called hypotenuse that returns the
length of the hypotenuse of a right triangle given the lengths of the two legs as arguments."""
    if a < 0 or b < 0:
        print("invalid arguments")
    return a * a + b * b

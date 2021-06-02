def is_power(a, b):
    """A number, a, is a power of b if it is divisible by b and a/b is a power of b."""
    if b <= 0:
        return False

    if a % b == 0:
        if a == b:
            return True
        else:
            return is_power(a/b, b)
    return False


print(is_power(29, 3))
print(is_power(8, 2))

def gcd(a, b):
    """returns their greatest common divisor"""
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(15, 45))
print(gcd(15, 35))
print(gcd(100, 104))
print(gcd(-30, 95))

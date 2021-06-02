import math


def factorial(n):
    """Computes factorial of n."""
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result


def estimate_pi():
    """return an estimate of"""
    k = 0
    sum_value = 0
    while True:
        numerator = factorial(4 * k) * (1103 + 26390 * k)
        denominator = factorial(k)**4 * 396**(4 * k)
        term = numerator / denominator
        sum_value += term
        if abs(term) < 1e-15:
            break
        k = k + 1

    factor = 2 * math.sqrt(2) / 9801
    return 1 / (factor * sum_value)


print(estimate_pi())

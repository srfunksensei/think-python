def ack(m, n):
    """Write a function named ack that evaluates Ackermann’s function http://en.wikipedia.org/wiki/Ackermann_function
    """
    if m < 0 or n < 0:
        print("invalid value")

    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))


print(ack(3, 4))

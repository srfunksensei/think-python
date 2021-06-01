def do_n(f, n):
    """Write a function called do_n that takes a function object and a number, n, as arguments,
and that calls the given function n times"""
    if n <= 0:
        return
    f(n)
    do_n(f, n - 1)

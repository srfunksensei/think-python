from pip._vendor.distlib.compat import raw_input


# 1
def is_triangle(a, b, c):
    """Write a function named is_triangle that takes three integers as arguments, and that prints
either “Yes” or “No,” depending on whether you can or cannot form a triangle from sticks
with the given lengths."""
    if a <= 0 or b <= 0 or c <= 0:
        print("No")
    if (a * a + b * b == c * c) or (a * a + c * c == b * b) or (b * b + c * c == a * a):
        print("Yes")
    else:
        print("No")


# 2
prompt = 'Enter length of three sticks to check if they can form triangle?\nFirst: '
first = int(raw_input(prompt))

prompt = 'Second: '
second = int(raw_input(prompt))

prompt = 'Third: '
third = int(raw_input(prompt))

is_triangle(first, second, third)

def is_palindrome(word):
    """Write a function called is_palindrome that takes a string argument and returns True if it
is a palindrome and False otherwise."""
    return word == word[::-1]


def is_number_palindromic(number):
    """Write a Python program that tests all the six-digit numbers and prints any numbers that satisfy
these requirements"""
    if len(str(number)) != 6 and len(str(number + 4)):
        return False

    return is_palindrome(str(number)[2:6]) and is_palindrome(str(number + 1)[1:6]) and is_palindrome(str(number + 2)[1:5]) and is_palindrome(str(number + 3))


for i in range(100000, 1000000):
    if is_number_palindromic(i):
        print(i)

def is_palindrome(word):
    """Write a function called is_palindrome that takes a string argument and returns True if it
is a palindrome and False otherwise."""
    return word == word[::-1]


print(is_palindrome('anavolimilovana'))

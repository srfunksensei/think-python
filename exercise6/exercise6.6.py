def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


# 1
print(middle('ab'))
print(middle('a'))
print(middle(''))


# 2
def is_palindrome(word):
    """Write a function called is_palindrome that takes a string argument and returns True if it
is a palindrome and False otherwise."""
    if len(word) == 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


print(is_palindrome('anavolimilovana'))

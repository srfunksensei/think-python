def backward(word):
    """displays the letters backward, one per line"""
    index = len(word) - 1
    while index >= 0:
        print(word[index])
        index -= 1


backward('anavolimilovana')

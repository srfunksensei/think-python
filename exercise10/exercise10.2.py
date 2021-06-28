def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


def capitalize_nested(array_of_strings):
    """Use capitalize_all to write a function named capitalize_nested that takes
a nested list of strings and returns a new nested list with all strings capitalized."""
    res = []
    for elem in array_of_strings:
        res.append(capitalize_all(elem))
    return res


print(capitalize_nested([["milan"], ["car", "najveci"]]))

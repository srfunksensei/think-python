import random


def has_duplicates(array):
    """Write a function called has_duplicates that takes a list and returns True if there is any
element that appears more than once. It should not modify the original list."""
    copy_array = array[:]
    copy_array.sort()

    val = copy_array[0]
    for i in range (1, len(array)):
        if val == copy_array[i]:
            return True
    return False


print(has_duplicates([1, 2, 3, 4, 1]))
print(has_duplicates([1, 2, 3, 4, 9]))


"""If there are 23 students in your class, what are the chances that two of you have the same
birthday? You can estimate this probability by generating random samples of 23 birthdays and
checking for matches. Hint: you can generate random birthdays with the randint function
in the random module."""


def generate_random_birthdays(n):
    array = []
    for i in range(n):
        array.append(random.randint(1, 365))
    return array


count = 0
simulation_count = 10000
for i in range(0, simulation_count):
    students = generate_random_birthdays(23)
    if has_duplicates(students):
        count += 1

print("probability: " + str(int(count * 100 / simulation_count)) + "/100%")
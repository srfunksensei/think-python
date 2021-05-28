# 1
def do_twice(f):
    f()
    f()


def print_spam():
    print('spam')


do_twice(print_spam)


# 2
def do_twice1(f, value):
    f(value)
    f(value)


# 3
def print_twice(value):
    print(value)
    print(value)


# 4
do_twice1(print_twice, 'spam')


# 5
def do_four(f, value):
    do_twice1(f, value)
    do_twice1(f, value)
# 1

def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def print_outside():
    print_row('+ - - - -')


def print_inside():
    print_row('|        ')


def print_row(value):
    print(value, end=' ')


def print_out():
    do_twice(print_outside)
    print('+')


def print_in():
    do_twice(print_inside)
    print('|')


def print_half():
    print_out()
    do_four(print_in)


def print_grid():
    do_twice(print_half)
    print_out()


print_grid()

# 2


def print_out_4():
    do_four(print_outside)
    print('+')


def print_in_4():
    do_four(print_inside)
    print('|')


def print_half_4():
    print_out_4()
    do_four(print_in_4)


def print_grid_4():
    do_four(print_half_4)
    print_out_4()


print_grid_4()
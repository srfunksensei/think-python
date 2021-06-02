from pip._vendor.distlib.compat import raw_input


def eval_loop():
    """Write a function called eval_loop that iteratively prompts the user, takes the resulting input and
evaluates it using eval, and prints the result."""
    while True:
        prompt = 'Type input to eval:\n'
        expression = raw_input(prompt)
        print(eval(expression))


eval_loop()

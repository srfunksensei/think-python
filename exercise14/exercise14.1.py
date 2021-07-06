import os


def walk(dirname):
    """print the names of the files in a given directory and
its subdirectories"""
    for root, dirs, files in os.walk(dirname):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            walk(name)


walk('.')
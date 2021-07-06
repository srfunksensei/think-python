import os
import hashlib


def filter_files_with_extension(dirname, extension):
    file_names = []
    for root, dirs, files in os.walk(dirname):
        for name in files:
            if name.endswith('.' + extension):
                file_names.append(os.path.join(root, name))
        for name in dirs:
            file_names.extend(filter_files_with_extension(name, extension))
    return file_names


def find_duplicates(dirname, extension):
    """Write a program that searches a directory and all of its subdirectories, recursively, and returns
a list of complete paths for all files with a given suffix (like .mp3)."""
    possible_duplicates = dict()

    for file in filter_files_with_extension(dirname, extension):
        file_name = os.path.basename(file)
        possible_duplicates.setdefault(file_name, [])
        possible_duplicates[file_name].append(file)

    duplicates = dict()
    for file_name, items in possible_duplicates.items():
        if len(items) > 1:
            checksum_first = hashlib.md5(open(items[0], 'rb').read()).hexdigest()
            duplicates[checksum_first] = [items[0]]

            for i in range(1, len(items)):
                checksum = hashlib.md5(open(items[i], 'rb').read()).hexdigest()
                if checksum_first == checksum:
                    duplicates[checksum_first].append(items[i])

    return duplicates

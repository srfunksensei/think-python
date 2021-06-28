"""Write a function that reads the file words.txt and builds a list with one element
per word. Write two versions of this function, one using the append method and the other using
the idiom t = t + [x]. Which one takes longer to run? Why?"""


def make_array_of_words1(file_name):
    array = []
    fin = open(file_name)
    for line in fin:
        array.append(line.strip())
    return array


def make_array_of_words2(file_name):
    array = []
    fin = open(file_name)
    for line in fin:
        array = array + [line.strip()]
    return array


start_time = datetime.now()
make_array_of_words1('words.txt')
elapsed_time = datetime.now() - start_time
print("version1 took: " + str(elapsed_time) + "s")


start_time = datetime.now()
make_array_of_words2('words.txt')
elapsed_time = datetime.now() - start_time
print("version2 took: " + str(elapsed_time) + "s")
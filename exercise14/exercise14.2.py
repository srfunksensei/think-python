def sed(regex, replacement, file1, file2):
    """Write a function called sed that takes as arguments a pattern string, a replacement string, and two filenames;
    it should read the first file and write the contents into the second file (creating it if necessary). If the
    pattern string appears anywhere in the file, it should be replaced with the replacement string. If an error
    occurs while opening, reading, writing or closing files, your program should catch the exception, print an error
    message, and exit """
    try:
        fin = open(file1)
        fout = open(file2, 'w')
        for line in fin:
            fout.write(line.replace(regex, replacement))
        fin.close()
        fout.close()
    except:
        print('Something went wrong.')

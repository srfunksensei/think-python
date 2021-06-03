prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    addon = ''
    if letter == 'Q' or letter == 'O':
        addon = 'u'
    print(letter + addon + suffix)

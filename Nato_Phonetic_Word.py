
def Nato_It(alnum_str):
    translate_dictionary = {
        'a': 'Alpha',
        'b': 'Bravo',
        'c': 'Charlie',
        'd': 'Delta',
        'e': 'Echo',
        'f': 'Foxtrot',
        'g': 'Golf',
        'h': 'Hotel',
        'i': 'India',
        'j': 'Juliett',
        'k': 'Kilo',
        'l': 'Lima',
        'm': 'Mike',
        'n': 'November',
        'o': 'Oscar',
        'p': 'Papa',
        'q': 'Quebec',
        'r': 'Romeo',
        's': 'Sierra',
        't': 'Tango',
        'u': 'Uniform',
        'v': 'Victor',
        'w': 'Whiskey',
        'x': 'Xray',
        'y': 'Yankee',
        'z': 'Zulu',
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine',
        '0': 'Zero'}
    NATO_list = []
    white_remove = 0
    for i in list(alnum_str):
        if i.isalpha():
            NATO_list.append(translate_dictionary[i.lower()])
        elif i.isdecimal():
            NATO_list.append(translate_dictionary[i])
        else:
            white_remove += 1

    return ' '.join(NATO_list)


print(Nato_It('Hello!!'))
print(Nato_It('abc ABC 1 2 3'))
print(Nato_It('Hello World'))
print(Nato_It('OX10 6HF'))

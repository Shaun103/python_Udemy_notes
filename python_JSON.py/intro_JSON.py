# https://www.ncdc.noaa.gov/cag/

import json
import urllib.request


def main():
    print()


    # languages = [
    #     ['ABC', 1987],
    #     ['Algol 68', 1968],
    #     ['APL', 1962],
    #     ['C', 1973],
    #     ['Haskell', 1990],
    #     ['Lisp', 1958],
    #     ['Modula-2', 1977],
    #     ['Perl', 1987],
    # ]

    languages = [
        ('ABC', 1987),
        ('Algol 68', 1968),
        ('APL', 1962),
        ('C', 1973),
        ('Haskell', 1990),
        ('Lisp', 1958),
        ('Modula-2', 1977),
        ('Perl', 1987),
    ]


    path = '/Users/User/Desktop/Python_Udemy/python_JSON.py/test.json'

    # writes to JSON file
    with open(path, 'w', encoding='utf-8') as testfile:
        json.dump(languages, testfile)
    
    for x in languages:
        if 1987 in x:
            print('found!', x)
#____________________________________________________________________________

    # reads from JSON files 
    # with open(path, 'r', encoding='utf-8') as testfile:
    #     data = json.load(testfile)
    
    # print(data)
    # print()
    # print(data[2])


if __name__ == "__main__":
    main()
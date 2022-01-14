def main():
    print()

#________________________________________________________________


    path = 'Jabberwocky.txt'

    with open(path) as poem:
        first = poem.readline().rstrip()
    
    print(first)

    chars = "' Twasebv"

#________________________________________________________________


    # removes text/characters at the beginning of a line
    twas_removed = first.removeprefix("'Twas")
    print(twas_removed)

    # removes text/characters from the end of a line
    toves_removed = first.removesuffix('toves')
    print(toves_removed)

#________________________________________________________________

    print('*'*80)

# creating functions that act similar to .removeprefix() / .removesuffix
# .startswith() / .endswith()

    def removeprefix(string: str, prefix: str) -> str:
        if string.startswith(prefix):
            return string[len(prefix):]
        else:
            return string[:] # return a copy of string 


    def removesuffix(string: str, suffix: str) -> str:
        if suffix and string.endswith(suffix):  # suffix='' should not call string[:-0]
            return string[:-len(suffix)]
        else:
            return string [:]


    twas_removed = removeprefix(first, "'Twas")
    print(twas_removed)

    toves_removed = removesuffix(first, 'toves')
    print(toves_removed)





if __name__ == "__main__":
    main()
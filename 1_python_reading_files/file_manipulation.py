


    # .strip() - removes white space
    # .rstrip() - removes white space from the left side of the string


def main():
    print()



# #   runs whole file within memory 

#     with open('Jabberwocky.txt', 'r') as jabber:
#         for line in jabber:
#             print(line.strip())
#         lines = jabber.readlines()

#     # iterating through a file 
#     print(lines)
#     print(lines[-1:])


#     # Printing in reverse
#     for line in reversed(lines):
#         print(line, end=" ")

#________________________________________________________________

# alternative method to run the program

    with open('Jabberwocky.txt') as jabber:
        text = jabber.read()

    print(text)

# reverses text in file 
    for character in reversed(text):
        print(character, end='')

#________________________________________________________________

# if you want to process the string 
    with open('Jabberwocky.txt') as jabber:
        while True:
            line = jabber.readline().rstrip()
            print(line)
            if 'jubjub' in line.casefold():
                break


    print('*'*80)

# prints the line contains the text we are looking for  

    with open('Jabberwocky.txt') as jabber:
        for line in jabber:
            print(line.rstrip())
            if 'jubjub' in line.casefold():
                break

#________________________________________________________________

    print('*'*80)

    path = 'Jabberwocky.txt'


    with open(path) as poem:
        first = poem.readline().rstrip()
    
    print(first)

    chars = "' Twasebv"

    # no_apostrophe = first.strip(chars)
    # print(no_apostrophe)

#________________________________________________________________

# how the strip method work 

    for character in first:
        if character in chars:
            print(f'"removing "{character}"')
        else:
            break

    print('*'*80)

    for character in first[::-1]:   # processes backwards 
        if character in chars:
            print(f'"removing "{character}"')
        else:
            break


if __name__ == "__main__":
    main()
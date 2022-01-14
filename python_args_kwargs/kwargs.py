# def print_backwards(*args, **kwargs):
#     end_character = kwargs.pop('end', '\n')
#     sep_character = kwargs.pop('sep', ' ')
#     for word in args[:0:-1]:    # change the range
#         print(word[::-1], end=sep_character, **kwargs)
#     print(args[0][::-1], end=end_character, **kwargs) # and print the first word seperately 
#     # print(end=end_character)  # which means we don't need this line

# list comprehension method
def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)

#________________________________________________________________
# two ways of doing the same thing

# def print_backwards(*args, end=' ', **kwargs):
#     print(kwargs)
#     kwargs.pop('end', None)
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)


# def print_backwards(*args, end=' ', **kwargs):
#     print(kwargs)
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)

#_________________________________________________________________

# def print_backwards(*args, file=None):
#     for word in args[::-1]:
#         print(word[::-1], end='\n', file=file)


def main():


    with open("backwards.txt", 'w') as backwards:
        backwards_print('hello', 'planet', 'earth', 'take', 'me', 'to', 'your', 'leader', file=backwards)
        print("Another String", file=backwards)
        print(file=backwards)
        print('hello', 'planet', 'earth', 'take', 'me', 'to', 'your', 'leader', end='', sep='\n**\n', file=backwards)
        backwards_print('hello', 'planet', 'earth', 'take', 'me', 'to', 'your', 'leader', end='', sep='\n**\n', file=backwards)
        print('='*10, file=backwards)


if __name__ == "__main__":
    main()
# https://docs.python.org/3/library/timeit.html

import timeit

list_comp1 = """\
def text_comp1(text):
    capitals = [char.upper() for char in text]
    return capitals    
"""


map_comp1 = """\
def text_comp2(text):
    map_capitals = list(map(str.upper, text))
    return map_capitals    
"""


list_comp2 = """\
def text_comp3(text):
    words = [word.upper() for word in text.split(' ')]
    return words    
"""


map_comp2 = """\
def text_comp4(text):
    map_words = list(map(str.upper, text.split(' ')))
    return map_words    
"""

# _____________________________________________________________


text = "what have the romans ever done for us"

# capitals = [char.upper() for char in text]
# print(capitals)

# # use map 
# map_capitals = list(map(str.upper, text))
# print(map_capitals)


# _____________________________________________________________


# words = [word.upper() for word in text.split(' ')]
# print(words)


# # use map 
# map_words = list(map(str.upper, text.split(' ')))
# print(map_words)


# for x in map(str.upper, text.split(' ')):
#     print(x)

# _____________________________________________________________

# print(text_comp1(text))
# print(text_comp2(text))
# print(text_comp3(text))
# print(text_comp4(text))

#_________________________________________________________________


if __name__ == "__main__":

    # print(timeit.timeit(list_comp1))
    # print(timeit.timeit(map_comp1))

    # print(timeit.timeit(list_comp2))
    # print(timeit.timeit(map_comp2))

    # print(timeit.repeat(list_comp1), 3)
    # print(timeit.repeat(map_comp1), 3)

    # print(timeit.repeat(list_comp2), 3)
    # print(timeit.repeat(map_comp2), 3)


    # print(timeit.timeit("list_comp1", setup="from map_intro import list_comp1", number=10000))

    #_________________________________________________________________

    print(timeit.timeit(list_comp1, number=100000))
    print(timeit.timeit(map_comp1, number=100000))

    print(timeit.timeit(list_comp2, number=100000))
    print(timeit.timeit(map_comp2, number=100000))
def centre_text(*args):
    # text = ""
    # for arg in args:
    #     text += str(arg) + "-"
    text = "-".join([str(arg) for arg in args]) # list comprehension
    text = "-".join(str(arg) for arg in args) # generator
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


def main():

    print(__file__)

    numbers = [1,2,3,4,5,6]
    squares = []
    for number in numbers:
        squares.append(number ** 2)
    
    print(squares)


    print()

    # squares2 = [number ** 2 for number in numbers]
    squares2 = [number ** 2 for number in range(1, 10)]
    print(squares2)


#____________________________________________________

    text = "what have the romans ever done for us"
    capitals = [char.upper() for char in text]
    print(capitals)

    words = [word.upper() for word in text.split(' ')]
    print(words)

    lc_words = text.split(' ')
    print(lc_words)
#____________________________________________________

    centre_text("spam and eggs")
    centre_text("spam, spam and eggs")
    centre_text(12)
    centre_text("spam, spam, spam and eggs")
    centre_text("first", "second", 3, 4, "spam")

#____________________________________________________

    # numbers = [1,2,3,4,5,6]
    # number = int(input("Please enter a number between 1 - 6, and I will tell you its square: "))
    # squares = []
    # # for number in numbers:
    # #     squares.append(number ** 2)
    # squares = [number ** 2 for number in numbers]

    # index_pos = numbers.index(number)
    # print(squares[index_pos])

#____________________________________________________










if __name__ == "__main__":
    main()
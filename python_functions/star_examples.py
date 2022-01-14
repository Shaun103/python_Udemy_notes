def test_star(*args):
    print(args)
    for x in args:
        print(x)
    




def main():
    print()

    # numbers = (0, 1, 2, 3, 4, 5)
    # number = [0, 1, 2, 3, 4, 5]

    # print(numbers)
    # print(*numbers) # unpacked sequience 
    # print(*number, sep=";")


    test_star(0, 1, 2, 3, 4, 5)
    
    print()
    test_star()


if __name__ == "__main__":
    main()
def main():



    print()

    numbers = {}
    numbers = {*{}}
    numbers = []
    numbers = set()
    numbers = {*""} # do not do this 

    # print(numbers, type(numbers)) # dictionary

    # # numbers.add(1)
    # print(numbers)

    # while len(numbers) < 4:
    #     next_value = int(input("Please enter your next value: "))
    #     numbers.add(next_value)
    # print(numbers)

#_________________________________________________________________________


    data = ["blue", "red", "blue", "green", "red", "blue", "white"]

    # create a set from a list, to remove duplicates
    unique_data = set(data)
    print(unique_data)

    print(sorted(unique_data))

    # create a list of unique colors, keeping the order they appeared in 

    unique_data = list(dict.fromkeys(data))
    print(unique_data)

    print()
    print(dict.fromkeys(data))











if __name__ == "__main__":
    main()
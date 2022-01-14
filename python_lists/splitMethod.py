def main():

    # print("ONLY WORKS WITH STRINGS")

    # panagram = """The quick brown
    #              fox jumps\tover 
    #              the laxy dog"""

    # words = panagram.split()
    # print(words)


    # numbers = "9,223,372,036,854,775,807"
    # num = numbers.split(",")
    
    # print(num)

#________________________________________________________________

    userinput = input("Please typing three numbers seperated by a coma: ")
    # print(prompt)

    strings = userinput.split(",")

    numbers = []

    for nums in strings:
        numbers.append(int(nums))
    print(numbers)
    
    a, b, c = numbers
    result = a + b - c

    print(result)

if __name__ == "__main__":
    main()
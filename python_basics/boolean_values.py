def main():


# true and false #

    print(" ")

    day = "Monday"
    temperature = 30
    raining = True     # False: for "Go swimming"

    if (day == "Saturday" and temperature > 27) or not raining:
        print("Go swimming!")
    else:
        print("Learn Python")


# truthy values #

    # if 0:
    #     print("True")
    # else:
    #     print("False")

    # name = input("Please enter your name: ")

    # if name:
    #     print("Hello, {}".format(name))
    # else:
    #     print("Are you the man with no name?")

    # if name != " ":
    #     print("Hello, {}".format(name))
    # else:
    #     print("Are you the man with no name?")


# in and not in #

    # parrot = "Norwegian Blue"
    # letter = input("Enter a character: ")

    # if letter in parrot:
    #     print("{} is in {}".format(letter, parrot))
    # else:
    #     print("I don't need that letter")


    activity  = input("What would you like to do today? ")

    if "cinema" not in activity.casefold(): 
        print("But I want to go to the cinema")



# If challenge #

    name = str(input("What is your name?"))
    age = int(input("What is your age?"))
    
    if age >= 18:
        print("Welcome to the holiday, {0}".format(name))
    else:
        print("Sorry, you cannot go on holiday")









if __name__ == "__main__":
    main()
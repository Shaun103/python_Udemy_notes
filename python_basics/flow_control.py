def main():

# # if else statements #
#     name = input("Please enter your name: ")
#     age = int(input("How old ar eyou, {0}? ".format(name)))

#     if age >= 18:
#         print("You are old enough to vote!")
#         print("Please put X in the box!")
#     else:
#         print("Please come back in {0} years".format(18 - age))

#     if age < 18:
#         print("Please come back in {0} years".format(18 - age))
#     else:
#         print("You are old enough to vote")
#         print("Please put an X in the box")

# Elif statements #

    # name = input("Please enter your name: ")
    # age = int(input("How old ar eyou, {0}? ".format(name)))

    # if age >= 18:
    #     print("You are old enough to vote!")
    # else:
    #     print("Please come back in {0} years".format(18 - age))
    #     print("Please put an X in the box")


    # if age < 18:
    #     print("Please come back in {0} years".format(18 - age))
    # elif age > 900:
    #     print("Sorry, Yoda, you die in the Return of the Jedi")
    # else:
    #     print("You are old enough to vote")
    #     print("Please put an X in the box")

# more elif statements #


    # answer = 5

    # print("Please guess a number between 1 and 10 ")
    # guess = int(input())

    # if guess > answer:
    #     print("Your guess is too high!")
    # elif guess < answer:
    #     print("You guess is too low!")
    # else:
    #     print("Winner winner chicken dinner!")

# adding a second guess #

    # answer = 5

    # print("Please guess a number between 1 and 10 ")
    # guess = int(input())

    # if guess < answer:
    #     print("Your guess is too low")
    #     guess = int(input("Please guess higher!"))
    #     if guess == answer:
    #         print("well done, you guessed it!")
    #     else:
    #         print("Sorry you have not guessed it!")
    # elif guess > answer:
    #     print("You guess is too high!")
    #     guess = int(input("Please guess lower!"))
    #     if guess == answer:
    #         print("well done, you guessed it!")
    #     else:
    #         print("Sorry you have not guessed it!")
    # else:
    #     print("Winner winner chicken dinner!")


# conditional operators #


    # if guess != answer:
    #     if guess < answer:
    #         print("Please guess higher")
    #     else: 
    #         print("Please guess lower")
    #     guess = int(input())
    #     if guess == answer: 
    #         print("Well done, you guess it!")
    #     else:
    #         print("Sorry, you have not guessed correctly")
    # else:
    #     print("You got it first time!")    


# challenge operators #

    # if guess == answer: 
    #     print("Well done, you guess it!")
    # elif guess < answer:
    #     print("Please guess higher!")
    #     print("Please guess again")
    #     guess = int(input())
    #     if guess != answer:
    #         print("You guessed incorrectly!")
    #     else:
    #         print("You guessed correctly!")
    # elif guess > answer:
    #     print("Please guess lower!")
    #     print("Please guess again")
    #     guess = int(input())
    #     if guess != answer:
    #         print("You guessed incorrectly!")
    #     else:
    #         print("You guessed correctly!")


# using and, or, in Conditions  #

    age = int(input("How old are you? "))

    # if age >= 16 and age <= 65:
    #     print("Have a good day at work!")


    if 16 <= age <= 65:
        print("Have a good day at work!")
    else:
        print("Enjoy your free time!")

    print("-" * 80)

    if age < 16 or age > 65:
        print("Enjoy your free time!")
    else:
        print("Have a good day at work!")









if __name__ == "__main__":
    main()
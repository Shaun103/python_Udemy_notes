def main():

    # for i in range(10):
    #     print("i is now {}".format(i))

    # i = 0
    # while i <= 10:
    #     print("i is now {}".format(i))
    #     i += 1


#_________________________________________________

    # available_exits = ["north", "south", "east", "west"]

    # choosen_exit = ""
    # while choosen_exit not in available_exits:
    #     choosen_exit = input("Please choose a direction: ")

    # print("aren't you glad you got out of there!")

#_________________________________________________

    # for index in range(0,21):
    #     if index % 3 == 0 or index % 5 == 0:
    #         continue
    #     print(index)


#_________________________________________________


    import random

    highest = 1000
    answer = random.randint(1,highest)
    print(answer)
    print("Please guess number between 1 and {}: ".format(highest))

    guess = 0


    while guess != answer:
        guess = int(input()) 

        if guess == 0:
            print("Breaking out of the program")
            break

        if guess == answer: 
            print("Well done, you guessed it!")
            break
        else:
            if guess < answer:
                print("Please guess higher")    
            else: 
                print("Please guess lower")          







if __name__ == "__main__":
    main()
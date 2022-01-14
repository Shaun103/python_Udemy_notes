def main():

    # will_continue = True

    # while will_continue != False:
    #     print(
    #     """
    #     Please choose you option from the list below: 
    #     1. \tLearn Python
    #     2. \tLearn Java
    #     3. \tGo swimming
    #     4. \tHave dinner
    #     5. \tGo to bed
    #     0. \tExit
    #     """
    #     )

    #     answer = int(input("Make a Selection here: "))
    #     # print(answer)
    #     if answer == 1:
    #         print("You have selected: 1")
    #         continue
    #     elif answer == 2:
    #         print("You have selected: 2")
    #         continue
    #     elif answer == 3:
    #         print("You have selected: 3")
    #         continue
    #     elif answer == 4:
    #         print("You have selected: 4")
    #         continue
    #     elif answer == 5:
    #         print("You have selected: 5")
    #         continue
    #     elif answer == 0:
    #         print("Now exiting the program...")
    #         break
    #     else:
    #         print("You have made an incorrect selection")
    #         continue

#_______________________________________________


    # print(
    # """
    # Please choose you option from the list below: 
    # 1. \tLearn Python
    # 2. \tLearn Java
    # 3. \tGo swimming
    # 4. \tHave dinner
    # 5. \tGo to bed
    # 0. \tExit
    # """
    # )

    # while True:
    #     choice = input()

    #     if choice == "0":
    #         break
    #     elif choice in "12345":
    #         print("You chose {}".format(choice))
    #     else:
    #         print(
    #         """
    #         ** Invalid statement please try again **
    #         Please choose you option from the list below: 
    #         1. \tLearn Python
    #         2. \tLearn Java
    #         3. \tGo swimming
    #         4. \tHave dinner
    #         5. \tGo to bed
    #         0. \tExit
    #         """
    #         )

#__________________________________________________________
    # choice = "-"
    # while True:
    #     if choice == "0":
    #         print("Exiting program...")
    #         break
    #     elif choice in "12345":
    #         print("You chose {}".format(choice))
    #     else:
    #         print(
    #         """
    #         Please choose you option from the list below: 
    #         1. \tLearn Python
    #         2. \tLearn Java
    #         3. \tGo swimming
    #         4. \tHave dinner
    #         5. \tGo to bed
    #         0. \tExit
    #         """
    #         )
    #     choice = input()

#__________________________________________________________

    choice = "-"
    while choice != "0":
        if choice in "12345":
            print("You chose {}".format(choice))
        else:
            print(
            """
            Please choose you option from the list below: 
            1. \tLearn Python
            2. \tLearn Java
            3. \tGo swimming
            4. \tHave dinner
            5. \tGo to bed
            0. \tExit
            """
            )

        choice = input()

if __name__ == "__main__":
    main()
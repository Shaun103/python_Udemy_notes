def main():
    
    print()

    # computer_parts = [
    #                     "computer", 
    #                     "monitor", 
    #                     "keyboard", 
    #                     "mouse", 
    #                     "mouse_pad"
    #                 ]


    # for part in computer_parts:
    #     print(part)

    # print("thrid item in list", computer_parts[2])

    # print("first three items: ",computer_parts[0:3])
    # print("last item in the list: ",computer_parts[-1])


#_______________________________________________________


    # empty_list = []

    # even = [2, 4, 6, 8]
    # odd = [1, 3, 5, 7, 9]

    # numbers = even + odd
    # print(numbers)

    # sorted_numbers = sorted(numbers) # creates a new list
    # print(sorted_numbers)

    # # digits  = sorted("432985617")
    # # print(digits)

    
    # digits  = list("432985617")
    # print(digits)

    # # more_numbers = list(numbers)
    # # more_numbers = numbers[:] # slicing list
    # more_numbers = numbers.copy() # copying the numbers list
    # print(more_numbers)
    # print(numbers is more_numbers) # not the same list
    # print(numbers == more_numbers) # lists are equal, same numbers

#_______________________________________________________


    # computer_parts = [
    #                     "computer", 
    #                     "monitor", 
    #                     "keyboard", 
    #                     "mouse", 
    #                     "mouse_pad"
    #                 ]

    # print(computer_parts)

    # # computer_parts[3] = "trackball"
    # print(computer_parts)

    # computer_parts[3:] = ["trackball"]

    # print(computer_parts)
    
#_______________________________________________________

    # empty_list = []

    # even = [2, 4, 6, 8]
    # odd = [1, 3, 5, 7, 9]

    # numbers = [even, odd]
    # print(numbers)

    # for number_list in numbers:
    #     print(number_list)

    #     for value in number_list:
    #         print(value)

#_______________________________________________________

    # menu = [
    #     ["eggs", "bacon"],
    #     ["eggs", "sausage","bacon"],
    #     ["eggs", "spam"],
    #     ["eggs", "bacon", "spam"],
    #     ["eggs", "sausage","bacon", "spam"],
    #     ["spam", "eggs","spam", "spam", "bacon", "spam"],
    #     ["spam", "sausage","spam", "bacon", "spam", "tomato", "spam"],
    # ]

    # for meal in menu:
    #     if "spam" not in meal:
    #         print(meal)

    #         for item in meal:
    #             print(item)

    #     else:
    #         print("{0} has a spam score of {1}".format(meal, meal.count("spam")))

if __name__ == "__main__":
    main()
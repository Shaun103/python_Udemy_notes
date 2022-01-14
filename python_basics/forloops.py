def main():
        
    # parrot = "Norwegian Blue"

    # for character in parrot:
    #     print(character)

    # number = "9,223;372:036 854,775;807" 
    # seperator = ""

    # for char in number:
    #     if not char.isnumeric():
    #         seperator = seperator + char
    
    # print(seperator)
    
    # values = "".join(char if char not in seperator else " " for char in number).split()
    # print([int(val) for val in values])

#_________________________________________________

    # number = input("Please enter a series of numbers, using any separators you like: ")
    # seperator = ""

    # for char in number:
    #     if not char.isnumeric():
    #         seperator = seperator + char
    
    # # print(seperator)

    #     values = "".join(char if char not in seperator else " " for char in number).split()
    # print(sum([int(val) for val in values]))


# extracting capitals challenge #

    # quote = """
    #         Alright, but apart from the Sanitation, the Medicine, Education, Wine,
    #         Public Order, Irrigation, Roads, the Fresh-Water System,
    #         and Public Health, what have the Romans ever done for us?
    #         """
    
    # # Use a for loop and an if statement to print just the capitals in the quote above.
    # for cap in quote:
    #     if cap.isupper():
    #         print(cap)


# range based for loops #

    # for i in range(0,10,2):
    #     print("I is now: {0}".format(i))


# reverse ranges #


    # for i in range(10,0,-2):
    #     print("I is now: {0}".format(i))


    # age = int(input("Please enter your age: "))

    # if age in range(16, 66):
    #     print("Have a good day at work")
    # else:
    #     print("Enjoy your free time")

    # print("-" * 80)

    
# nesting for loops #


    # for i in range(1, 13):
    #     for j in range(1, 13):
    #         print("{0} times {1} is {2}".format(j, i, i*j))
    #     print("-" * 30)

    
# continue #

    shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

    # for item in shopping_list:
    #     print("Buy {0}".format(item))

    # for item in shopping_list:
    #     if item != "spam":
    #         print("Buy " + item)


    # for item in shopping_list:
    #     if item == "spam":
    #         continue
    #     print("Buy " + item)


# Searching #

    # item_to_find = "spam"
    # found_at = None  # no value

    # for index in range(len(shopping_list)):
    #     if shopping_list[index] == item_to_find:
    #         found_at = index
    #         break
    
    # print("Item found at position: {}".format(found_at))


# if item is not in the list #


    # item_to_find = "albatross"
    item_to_find = "spam"
    found_at = None  # no value

    # for index in range(len(shopping_list)):
    #     if shopping_list[index] == item_to_find:
    #         found_at = index
    #         break

    if item_to_find in shopping_list:
        found_at = shopping_list.index(item_to_find)
        
    if found_at is not None:
        print("Item found at position: {}".format(found_at))
    else:
        print("{} not found".format(item_to_find))







if __name__ == "__main__":
    main()
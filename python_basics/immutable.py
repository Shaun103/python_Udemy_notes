def main():


    # result = True

    # another_result = result

    # print(id(result))
    # print(id(another_result))


    # result = False
    # print(id(result))


    # result = "Correct"
    # another_result = result
    # print(id(result))
    # print(id(another_result))

    # result += "ish"
    # print(id(result))

    # print(id(another_result))


#______________________________________________

    shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

    another_list = shopping_list

    print(id(shopping_list))
    print(id(another_list))

    shopping_list += ["cookies"] # adding cookies to list 
    print(shopping_list)
    print(id(shopping_list))

if __name__ == "__main__":
    main()
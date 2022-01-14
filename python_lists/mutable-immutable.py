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


    print(another_list)


    a = b  = c = d = e = f = another_list

    print(a)
    print(b)

    print("adding cream")
    b.append("cream")
    print(a)
    print(c)
    print(d)

#______________________________________________

    even = [2,4,6,8]
    odd = [1,3,5,7,9]

    print("Min: ")
    print(min(even))
    print(min(odd))

    print("Max: ")
    print(max(even))
    print(max(odd))

    print()
    print(len(even))
    print(len(odd))

    print("number of 's in Mississippi")
    print("Mississippi".count("issi"))

#______________________________________________












if __name__ == "__main__":
    main()
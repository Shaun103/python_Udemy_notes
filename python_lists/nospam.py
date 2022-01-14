def main():
    menu = [
        ["eggs", "bacon"],
        ["eggs", "sausage","bacon"],
        ["eggs", "spam"],
        ["eggs", "bacon", "spam"],
        ["eggs", "sausage","bacon", "spam"],
        ["spam", "eggs","spam", "spam", "bacon", "spam"],
        ["spam", "sausage","spam", "bacon", "spam", "tomato", "spam"],
    ]

#______________________________________________________________________

    # one solution

    for meal in menu:
        for index in range(len(meal) -1, -1, -1):
            if meal[index] == "spam":
                del meal[index]
        
        print(meal)

    # second solution 

    for meal in menu:
        for item in meal:
            if item != "spam":
                print(item, end=" ")
        print()



            

if __name__ == "__main__":
    main()
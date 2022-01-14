










def main():
    print()

    menu = [
        ["egg", "bacon"],
        ["egg", "sausage", "bacon"],
        ["egg", "spam"],
        ["egg", "bacon", "spam"],
        ["spam", "egg", "sausage", "bacon", "spam"],
        ["spam","egg", "sausage", "bacon", "chips"],
        ["spam","egg", "spam", "spam", "bacon", "spam"],
        ["spam","egg", "sausage", "bacon"],
        ["chicken", "chips"],
    ]

    # meals = []
    # for meal in menu:
    #     if "spam" not in meal:
    #         meals.append(meal)            
    #     else:
    #         meals.append("a meal was skipped")
    # print(meals)

    # # meals = [meal for meal in menu if "spam" not in meal if "chicken" not in meal]
    # meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
    # print(meals)


    # #_____________________________________________________________________________________

    # # similar ways of doing the same thing

    # print()
    # fussy_meals = [meal for meal in menu if "spam" in meal or "egg" in meal if not ("bacon" in meal and "sausage" in meal)]
    # print(fussy_meals)

    # fussy_meals = [meal for meal in menu if ("spam" in meal or "egg" in meal) and not ("bacon" in meal and "sausage" in meal)] 
    # print(fussy_meals)


    #_____________________________________________________________________________________

    # dealing with else in list comprehension

    # meals = []
    # for meal in menu:
    #     if "spam" not in meal:
    #         meals.append(meal)
    #     else:
    #         meals.append("a meal was skipped")
    # print(meals)


    # print()
    # meals = [meal if "spam" not in meal else "a meal skipped" for meal in menu]
    # print(meals)


    # # conditional expression 
    # x = 12
    # expression = "Twelve " if x == 12 else "unknown"
    # print(expression)

    #_____________________________________________________________________________________



    for meal in menu:
        print(meal, "contains sausage" if "chicken" in meal else "contains bacon" if "bacon" in meal else "contains eggs")

    print()

    items = set()
    for meal in menu:
        for item in meal:
            items.add(item)
    print(items)
    print()


#_____________________________________________________________________________________

    print("next line")
    for meal in menu:
        for item in items:
            if item in meal:
                print(f"{meal} contains {item}")
                break

    
#_____________________________________________________________________________________

# challenge portion

    # for x in range(1, 31):
    #     fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
    #     print(fizzbuzz)

    # print()

    fizzbuzz = ["fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x) 
                    for x in range(1,31)]
    print(fizzbuzz)

    for buzz in fizzbuzz:
        print(buzz.center(12, '*'))
    





if __name__ == "__main__":
    main()
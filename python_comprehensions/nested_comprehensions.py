def main():
    print()

    burgers = ["beef", "chicken", "spicy bean"]
    toppings = ["cheese", "egg", "beans", "spam"]
    
    # two methods for doing the same thing
    print()
    meals = [(burger, topping) for burger in burgers for topping in toppings]
    print(meals)

    print()
    for meals in [(burger, topping) for burger in burgers for topping in toppings]:
        print(meals)
        
    #_____________________________________________________________________________

    # print()
    # for burger in burgers:
    #     for topping in toppings:
    #         print((burger,topping))

    #_____________________________________________________________________________

    # [] make four list of tuples
    print()
    for meals in [[(burgers, toppings) for burger in burgers] for topping in toppings]:
        print(meals)

    print()
    # # keeping the order to output the same as each other
    for nested_meals in [[(burger, topping) for topping in toppings] for burger in burgers]:
        print(nested_meals)

#_____________________________________________________________________________

    # challenge 

    # EXAMPLE
    print()
    for i in range(1, 11):
        for j in range(1, 11):
            print(i, j * j)

#_____________________________________________________________________________

    print()
    answer = [[(i, i*j ) for i in range(1, 11) for j in range(1, 11)]]
    print(answer)

#_____________________________________________________________________________

    print()
    for answer in [[(i, i*j) for i in range(1, 11) for j in range(1, 11)]]:
        print(answer)

#_____________________________________________________________________________

    # prints the same as the EXAMPLE for loop
    print()
    for x, y in [(i, i*j) for i in range(1, 11) for j in range(1, 11)]:
        print(x,y)

#_____________________________________________________________________________
    
    # generator method
    # uses generator: less memory usage
    # performence suffers
    for x, y in ((i, i*j) for i in range(1, 11) for j in range(1, 11)):
        print(x,y)



if __name__ == "__main__":
    main()
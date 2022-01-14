import shelve 

def main():
    print()


    # cannot shelve a dictionary

    # with shelve.open('ShelfTest') as fruit:
    #     fruit = {
    #         'orange': "a sweet citrus fruit",
    #         'apple': "good for making cider",
    #         'lemon': "a sour, yellow citrus fruit",
    #         'grape': "a small, sweet fruit growing in bunches",
    #         'lime': "a sour, green citrus fruit",
    #     }

    
    # print(fruit["lemon"])
    # print(fruit["grape"])

    # print(fruit)

#____________________________________________________________________________

    # file closes on its own 

    # with shelve.open('ShelfTest') as fruit:
    #     fruit['orange'] = "a sweet citrus fruit"
    #     fruit['apple'] = "good for making cider"
    #     fruit['lemon'] = "a sour, yellow citrus fruit"
    #     fruit['grape'] = "a small, sweet fruit growing in bunches"
    #     fruit['lime'] = "a sour, green citrus fruit"


    # print(fruit["lemon"])
    # print(fruit["grape"])

    # fruit["Lime"] = "great with tequila"
    

    # for snack in fruit:
    #     print(snack + ": " + fruit[snack])

    # print(fruit)


#____________________________________________________________________________

    # closing the file manually

    # fruit = shelve.open('ShelveTest')
    # fruit['orange'] = "a sweet citrus fruit"
    # fruit['apple'] = "good for making cider"
    # fruit['lemon'] = "a sour, yellow citrus fruit"
    # fruit['grape'] = "a small, sweet fruit growing in bunches"
    # fruit['lime'] = "a sour, green citrus fruit"

    # print(fruit["lemon"])
    # print(fruit["grape"])

    # fruit["Lime"] = "great with tequila"
    

    # for snack in fruit:
    #     print(snack + ": " + fruit[snack])

    # fruit.close()

    # print(fruit)

#____________________________________________________________________


    fruit = shelve.open('ShelveTest')
    fruit['orange'] = "a sweet citrus fruit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow citrus fruit"
    fruit['grape'] = "a small, sweet fruit growing in bunches"
    fruit['lime'] = "a sour, green citrus fruit"

    # looping through the dictionary 

    while True:
        dict_key = input("Please enter a fruit: ")
        if dict_key == "quit":
            print("quiting program")
            break

        if dict_key in fruit:
            description = fruit[dict_key]
            print(description)
        else:
            print(f"We dont have a {dict_key}")

# _____________________________________________________________________


    # # ordering the dictionary by name
    
    # order_keys = list(fruit.keys())
    # order_keys.sort()

    # # for f in fruit:
    # for f in order_keys:
    #     print(f + f" - {fruit[f]}")


# _____________________________________________________________________

    # grabbing the items and values: similar to keys and values in dictionaries

    # for v in fruit.values():
    #     print(v)

    # print(fruit.values())

    # for f in fruit.items():
    #     print(f)

    # print(fruit.items())


    # fruit.close()







if __name__ == "__main__":
    main()
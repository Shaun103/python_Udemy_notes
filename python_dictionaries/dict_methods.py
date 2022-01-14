def main():
    print()

    d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "iv": "four"
}

    pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

    # new_dict = dict.fromkeys(pantry_items, 0)   # create an initial dictionary 
    # print(new_dict)

    keys = d.keys()
    # print(keys)

    # for item in d.keys():
    #     print(item)


#____________________________________________________________________________

    # information to update d with d2 information
    d2 = {
        7: "lucky seven",
        10: "ten",
        3: "This is the new three"
    }


    # d.update(d2)
    # for key, value in d.items():
    #     print(key,value)

    # print()

    # d.update(enumerate(pantry_items))
    # for key, value in d.items():
    #     print(key, value)


#____________________________________________________________________________

    # v = d.values()
    # print(v)

    # d[10] = "ten"
    # print(v)


    # print("four" in v)
    # print("eleven" in v)


    # # copies the keys and values - less efficient 
    # # only finds the first occurence
    # keys = list(d.keys())
    # values = list(v)
    # if "four" in values:
    #     index = values.index("four")
    #     key = keys[index]
    #     print(f"d[key] was found with the key {key}")

    # print()

    # # more efficient 
    # for key, value in d.items():
    #     if value == "four":
    #         print(f"d[key] was found with the key {key}")

#____________________________________________________________________________

    animals = {
        "Lion": ["Scary", "big", "cat"],
        "Elephant":["Big", "grey", "wrinkled"],
        "Teddy":["Cuddly", "stuffed"],
    }

    things = animals.copy()     # creates two seperate dictionaries
    # animals["Teddy"] = "toy"
    
    print(things["Teddy"])
    print(animals["Teddy"])

    things["Teddy"].append("toy")

    print(things["Teddy"])
    print(animals["Teddy"])












if __name__ == "__main__":
    main()
def main():
    print()


    # small_ints = set(range(21))
    # print(small_ints)

    # # clear all of the items from the set
    # # small_ints.clear()
    # # print(small_ints)

    # small_ints.discard(10)
    # small_ints.remove(11)
    # print(small_ints)

    # small_ints.discard(99) # number not in the set
    # print(small_ints)

    # # small_ints.remove(99)   # error number not in set crashes program 
    # # print(small_ints)

#________________________________________________________________________________

travel_mode = {"1": "car", "2": "plane"}

items = {
    "can opener",
    "fuel",
    "jumper",
    "knife",
    "matches",
    "razor blades",
    "razor",
    "scissors",
    "shampoo",
    "shaving cream",
    "shirts (3)",
    "shorts",
    "sleeping bag(s)",
    "soap",
    "socks (3 pairs)",
    "stove",
    "tent",
    "mug",
    "toothbrush",
    "toothpaste",
    "towel",
    "underwear (3 pairs)",
    "water carrier",
}

restricted_items = {
    "catapult",
    "fuel",
    "gun",
    "knife",
    "razor blades",
    "scissors",
    "shampoo",
}

print("Please choose your mode of travel:")
for key, value in travel_mode.items():
    print(f"{key}: {value}")
    # Python 3.5 and earlier
    # print("{}: {}".format(key, value))

mode = "-"
while mode not in travel_mode:
    mode = input("> ")

if mode == "2":
    for retricted_item in restricted_items:
        items.discard(retricted_item)
    

# print the packing list
print("You need to pack:")
for item in sorted(items):
    print(item)











if __name__ == "__main__":
    main()
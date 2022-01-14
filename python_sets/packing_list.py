


def main():
    print()

    # travel_mode = {"1": "car", "2": "plane"}

    # items = {
    #     "can opener",
    #     "fuel",
    #     "jumper",
    #     "knife",
    #     "matches",
    #     "razor blades",
    #     "razor",
    #     "scissors",
    #     "shampoo",
    #     "shaving cream",
    #     "shirts (3)",
    #     "shorts",
    #     "sleeping bag(s)",
    #     "soap",
    #     "socks (3 pairs)",
    #     "stove",
    #     "tent",
    #     "mug",
    #     "toothbrush",
    #     "toothpaste",
    #     "towel",
    #     "underwear (3 pairs)",
    #     "water carrier",
    # }

    # restricted_items = {
    #     "catapult",
    #     "fuel",
    #     "gun",
    #     "knife",
    #     "razor blades",
    #     "scissors",
    #     "shampoo",
    # }

    # print("Please choose your mode of travel:")
    # for key, value in travel_mode.items():
    #     print(f"{key}: {value}")
    #     # Python 3.5 and earlier
    #     # print("{}: {}".format(key, value))

    # mode = "-"
    # while mode not in travel_mode:
    #     mode = input("> ")

    # if mode == "2":
    #     # travelling by plane, remove restricted items
    #     # for restricted_item in restricted_items:
    #     #     # remove will give an error here
    #     #     items.discard(restricted_item)
    #     # items -= restricted_items
    #     items.difference_update(restricted_items)

    # # print the packing list
    # print("You need to pack:")
    # for item in sorted(items):
    #     print(item)

#_______________________________________________________________________________

    # finds all of the items that are not found in baskets from favourites

    favourites = {'door screen',
              'frying pan',
              'roller blind',
              'football',
              'coffee grinder',
              'bush hat',
              'stirling engine',
              'cachemira cd',
              'shirt',
              }

    basket = {'garlic crusher',
            'stirling engine',
            'frying pan',
            'shirt',
            'bush hat',
            }

    suggestions = sorted(favourites - basket)

    print(suggestions)



if __name__ == "__main__":
    main()
# https://docs.python.org/3/library/functions.html#open


def main():
    print()

    # write vs print

    data = [
        "Andromeda - Shrub",
        "Bellflower - Flower",
        "China Pink - Flower",
        "Daffodil - Flower",
        "Evening Primrose - Flower",
        "French Marigold - Flower",
        "Hydrangea - Shrub",
        "Iris - Flower",
        "Japanese Camellia - Shrub",
        "Lavender - Shrub",
        "Lilac- Shrub",
        "Magnolia - Shrub",
        "Peony - Shrub",
        "Queen Anne's Lace - Flower",
        "Red Hot Poker - Flower",
        "Snapdragon - Flower",
        "Sunflower - Flower",
        "Tiger Lily - Flower",
        "Witch Hazel - Shrub",
    ]

#______________________________________________________________________________

    plants_filename = "flowers_print.txt"

    with open(plants_filename, "w") as plants:
        for plant in data: 
            print(plant, file=plants)

    
    new_list = []
    with open(plants_filename) as plants:
        for plant in plants:
            new_list.append(plant.rstrip())
    

    print(new_list)

#______________________________________________________________________________

    # write vs print

    with open(plants_filename, "w") as plants:
        for plant in data:
            # plants.write(plant)
            plants.write(str(plant) + "\n") # prints on new line


    # why print and write return different results
    print(data)
    string_representation = data.__str__()
    print(type(string_representation))



    with open(plants_filename, "a") as plants:
        plants.write("\n") # blank first line 
        for plant in data:
            plants.write(plant)
            # plants.write(str(plant) + "\n") # prints on new line







if __name__ == "__main__":
    main()
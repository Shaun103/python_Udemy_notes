def main():
    print()

    lion_list = ["Scary", "big", "cat"]
    elephant_list = ["Big", "grey", "wrinkled"]
    teddy_list = ["Cuddly", "stuffed"]

    animals = {
    "Lion": lion_list,
    "Elephant": elephant_list,
    "teddy": teddy_list,
}

    # things = animals.copy()     # copies only the reference # creates two seperate dictionaries

    things = {
        "Lion": lion_list,
        "Elephant": elephant_list,
        "teddy": teddy_list,
    }
    
    print(things["teddy"])
    print(animals["teddy"])

    # things["teddy"].append("toy")

    teddy_list.append("toy")

    animals["teddy"].append("added via `animals`")
    things["teddy"].append("added via `things`")

    print(things["teddy"])
    print(animals["teddy"])
    print(teddy_list)


if __name__ == "__main__":
    main()
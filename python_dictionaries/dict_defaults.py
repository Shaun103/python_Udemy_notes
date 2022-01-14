from contents import pantry

def main():

    print()

    # set default, displays the value of the key if the item exists
    chicken_quantity = pantry.setdefault("chicken", 0)
    print(f"chicken: {chicken_quantity}")
    
    # places in list if it is not already there
    beans_quantity = pantry.setdefault("Beans: ", 0) 
    print(f"Beans: {beans_quantity}")

    # does not exist, uses the get method
    ketchup_quantity = pantry.get("ketchup", 0) 
    print(f"ketchup: {ketchup_quantity}")

    z_quantity = pantry.setdefault("zucchini", "eight")
    print(f"zucchini: {z_quantity}")

    print()
    print("`pantry` now contains: ")
    for key, value in sorted(pantry.items()):
        print(key, value)

if __name__ == "__main__":
    main()
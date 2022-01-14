from contents import pantry, recipes 


def add_shopping_item(data: dict, item:str, amount: int)-> None:
    """Add a tuple containing `item` and `amount` to the `data` dict."""

    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount

    # does the same as above
    # if the item is found in the dictionary, it adds the amount
    data[item] = data.setdefault(item, 0) + amount 


def main():
    print()

    # print(pantry)
    # print()
    # print(recipes)

    # for item in recipes:
    #     print(item)
    # 
#____________________________________________________________________


    display_dict = {}
    shopping_list = {}


    # places recipe data into `display_dict` variable
    for index, key in enumerate(recipes):
        display_dict[str(index + 1)] = key
    
    while True:
        # Display a menuu of the recipes we know how to cook
        print("Please choose your recipe")
        print("--------------------------")

        # looping over recipe dictionary to print menu  
        for key, value in display_dict.items():
            print(f"{key} - {value}")
        
        choice = input(": ")
        if choice == "0":
            break
        elif choice in display_dict:
            selected_item = display_dict[choice]
            print(f"You have selected {selected_item}")
            print("Listed ingredients: ")
            ingredients = recipes[selected_item]
            print(ingredients)
            for food_item, required_quantity in ingredients.items():
                quantity_in_pantry = pantry.get(food_item, 0)
                if required_quantity <= quantity_in_pantry:
                    print(f"\t{food_item} OK")
                else:
                    quantity_to_buy = required_quantity - quantity_in_pantry
                    print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                    add_shopping_item(shopping_list, food_item, quantity_to_buy)

    for things in shopping_list.items():
        print(things)

if __name__ == "__main__":
    main()
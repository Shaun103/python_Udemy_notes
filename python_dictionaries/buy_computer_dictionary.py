def main():
    
    print()

    available_parts = {
        "1":"Computer",
        "2":"Monitor",
        "3":"Keyboard",
        "4":"Mouse",
        "5":"HDMI Cable",
        "6":"DVD Drive",
    }


    current_choice=None
    computer_parts = {}     # creating an empty dictionary


    while current_choice != "0":
        if current_choice in available_parts:
            chosen_part = available_parts[current_choice]
            if current_choice in computer_parts:
                # it's already in so we remove it
                print(f"Removing {chosen_part}")
                computer_parts.pop(current_choice)
            else:
                print(f"Adding {chosen_part}")
                computer_parts[current_choice] = chosen_part
            print(f"You dictionary now contains: {computer_parts}")
        else:
            print("Please add options from the list: ")
            for key, value in available_parts.items():
                print(f"{key}: {value}")
            print("0: to quit ")

        current_choice = input("> ")

if __name__ == "__main__":
    main()
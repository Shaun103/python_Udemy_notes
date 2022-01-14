def main():

    # available_parts = ['computer', "monitor", "keyboard", "mouse", "mousepad", "hdmi cable", "dvd drive"]
    # current_choice = "-"
    # computer_parts = [] # creating empty list

    # while current_choice != '0':
    #     if current_choice in "123456":
    #         print("Adding {}".format(current_choice))
    #         if current_choice == '1':
    #             computer_parts.append("computer")
    #         elif current_choice == '2':
    #             computer_parts.append("monitor")
    #         elif current_choice == '3':
    #             computer_parts.append("keyboard")
    #         elif current_choice == '4':
    #             computer_parts.append("mouse")
    #         elif current_choice == '5':
    #             computer_parts.append("mousepad")
    #         elif current_choice == '6':
    #             computer_parts.append("hdmi cable")
    #     else:
    #         print("Please add otpions from the list below: ")
    #         # has to look up each item in a list
    #         for part in available_parts:
    #             print("{0}: {1}".format(available_parts.index(part) + 1, part))

    #     current_choice = input()


#______________________________________________________________________

    # available_parts = ['computer', "monitor", "keyboard", "mouse", "hdmi cable", "dvd drive"]
    # current_choice = "-"
    # computer_parts = [] # creating empty list
    # #valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
    
    # valid_choices = []
    # for i in range(1, len(available_parts) +1):
    #     valid_choices.append(str(i))
    
    # print(valid_choices)


    # while current_choice != '0':
    #     if current_choice in valid_choices:
    #         print("Adding {} to the list".format(current_choice))
    #         index = int(current_choice) -1
    #         chosen_part = available_parts[index]
    #         computer_parts.append(chosen_part)
    #     else:
    #         print("Please add otpions from the list below: ")
    #         for number, part in enumerate(available_parts):
    #             print("{0}: {1}".format(number +  1, part))

    #     current_choice = input()

    # print(computer_parts)

#______________________________________________________________________

    # available_parts = ['computer', "monitor", "keyboard", "mouse", "hdmi cable", "dvd drive"]
    # current_choice = "-"
    # computer_parts = [] # creating empty list
    # #valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
    
    # valid_choices = []
    # for i in range(1, len(available_parts) +1):
    #     valid_choices.append(str(i))
    
    # print(valid_choices)


    # while current_choice != '0':
    #     if current_choice in valid_choices:
    #         print("Adding {} to the list".format(current_choice))
    #         index = int(current_choice) -1
    #         chosen_part = available_parts[index]
    #         computer_parts.append(chosen_part)
    #     else:
    #         print("Please add otpions from the list below: ")
    #         for number, part in enumerate(available_parts):
    #             print("{0}: {1}".format(number +  1, part))

    #     current_choice = input()

    # print(computer_parts)

#_____________________________________________________________

# adding and removing - FINISHED

    available_parts = ['computer', "monitor", "keyboard", "mouse", "hdmi cable", "dvd drive"]
    current_choice = "-"
    computer_parts = [] # creating empty list
    
    valid_choices = []

    # adds items from the list to valid_choices
    for i in range(1, len(available_parts) +1):
        valid_choices.append(str(i))
    
    # print(valid_choices) # debugging purposes 

    while current_choice != '0':
        if current_choice in valid_choices:
            index = int(current_choice) - 1
            chosen_part = available_parts[index]
            if chosen_part in computer_parts:
                # it's already in, so remove it
                print("Removing {}".format(current_choice))
                computer_parts.remove(chosen_part)
            else:
                print("Adding {}".format(current_choice))
                computer_parts.append(chosen_part)
            print("your list now contains: {}".format(computer_parts))
        else:
            print("Please add otpions from the list below: ")
            for number, part in enumerate(available_parts):
                print("{0}: {1}".format(number + 1, part)) # number + 1: starts list from 1

        current_choice = input()

    print(computer_parts)

#_____________________________________________________________

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
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

for plant in data:
    if "Flower" in plant:
        flowers.append(plant)
    if "Shrub" in  plant: 
        shrubs.append(plant)

for item in flowers:
    print("Flowers: ", item)

for item in shrubs:
    print("Shrubs", item)

if __name__ == "__main__":
    main()
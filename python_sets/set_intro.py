

def main():
    print()

    # farm_animals = {'cow', 'sheep', 'hen', 'horse', 'goat'}
    # print(farm_animals)

    # for animal in farm_animals:
    #     print(animal)

    # print()
    # print("indexing a sequence")
    # animal_list = ['cow', 'sheep', 'hen', 'goat', 'horse']
    # goat = animal_list[3]
    # print(goat)

    # # error
    # # print("Indexing a set is not possible")
    # # goat = farm_animals[3]
    # # print(goat)


    # more_animals = {'sheep', 'goat', 'cow', 'horse', 'hen'}

    # if more_animals == farm_animals:
    #     print('the sets are equal')
    # else:
    #     print('The sets are different')

#________________________________________________________________________


choice = "-"  # initialise choice to something invalid
while choice != "0":
    if choice in {"1", "2", "3", "4", "5"}:
    # if choice in set("12345"):
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()

#________________________________________________________________________






if __name__ == "__main__":
    main()
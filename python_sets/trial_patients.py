def main():
    print()


    # trial_1 = {"Bob", "Charley", "Georgia", "John"}
    # trial_2 = {"Anne", "Charley", "Eddie", "Georgia"}

    # check_set = trial_1.intersection(trial_2)
    # print(check_set)


    # farm_animals = {"Sheep", "hen", "cow", "horse", "goat"}
    # wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
    # potential_rides = {"donkey", "horse", "camel"}

    # intersection = farm_animals & wild_animals & potential_rides
    # print(intersection)
    

    # mounts = farm_animals.intersection(wild_animals, potential_rides)
    # print(mounts)

#_________________________________________________________________________


    text = """Education is not the learning of facts
    but the training of the mind to think

    - Albert Einstein"""

    prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

    # Add your code here.
    words = text.split()

    preps_used = prepositions.intersection(words)
    print(preps_used)

    # or

    preps_used = set(words).intersection(prepositions)
    print(preps_used)


    # preps_used = prepositions.intersection(lists)
    # print(preps_used)

if __name__ == "__main__":
    main()
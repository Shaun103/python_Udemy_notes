from prescription_data import adverse_interactions


def main():
    print()

    # farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
    # wild_animals = {'lion', 'elephant', 'tiger', 'goat', 'panther', 'horse'}

    # all_animals_1 = farm_animals.union(wild_animals)
    # print(all_animals_1)

    # all_animals_2 = wild_animals.union(farm_animals)
    # print(all_animals_2)

    # all_animals_3 = wild_animals | farm_animals
    # print(all_animals_3)

#______________________________________________________________________________________

    meds_to_watch = set()

    # creates a new set each time around the loop 
    for interaction in adverse_interactions: 
        # meds_to_watch = meds_to_watch.union(interaction)
        # meds_to_watch = meds_to_watch | interaction
        # meds_to_watch.update(interaction)
        meds_to_watch |= interaction

    print(sorted(meds_to_watch))

#______________________________________________________________________________________


    meds_to_watch = set()

    meds_to_watch.update(*adverse_interactions)
    print(sorted(meds_to_watch))
    print(*sorted(meds_to_watch), sep='\n')

#______________________________________________________________________________________


    # scorpions = {"emperor", "red claw", "arizona", "forest", "fat tail"}
    # snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
    # spiders = {"tarantula", "black widow", "wolf spider", "crab spider"}
    # vespas = {"yellowjacket", "hornet", "paper wasp"}

    # things_that_bite = snakes.union(spiders)
    # # things_that_bite = snakes | spiders
    # things_that_sting = scorpions | vespas
    # # things_that_sting = scorpions.union(vespas)

    # arachnids = scorpions | spiders
    # # arachnids = scorpions.union(spiders)

#______________________________________________________________________________________














if __name__ == "__main__":
    main()
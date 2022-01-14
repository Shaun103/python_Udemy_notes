from named_tuples import people, basic_plants_list, plants_list, plants_dict


def main():
    print()

    # people = []
    if bool(people) and all([person[1] for person in people]):
        print("Sending email")
    else:
        print("User must edit the list of the recipients")

#_________________________________________________________________________

    
    if any([plant.plant_type == "Grass" for plant in plants_list]):
        print("This pack contains grass")
    else:
        print("No grasses in this pack")
#_________________________________________________________________________


    if any(plant.plant_type == "Grass" for plant in plants_dict.values()):
        print("This dict contains grasses")
    else:
        print("No grasses in the dict")
    

    if any(plants_dict[key].plant_type == "Cactus" for key in plants_dict):
        print("This dict contains grasses")
    else:
        print("No cactii in the dict")


if __name__ == "__main__":
    main()
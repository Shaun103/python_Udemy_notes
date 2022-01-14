# Create a comprehension that returns a list of all the locations that have an exit to the forest.
# The list should contain the description of each location, if it's possible to get to the forest from there.
#
# The forest is location 5 in the locations dictionary
# The exits for each location are represented by the exits dictionary.
#
# Remember that a dictionary has a .values() method, to return a list of the values.
#
# The forest can be reached from the road, and the hill; so those should be the descriptions that appear in your list.
#
# Test your program with different destinations (such as 1 for the road) to make sure it works.
#
# Once it's working, modify the program so that the comprehension returns a list of tuples.
# Each tuple consists of the location number and the description.
#
# Finally, wrap your comprehension in a for loop, and print the lists of all the locations that lead to each of the
# other locations in turn.
# In other words, use a for loop to run the comprehension for each of the keys in the locations dictionary.
 

def main():

    locations = {0: "You are sitting in front of a computer learning Python",
                1: "You are standing at the end of a road before a small brick building",
                2: "You are at the top of a hill",
                3: "You are inside a building, a well house for a small stream",
                4: "You are in a valley beside a stream",
                5: "You are in the forest"
    }
    
    exits = {0: {"Q": 0},
            1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
            2: {"N": 5, "Q": 0},
            3: {"W": 1, "Q": 0},
            4: {"N": 1, "W": 2, "Q": 0},
            5: {"W": 2, "S": 1, "Q": 0}
    }

    # displays all of the choices given a location 
    
    loc = 2 # starting position 
    forest = [locations[xit] for xit in exits if loc in exits[xit].values()]
    print(forest)

    # displaying both the number and position
    print()
    forest = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()] 
    print(forest)

# #__________________________________________________________________________________

    print()
    # displays what is at the location
    loc = 3 
    forest = [locations[exit] for exit in exits if loc in exits[exit].values()]
    print(forest)

    forest = []
    for x in exits:
        if loc in exits[x].values():
            forest.append(locations[x])
    print(forest)

# #__________________________________________________________________________________

    # going through every possible path 
    # and locations
    print()
    for loc in sorted(locations):
        forest = [(x, locations[x]) for x in exits if loc in exits[x].values()]
        print(f"Locations leading to {loc}", end = '\t')
        print(forest)

# #__________________________________________________________________________________

    print()
    for loc in sorted(locations):
        forest = []
        for xit in exits:
            if loc in exits[xit].values():
                forest.append((xit, locations[xit]))
        print(f"Locations leading to {loc}", end = '\t')
        print(forest)


if __name__ == "__main__":
    main()
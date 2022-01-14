def main():
    print()


    morning1 = {'Java', 'C', 'Ruby', 'Lisp', 'C#'}
    afternoon1 = {'Python', 'C#', 'Java', 'C', 'Ruby'}

    morning = ['Java', 'C', 'Ruby', 'Lisp', 'C#']
    afternoon = ['Python', 'C#', 'Java', 'C', 'Ruby']

    # the difference between the two sets 
    possible_courses = morning1 ^ afternoon1 
    print(possible_courses)

    possible_courses = set(morning).symmetric_difference(afternoon)
    print(possible_courses)

    possible_courses = set(afternoon).symmetric_difference(morning)
    print(possible_courses)


    animals = {'Turtle',
                'Horse',
                'Robin',
                'Swallow',
                'Hedgehog',
                'Wren',
                'Aardvark',
                'Cat'}

    birds = {'Robin', 'Swallow', 'Wren'}

    print(f"birds is a subset of animals: {birds.issubset(animals)}")
    print(f'animals is a superset of birds: {animals.issuperset(birds)}')
    print(f'birds is a superset of animals: {birds.issuperset(animals)}')

    print(birds <= animals) # 
    print(birds < animals)  #  
    print('*' * 80)

    garden_birds = {'Swallow', 'Wren', 'Robin'}
    
    print(garden_birds == birds)    # proper subset
    print(garden_birds <= birds)    # subset
    print(garden_birds < birds)     # proper subset - subset in the same subset

    print('*' * 80)

    more_birds = {'Wren', 'Budgie', 'Swallow'}
    print(garden_birds >= more_birds)
    





if __name__ == "__main__":
    main()
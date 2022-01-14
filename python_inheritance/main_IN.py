# import player_IN
from player_IN import Player
from enemy import Enemy, Troll, Vampire, VampireKing



def main():
    print()

# # testing the player class

    #tim = player.Player("Tim")

    tim = Player("Tim")

#     print(tim.name)
#     print(tim.lives)
#     tim.lives -= 1
#     print(tim)

#     tim.lives -= 1
#     print(tim)

#     tim.lives -= 1
#     print(tim)

#     tim._lives = 9
#     print(tim)

#     tim.level = 1 
#     print(tim)

#     tim.level += 2
#     print(tim)

#     tim.level = 3
#     print(tim)

#     tim.score = 500
#     print(tim)
#____________________________________________________

# testing the enemy class 
    
    
    random_monster = Enemy("Basic enemy", 12, 1)

    print(random_monster)

    random_monster.take_damage(4)
    print(random_monster)

    random_monster.take_damage(8)
    print(random_monster)

    random_monster.take_damage(9)
    print(random_monster)

#____________________________________________________

    print()
    ugly_troll = Troll("Pug")
    print(f"Ugly troll - {ugly_troll}")

    another_troll = Troll("Ug")
    print(f"Another troll - {another_troll}")

    brother_troll = Troll("Urg")
    print(f"Brother troll {brother_troll}")


#____________________________________________________

    ugly_troll.grunt()

    another_troll.grunt()

    brother_troll.grunt()

    # # Error, Enemy does not has this part of the class
    # monster = Enemy("Basic enemy")
    # monster.grunt()


#____________________________________________________

    dracula = Vampire("Dracula")

    print("Vampire instance", dracula)
    # dracula.take_damage(5)
    # print(dracula)

    print("-"*40)

    # another_troll.take_damage(40)
    # print(another_troll)


    # while dracula.alive:
    #     dracula.take_damage(1)
    #     print(dracula)


    # print("-"*40)
    # while dracula.alive:
    #     if not dracula.dodges():
    #         dracula.take_damage(1)
    #         print(dracula)



    # dracula.lives = 0
    # dracula.hit_points = 1
    # print(dracula)

#_________________________________________________________

    vampKing = VampireKing("King_Vlad")
    print(vampKing)
    vampKing.take_damage(12)
    print(vampKing)


    while vampKing._alive:
        vampKing.take_damage(50)
        print(vampKing)




if __name__ == "__main__":
    main()
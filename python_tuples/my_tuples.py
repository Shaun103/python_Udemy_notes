def main():
    
    # t = ("a", "b", "c")
    # print(t)

    # name = "Tim"
    # age = 10
    # print(name, age, "Python", 2020)
    # print((name, age, "Python", 2020))  # assigning as tuple 

    welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
    bad = "Bad Company", "Bad Company", 1974
    budgie = "Nightflight", "Budgie", 1981
    imedla = "More Mayhem", "Emilda May", 2011
    metallica = "Ride the Lightning", "Metallica", 1984

    # print("Metallica: ",metallica)

    # print(metallica[0])
    # print(metallica[1])
    # print(metallica[2])

    # # metallica[0] = "Master of Puppets"  # will create an error

    # metallica2 = list(metallica)
    # print(metallica2)


    # metallica2[0] = "Master of puppets"
    # print(metallica2)

#________________________________________________________________________

# tuple unpacking 

    # print()
    
    # a = b = c = d = e = f = 42

    # print(c)

    # x, y, z = 1, 2, 76  # unpacking

    # print(x, y, z)
    # print(x)
    # print(y)
    # print(z)

    # print("Unpacking a tuple: ")
    # data = 1, 2, 76 
    # x, y, z = data
    # print(x)
    # print(y)
    # print(z)

    # print("Unpacking lists: ")
    # data_list = [12, 13, 14]
    
    # # data_list.append(15) # Error: adding too many arguments
    
    # p, q, r = data_list
    # print(p)
    # print(q)
    # print(r)

#________________________________________________________________

# Practical uses tuple unpacking

# for index, character in enumerate("abcdegh"): # shorthand of below
#     print(index, character)

    # for t in enumerate("abcdefgh"): # longer versions of above
    #     index, character = t
    #     print(index, character)

    # index, character = (0, 'a')
    # print(index)
    # print(character)

#________________________________________________________________

# tuple unpacking nameing conventions 
 
    # title, artist, year = metallica 

    # print(title)
    # print(artist)
    # print(year)

    # table = ("coffee table", 200, 100, 75, 34.50)

    # # print(table[1] * table[2]) #

    # name, length, width, height, price = table # assigning values from table

    # print(length * width)

#______________________________________________________________________

# nested tuples and lists 

    # list contains 5 tuples

    # albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
    #     ("Bad Company", "Bad Company", 1974),
    #     ("Nightflight", "Budgie", 1981),
    #     ("More Mayhem", "Emilda May", 2011),
    #     ("Ride the Lightning", "Metallica", 1984),
    # ]

    # print(len(albums))

    # for album in albums:
    #     print("Album {}, Artist: {}, Year: {}".format(album[0], album[1], album[2]))


    # more efficient 
    # for name, artist, year in albums:
    #     print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))


    # # can still refer to the original tuple: not as efficient
    # for album in albums:
    #     name, artist, year = album
    #     print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))

#______________________________________________________________________

# nested data structures 

    albums = [
        ("Welcome to my Nightmare", "Alice Cooper", 1975,
        [
            (1, "Welcome to my Nightmare"),
            (2, "Devil's Food"),
            (3, "The Black Widow"),
            (4, "Some Folks"),
            (5, "Only Women Bleed"),
        ]
        ),
        ("Bad Company", "Bad Company", 1974,
        [
            (1, "Can't Get Enough"),
            (2, "Rock Steady"),
            (3, "Ready for Love"),
            (4, "Don't Let Me Down"),
            (5, "Bad Company"),
            (6, "The Way I Choose"),
            (7, "Movin' On"),
            (8, "Seagull"),
        ]
        ),
        ("Nightflight", "Budgie", 1981,
        [
            (1, "I Turned to Stone"),
            (2, "Keeping a Rendezvous"),
            (3, "Reaper of the Glory"),
            (4, "She Used Me Up"),
        ]
        ),
        ("More Mayhem", "Imelda May", 2011,
        [
            (1, "Pulling the Rug"),
            (2, "Psycho"),
            (3, "Mayhem"),
            (4, "Kentish Town Waltz"),
        ]
        ),
    ]


    for name, artists, year, songs in albums:
        print("Album: {}, Artists: {}, Year: {}, Songs: {}".format(name, artists, year,songs))

    print()

    album = albums[3] # 2nd data in list: 
    print(album)

    print()

    songs = album[3] # 3rd item in list: LIST OF SONGS
    print(songs)

    song = songs[2] # individual song
    # print(song)
    print(song[1]) # song name 


    # all in one go 
    mayhem = albums[3][3][2][1]
    print(mayhem)

    print()

    print("1",albums[3])                # all information - 2nd album
    print("2",albums[3][3])             # song lists
    print("3",albums[3][3][2])          # individual track and song name
    print("4",albums[3][3][2][1])       # name of song

#______________________________________________________________________

    print()
    print(albums[1][3][5][1])   # second album, list of songs, 6th track, track name
    print(albums[2][2])         # third album, year release
    print(albums[2][3][3][0])   # third album, list of songs, 4th track, track number
    print(albums[2][3][1])   # third album, lists of songs, 2nd track, track name

    print()

if __name__ == "__main__":
    main()
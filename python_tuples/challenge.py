from album_data import albums

def main():
    
    # print(albums)

    # CONSTANTS
    SONGS_LISTS_INDEX = 3
    SONG_TITLE_INDEX = 1

    while True:
        print("Please choose your album (invalid choice exits):")
        for index, (title, artist, year, songs) in enumerate(albums):
            print("{}: {}".format(index + 1, title))
        
        # print()
        # # _____code does the same as above _____ # #
        # for index, value in enumerate(albums):    
        #     title, artist, year, songs = value
        #     print(index, title, artist, year, songs)

        choice = int(input())
        if 1 <= choice <= len(albums):
            songs_list = albums[choice -1][SONGS_LISTS_INDEX]
        else:
            break
    
        # debugging code
        # print(albums[choice - 1])
        # print(songs_lists)
        # print()

        print("Please choose your song:")
        for index, (track_number, song) in enumerate(songs_list):
            print("{}: {}".format(index + 1, song))

        song_choice = int(input())
        if 1 <= song_choice <= len(songs_list):
            title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
            print("Playing {}".format(title))
        print("=" * 40)

if __name__ == "__main__":
    main()
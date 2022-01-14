import os 
import fnmatch

# searching but not filtering what we are looking for
# 1 
def find_albums1(root, artist_name):
    for path, directory, files in os.walk(root):
        for artist in directory:
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


# specificly looking for a file in directory 
# 2
def find_albums2(root, artist_name):
    for path, directory, files in os.walk(root):
        for artist in fnmatch.filter(directory, artist_name):  # for loop to specifically look for what we want
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album)


def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]): # we want the path, not the name of the album
            yield song


def main():
    print()

    # # file path - what we are looking for 
    album_list = find_albums1("/Users/User/Desktop/Python_Udemy/python_generators/music", "Aerosmith")
    album_list2 = find_albums2("/Users/User/Desktop/Python_Udemy/python_generators/music", "Bla*")
    # album_list = find_albums("/Users/User/Desktop/Python_Udemy/python_generators/music", "Bla*")
    
#______________________________________________________________

    # 2 
    # prints out every directory in path
    for a in album_list2:
        print(a[67:])
        print(a[57:])

#______________________________________________________________

    # 1
    # loops through every word from selected folder
    # uses the first def
    song_list = find_songs(album_list)
    for s in song_list:
        print(s)


if __name__ == "__main__":
    main()
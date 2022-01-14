import os 
import fnmatch
import id3reader_p3 as id3reader


# specificly looking for a file in directory
# start: file path
# extension: file_extension 
def find_music(start, extension):
    for path, directories, files, in os.walk(start):
        for file in fnmatch.filter(files, f'*.{extension}'):
            yield file
            # absolute_path = os.path.abspath(path)       # creating absolute path
            # yield os.path.join(path, file)              # use it in yield values


def main():
    print()

    # path and file type searched
    my_music_files = find_music('/Users/User/Desktop/Python_Udemy/python_generators/music', 'emp3')

#____________________________________________________

    # prints out every directory in path 
    for f in my_music_files:
        print(f)

#____________________________________________________

    # error_list = []
    
    # # prints out every directory in path 
    # for f in my_music_files:
    #     try:
    #         id3r = id3reader.Reader(f)
    #         print(f"Artists: {id3r.get_value('performer')}, \
    #             Albums: {id3r.get_value('album')}, \
    #             Track: {id3r.get_value('track')}, \
    #             Song: {id3r.get_value('title')}")
    #     except:
    #         error_list.append(f)
    

    # # displaying the errors
    # for error in error_list:
    #     print(error)


if __name__ == "__main__":
    main()
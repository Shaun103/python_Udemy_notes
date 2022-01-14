import os 


def main():
    print("Hello World!")


    root = "/Users/User/Desktop/Python_Udemy/python_generators/music"

    for path, directories, files in os.walk(root, topdown=True):

        print(directories)  # prints all directories 
        print(files)        # displays all files in diretory
        input()             # you can manually walk through the directory
        for f in files:     # loops through the files
            print(f"\t {f}")

        # if files:
        #     print(path)
        #     first_split = os.path.split(path)
        #     print(first_split)
        #     second_split = os.path.split(first_split[0])
        #     print(second_split)
        #     for f in files:
        #         song_details = f[:-5].split(' - ')
        #         print(song_details)
        #     print("*" * 40)


if __name__ == "__main__":
    main()
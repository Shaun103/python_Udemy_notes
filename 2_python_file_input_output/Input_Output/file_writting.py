def main():
    print()

    cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]
    path = '\\Users\\User\\Desktop\\Python_Udemy\\2_python_file_input_output\\cities.txt'

    # with open(path, 'w') as city_file:
    #     for city in cities:
    #         print(city, file=city_file, flush=True) # print data to a file immediately 
    #         print("\n")
    #         # city_file.write(str(city))
    #         # city_file.write("\n")

#_________________________________________________

    cities = []
    jabjab = '\\Users\\User\\Desktop\\Python_Udemy\\2_python_file_input_output\\cities.txt'

    # with open(jabjab, 'r') as city_file:
    #     for city in city_file:
    #         cities.append(city.strip('\n')) # strips whitespace at the end 
    
    # print(cities)
    # for city in cities:
    #     print(city)

#_________________________________________________

    path = '\\Users\\User\\Desktop\\Python_Udemy\\2_python_file_input_output\\imelda3.txt'

    # what is being printed
    imelda = "More Mayhem","Imedla May","2011",((1, "Pulling the Ring"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

    # writing to file
    with open(path, 'w') as imelda_file:
        print(imelda, file=imelda_file)

    # reading from that file 
    with open(path, 'r') as imelda_file:
        contents = imelda_file.readline() # reads larger files 
    imelda = eval(contents) #

    # print(imelda)

    # labels each column in imelda
    title, artist, year, tracks = imelda

    print(title)
    print(artist)
    print(year)
    print(tracks)

#_________________________________________________

# chellenge

    jabber1 = '\\Users\\User\\Desktop\\Python_Udemy\\2_python_file_input_output\\sample.txt'

    # # appending to the file
    # with open(jabber1, 'a') as table:
    #     for i in range(1, 13):
    #         print(f"{i} times 2 is {i * 2}", file=table)
    #     print('-' * 20, file=table)


if __name__ == "__main__":
    main()
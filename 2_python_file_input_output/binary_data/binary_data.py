from pickle import DEFAULT_PROTOCOL


def main():
    print()

    file = '\\Users\\User\\Desktop\\Python_Udemy\\2_python_file_input_output\\binary_data\\binary'


    # with open("binary", 'bw') as bin_file:
    #     # for i in range(17):
    #     #     bin_file.write(bytes([i]))
    #     bin_file.write(bytes(range(17)))

    # with open("binary", 'br') as binfile:
    #     for b in binfile:
    #         print(b)


#____________________________________________________________________

    file = '\\Users\\User\\Desktop\\Python_Udemy\\2_python_file_input_output\\binary_data\\binary2'

    # a = 65534   # FF FE
    # b = 65535   # FF FF
    # c = 65536   # 00 01 00 00 
    # x = 2998302 # 02 2D C0 1E

    # with open(file, 'bw') as bin_file:
    #     bin_file.write(a.to_bytes(2, 'big'))
    #     bin_file.write(b.to_bytes(2, 'big'))
    #     bin_file.write(c.to_bytes(4, 'big'))
    #     bin_file.write(x.to_bytes(4, 'big'))
    #     bin_file.write(x.to_bytes(4, 'little'))

    # with open(file, 'br') as bin_file:
    #     e = int.from_bytes(bin_file.read(2), 'big')
    #     print(e)
    #     f = int.from_bytes(bin_file.read(2), 'big')
    #     print(f)
    #     g = int.from_bytes(bin_file.read(4), 'big')
    #     print(g)
    #     h = int.from_bytes(bin_file.read(4), 'big')
    #     print(h)
    #     i = int.from_bytes(bin_file.read(4), 'big')
    #     print(i)
        
#____________________________________________________________________

    # Pickle

    import pickle

    file = '\\Users\\User\\Desktop\\Python_Udemy\\2_python_file_input_output\\binary_data\\imelda.pickle'

    # imelda = ('More Mayhem',
    #             'Imelda May',
    #             '2011',
    #             ((1, 'Pulling the Rug'),
    #             (2, 'Psycho'),
    #             (3, 'Mayhem'),
    #             (4, 'Kentish Town Waltz')))

    # with open(file, "wb") as pickle_file:
    #     pickle.dump(imelda, pickle_file)

#____________________________________________________________________

    # reading the data from the binary file

    # with open(file, "rb") as imelda_pickled:
    #     imelda2 = pickle.load(imelda_pickled)
    
    # print(imelda2)

    # album, artist, year, track_list = imelda2

    # print(album)
    # print(artist)
    # print(year)
    # for track in track_list:
    #     track_number, track_title = track
    #     print(track_number, track_title)

#____________________________________________________________________

    imelda = ('More Mayhem',
                'Imelda May',
                '2011',
                ((1, 'Pulling the Rug'),
                (2, 'Psycho'),
                (3, 'Mayhem'),
                (4, 'Kentish Town Waltz')))
    
    even = list(range(0, 10, 2))
    odd = list(range(1, 11, 2))

    # writting to a binary file
    with open(file, "wb") as pickle_file:
        pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
        pickle.dump(even, pickle_file, protocol=0)
        pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
        pickle.dump(2999302, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)

    # reading from the binar file
    with open(file, "rb") as imelda_pickled:
        imelda2 = pickle.load(imelda_pickled)
        even_list = pickle.load(imelda_pickled)
        odd_list = pickle.load(imelda_pickled)
        x = pickle.load(imelda_pickled)
    
    print(imelda2)

    album, artist, year, track_list = imelda2

    print(album)
    print(artist)
    print(year)

    # prints everything in list
    for track in track_list:
        track_number, track_title = track
        print(track_number, track_title)

    print('=' * 40)
    for i in even_list:
        print(i)

    
    print('=' * 40)
    for i in odd_list:
        print(i)


    print('=' * 40)
    print(x)

#____________________________________________________________________

    # deletes the binary file
    # pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")














if __name__ == "__main__":
    main()
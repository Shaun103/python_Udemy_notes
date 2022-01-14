def main():
    

    data = [4,5,104,105,110,120,130,130,150,
            160,170,183,185,187,188,191,350,360]

    # del data[0:2]
    # print(data)
    
    # del data[16:] # the lines changed
    # del data[14:]


    # print(data)

    min_valid = 100
    max_valid = 200


#__________________________________________________________


    # for index, value in enumerate(data): # loop does not delete 350  because size change
    #     if (value < min_valid) or (value > max_valid):
    #         del data[index]
    
    # print(data)
#__________________________________________________________

    # # process low values in list

    # stop = 0
    # for index, value in enumerate(data):
    #     if value >= min_valid:
    #         stop = index
    #         break

    # print(stop)
    # del data[:stop]
    # print(data)

    # # process high values in list 

    # start = 0
    # for index in range(len(data)- 1, -1,-1):
    #     # print(index)
    #     if data[index] <= max_valid:
    #         # we have the index of the last item to keep
    #         # set 'start' to the position of the frist 
    #         # item to delete, which is 1 after 'index'
    #         start = index + 1
    #         break
    # print(start) # for debugging

    # # del data[start + 1:]
    # del data[start:]
    # print(data)

#__________________________________________________________

    # iterating backwards

    # data = [4,5,104,105,110,120,130,130,150,
    #     160,170,183,185,187,188,191,350,360]

    data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]

    min_valid = 100
    max_valid = 200

    # for index in range(len(data) -1, -1, -1):
    #     if data[index] < min_valid or data[index] > max_valid:
    #         print(index, data)
    #         del data[index]
    # print(data)

#__________________________________________________________

    # reverse function - backwards 

    top_index = len(data) - 1
    for index, value in enumerate(reversed(data)):
        if value < min_valid or value > max_valid:
            print(top_index - index, value)
            del data[top_index - index]
    print(data)

#__________________________________________________________


if __name__ == "__main__":
    main()
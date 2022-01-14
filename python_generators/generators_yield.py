import sys 


def my_range(n: int) -> None:
    start = 0
    print("my_range starts")
    while start < n:
        # generator - returns the yield value then enters suspended state
        print(f"my_range is returning {start}")
        yield start
        start += 1


def main():
    print()


    big_range = range(5)
    # big_range = my_range(5)
    

    # print(next(big_range))
    print(f"big rang is: {sys.getsizeof(big_range)} bytes ")

    # create list containing  all the values in big_range
    big_list = []
    


    for val in big_range:
        # makes the program wait for user input
        # _ = input("line 32 - inside loop") 
        big_list.append(val)
    
    print(f"big_list is {sys.getsizeof(big_list)} bytes")
    print(big_range)
    print(big_list)

    print("...looping again ... or not")

    # generators do no return the values
    for i in big_range:
        print(f"i is {i}")

    print()
    
    # for i in my_range(5):
    #     print(f"i is {i}")
    



#_______________________________________________________________


    






if __name__ == "__main__":
    main()
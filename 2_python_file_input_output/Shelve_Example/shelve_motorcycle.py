import shelve


def main():
    print()

    # with shelve.open("bike") as bike:
    #     bike["make"] = "Honda"
    #     bike["model"] = "250 Dream"
    #     bike["color"] = "red"
    #     bike["engine_size"] = 250

    #     print(bike["engine_size"])
    #     print(bike["color"])


#____________________________________________________________

    # dealing with typos

    with shelve.open("bike2") as bike:
        bike["make"] = "Honda"
        bike["model"] = "250 Dream"
        bike["color"] = "red"
        bike["engine_size"] = 250

        # del bike['engin_size'] # deleting typo

        for key in bike:
            print(key)
        
        print('='*40)

        print(bike["engine_size"])
        # print(bike["engin_size"])    # debugging typo
        print(bike["color"])


if __name__ == "__main__":
    main()
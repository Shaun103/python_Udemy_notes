import shelve


def main():
    print()

    # books = { 
    #     "recipes": {"bit": ["bacon", "lettuce", "tomato", "bread"], 
    #     "beans_on_toast": ["beans", "bread"],
    #     "scrambled eggs": ["eggs", "butter", "milk"],
    #     "soup": ["tin of soup"],
    #     "pasta" : ["pasta", "cheese"]},
    # "maintenance": {"stuck": ["oil"], "loose": ["gaffer tape"]}}

    # print(books["recipes"]["soup"])
    # print(books["recipes"]["scrambled eggs"])
    # print(books["maintenance"]["loose"])



#__________________________________________________________________________________

    # Converting to shelve

    books = shelve.open("books")

    books["recipes"] = {
        "blt": ["bacon", "lettuce", "tomato", "bread"], 
        "beans_on_toast": ["beans", "bread"],
        "scrambled eggs": ["eggs", "butter", "milk"],
        "soup": ["tin of soup"],
        "pasta" : ["pasta", "cheese"]}  #, watch out for commas - no additional commas 
    books["maintenance"] = {"stuck": ["oil"], "loose": ["gaffer tape"]}


    # print(books["recipes"]["soup"])
    # print(books["recipes"]["scrambled eggs"])
    # print(books["maintenance"]["loose"])


    print(books["recipes"]["blt"])

    books.close()

#__________________________________________________________________________________

    


if __name__ == "__main__":
    main()
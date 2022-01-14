def main():
    print("ONLY WORKS WITH STRINGS")

    menu = [
        ["eggs", "bacon"],
        ["eggs", "sausage","bacon"],
        ["eggs", "spam"],
        ["eggs", "bacon", "spam"],
        ["eggs", "sausage","bacon", "spam"],
        ["spam", "eggs","spam", "spam", "bacon", "spam"],
        ["spam", "sausage","spam", "bacon", "spam", "tomato", "spam"],
    ]

    for meal in menu:
        for index in range(len(meal) -1, -1, -1):
            if meal[index] == "spam":
                del meal[index]

    print(", ".join(meal))
    
#_______________________________________________________

    flowers = [
        "Daffodill",
        "Evening Primrose",
        "Hydrangea",
        "Iris",
        "Lavender",
        "Sunflower",
        "Tiger Lily",
    ]

    for flower in flowers:
        print(flower)

    # seperator = " | "
    seperator = ", "
    output = seperator.join(flowers)
    print(output)

    print(", ".join(flowers)) # similar as the top 

if __name__ == "__main__":
    main()
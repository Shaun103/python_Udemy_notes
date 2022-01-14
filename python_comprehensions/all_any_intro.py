









def main():
    print()


    entries = [1, 2, 3, 4, 5]

    print(f"Iterable with a 'True' value: ")

    print(f"All: {all(entries)}")
    print(f"Any: {any(entries)}")

    print(f"Iterable with a 'False' value: ")
    
    entries_with_zero = [1, 2, 0, 4, 5]
    print(f"All: {all(entries_with_zero)}")
    print(f"Any: {any(entries_with_zero)}")


# views zero as false, returns false for all of the others 

    print()
    print("Values interpreted as False in Python")
    print("""False: {0}
    None: {1}
    0: {2}
    0.0: {3}
    empty list []: {4}
    empty tuple (): {5}
    empty string '': {6}
    empty string "": {7}
    empty mapping {{}}: {8}
    """.format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))

#______________________________________________________________________________________________


    print("-" * 80)


    name = ""
    # name = "Tim"


    if name:
        print(f"Hello: {name}")
    else:
        print("Welcome, person with no name")


#______________________________________________________________________________________________


    entries = []

    if entries:
        print(f"all: {entries}")
    else:
        print(False)
    print(f"any: {any(entries)}")
    
    result = bool(entries) and all(entries)
    print(result)








if __name__ == "__main__":
    main()
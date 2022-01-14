from simple_deepcopy import my_deepcopy
import copy

def main():
    
    print()

    # original copy
    original = {
        "Tim": ["Buchalka", ["Programmer", "Teacher"]],
        "J-P": ["Roberts", ["Programmer", "Teacher"]],
    }

    # shallow copy 
    copy_1 = copy.deepcopy(original)
    
    # deepcopy
    copy_2 = my_deepcopy(original)

    # manipulates ONLY with the originals list
    original["Tim"].append("Australia")
    original["J-P"].append("Uk")

    # manipulating original copy 
    original["Tim"][1].append("Cashier")
    jp_list = original["J-P"]
    jp_list[1].append("Courier")

    print(original)
    print(copy_1)
    print(copy_2)

if __name__ == "__main__":
    main()
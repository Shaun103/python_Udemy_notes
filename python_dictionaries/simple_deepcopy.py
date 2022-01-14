import copy 
from contents import recipes

def my_deepcopy(d: dict) -> dict:
    new_dict = {}
    for key, value in d.items():
        new_value = value.copy()
        new_dict[key] = new_value

    return new_dict


def main():
    print()

# perform shallow copy 

lion_list = ["Scary", "big", "cat"]
elephant_list = ["Big", "grey", "wrinkled"]
teddy_list = ["Cuddly", "stuffed"]

animals = {
"Lion": lion_list,
"Elephant": elephant_list,
"teddy": teddy_list,
}

# things = animals.copy()     # copies only the reference # creates two seperate dictionaries

# things = {
#     "Lion": lion_list,
#     "Elephant": elephant_list,
#     "teddy": teddy_list,
# }

# print(things["teddy"])
# print(animals["teddy"])

# # things["teddy"].append("toy")

# teddy_list.append("toy")

# animals["teddy"].append("added via `animals`")
# things["teddy"].append("added via `things`")

# print(things["teddy"])
# print(animals["teddy"])

#_________________________________________________________________



# preform deepcopy 

# things = copy.deepcopy(animals)

# print(id(things["teddy"]), things["teddy"])
# print(id(animals["teddy"]), animals["teddy"])

# print()

# things["teddy"].append("toy")
# print(things["teddy"])
# print(animals["teddy"])


#_________________________________________________________________


recipes_copy = my_deepcopy(recipes)

recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])



if __name__ == "__main__":
    main()
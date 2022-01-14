import shelve
import builtins
import pandas
import random


d = dir()
print(d)

# print(dir(__builtins__))

# for n in dir(__builtins__):
    # print(n)

# print()
# print(dir(shelve))


for n in dir(shelve):
    print(n)


print()

for obj in dir(shelve.Shelf):
    if obj[0] != '_':
        print(obj)

# shelve.Shelf.

help(random)


def main():
    print()


        
if __name__ == "__main__":
    main()
from __future__ import division # python 2


def average(*args):
    print(type(args))
    print(f"args is {args}")
    print(f"*args is", *args)
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


def build_tuple(*args):
    return args

def small_num(*args):
    min = list[0]
    big  = list[0]
    for arg in args:
        if arg < min:
            small = arg
        elif arg > big:
            big = arg
        
    print(small)
    print(big) 


def main():
    print()

    print(average(1,2,3,4))


    # result1 = build_tuple(1,2,3,4,5,6)
    # result2 = build_tuple("Hello", "planet", "earth", "take", "me", "to", "the", "moon")

    # print(result1)
    # print(result2)

    
    # small_num(63,67,2,7,3,1,7,23,2,54,885,21,1,0)




if __name__ == "__main__":
    main()
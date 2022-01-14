def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:....{}, {}".format(p1, p2))
    print("var-positional (*args):...{}".format(args))
    print("keyword:..................{}".format(k))
    print("var-keyword:..............{}".format(kwargs))


def sum_numbers(*args):
    print(args)
    
    answer = 0
    for num in args:
        answer += num
    print(answer)


def main():
    print()

    func(1, 2, 3, 4, 5, 9, k=6, key1=7, key2=8)

    # error # 
    # func(1, 2, 3, 4, 5, 9, 6, key1=7, key2=8) # no k argument

    sum_numbers(1,2,3)

if __name__ == "__main__":
    main()
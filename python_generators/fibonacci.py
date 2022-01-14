
def fibinacci():
    current, previous = 0, 1
    while True:
        yield current 
        current, previous = current + previous, current


# def odd_num(n: int) -> None:
#     odd_item = range(n)
#     for i in odd_item:
#         if i % 3 == 0:
#             print(i)


def oddNumbers():
    n = 1
    while True:
        yield n 
        n += 2


def pi_series():
    odds = oddNumbers()
    approximation = 0 
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


def main():
    print()


    # a = 2
    # b = 3

    # print(f"a is {a}, b is {b}")

    # a, b = 3, 2, # b, a

    # # temp = a 
    # # a = b
    # # b = temp

    # print(f"a is {a}, b is {b}")

#__________________________________________


    # fib = fibinacci()

    # print(next(fib))
    # print(next(fib))
    # print(next(fib))
    # print(next(fib))
    # print(next(fib))
    # print(next(fib))
    # print(next(fib))
    # print(next(fib))
    # print(next(fib))
    # print(next(fib))
    # print(next(fib))
    # print(next(fib))
    # print(next(fib))
    # print(next(fib))
    # print(next(fib))
    # print(next(fib))
    # print(next(fib))
    # print(next(fib))
    # print(next(fib))
    # print(next(fib))
    # print(next(fib))
    
#__________________________________________

    odds = oddNumbers()

    # test generator
    for i in range(6):
        print(next(odds))

#__________________________________________

    # approx_pi = pi_series()

    # for x in range(10):
    #     print(next(approx_pi))

#__________________________________________











if __name__ == "__main__":
    main()
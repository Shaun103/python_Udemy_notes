# In the section on Functions, we looked at 2 different ways to calculate the factorial
# of a number.  We used an iterative approach, and also used a recursive function.
#
# This challenge is to use the timeit module to see which performs better.
#
# The two functions appear below.
#
# Hint: change the number of iterations to 1,000 or 10,000.  The default
# of one million will take a long time to run.
 
import timeit
from statistics import mean, stdev
 
# fact_test = """\
# def fact(n):
#     result = 1
#     if n > 1:
#         for f in range(2, n + 1):
#             result *= f
#     return result

# x = fact(130)
# """ 


# factorial_test = """\
# def factorial(n):
#     # n! can also be defined as n * (n-1)!
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)    

# y = factorial(130)
# """





# result = timeit.timeit(fact_test, number=1000)
# result2 = timeit.timeit(factorial_test, number=1000)


# print(f"Fact     :{result}")
# print(f"Factorial:{result2}")

#_________________________________________________________________



# def fact(n):
#     result = 1
#     if n > 1:
#         for f in range(2, n + 1):
#             result *= f
#     return result


# def factorial(n):
#     # n! can also be defined as n * (n-1)!
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)    


# if __name__=="__main__":
#     print(timeit.timeit("x = fact(130)", setup="from __main__ import fact", number=10000))
#     print(timeit.timeit("x = factorial(130)", setup="from __main__ import factorial", number=10000))


#_________________________________________________________________


def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)    


if __name__=="__main__":
    list_1 = timeit.repeat("x = fact(130)", setup="from __main__ import fact", number=10000, repeat=6)
    list_2 = timeit.repeat("x = factorial(130)", setup="from __main__ import factorial", number=10000, repeat=6)

    # print(sum(list_1))
    # print(sum(list_2))

    print("Mean: ", mean(list_1), "Standard dev: ", stdev(list_1))
    print("Mean:", mean(list_2), "Standard dev: ", stdev(list_2))
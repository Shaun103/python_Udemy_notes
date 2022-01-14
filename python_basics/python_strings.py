def main():

#   Python slicing    #
    
    
    # print("")
    # letters = "abcdefghijklmnopqrstuvwxyz"
    # letters2 = ""
    # backwards = letters[::-1]
    # print(backwards)
    # print(letters[4::-1])
    # print(letters[:-9:-1])
    # print("last four letters: ", letters[-4:])
    # print("last item in the string", letters[-1:])
    # print(": ", letters2[:1])

#   python joining strings    #


    # computer_parts = "monitor"

    # string1 = "he's "
    # string2 = "probably "
    # string3 = "pining "
    # string4 = "for the "
    # string5 = "fjords "

    # print( string1 + string2 + string3 + string4 + string5)
    
    # print("He's " "probably " "pining " "for the " "fjords")

    # print("Hello " * 5)


    # today = "Friday"

    # print("day" in today) # True
    # print("fri" in today)
    # print("thur" in today)
    # print("parrot" in "fjord") 

#    python string replacements    #

    # age = 24

    # print("My age is " + str(age) + " years")

    # print("My age is {0} years".format(age))

    # print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

    # print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dec".format(31))

    # print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May {2}, Jun: {1}, Jul: {2}, Sep {1}, Oct: {2}".format(28, 30, 31))

    # print("""
    #     Jan: {2}
    #     Feb: {0}
    #     Mar: {2} 
    #     Apr: {1} 
    #     May  {2} 
    #     Jun: {1} 
    #     Jul: {2} 
    #     Sept {1} 
    #     Oct: {2}
    #     Nov: {1}
    #     Dec: {2} 
    # """.format(28, 30, 31))



    # for i in range(1, 13):
    #     print("No. {0} squared is {1} and cubed is {2}".format(i, i**2, i**3))

    # for i in range(1, 13):
    #     num = i 
    #     squared = i**2
    #     cubed = i**3
    #     print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(num, squared, cubed))

    # for i in range(1, 13):
    #     print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i**2, i**3))

    # for i in range(1, 13):
    #     print("No. {0:2} squared is {1:<4} and cubed is {2:^4}".format(i, i**2, i**3))


#  precision out put #

    # print("Pi is approximately {0:12}".format(22/7))
    # print("Pi is approximately {0:12f}".format(22/7))
    # print("Pi is approximately {0:12.50}".format(22/7))
    # print("Pi is approximately {0:52.50f}".format(22/7))
    # print("Pi is approximately {0:62.50}".format(22/7))
    # print("Pi is approximately {0:72.50f}".format(22/7))
    # print("Pi is approximately {0:<72.50f}".format(22/7))
    # print("Pi is approximately {0:<72.54f}".format(22/7))


    for i in range(1, 13):
        print("No. {} squared is {} and cubed is {:3}".format(i, i**2, i**3))


# f - strings   #

#     age = 24
#     name = "John"

#     print(name + f" is  {age} years old")
#     print(f"Pi is approximately {22 / 7:12.50f}")
#     pi = 22 / 7
#     print(f"Pi is approximately {pi:12.50f}")



# # Python 2 string formating #

#     print("My age is %d years" % age)


#     major = "years"
#     minor = "months"
#     print("My age is %d %s, %d %s" % (age, major, 6, minor))
#     print("PI is approximately %f" % (22/7))
#     print("PI is approximately %60.50f" % (22/7))




#     print(45 - 15 / 3)


if __name__ == "__main__":
    main()
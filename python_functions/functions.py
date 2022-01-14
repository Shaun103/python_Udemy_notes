def multiply(x:float,y:float) -> float:
    """
    Multiply 2 numbers.

    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence. If you pass 
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.

    :parm x: The first number to multiply.
    :parm y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """
    result = x * y
    return result


def is_palindrome(string: str)-> bool:
    """
    Check if a string is a palindrome.
    A palindrome is a string that reads the same forwards and backwards.

    :parm string: The string to check.
    :return: True if `string` is a palindrome, False otherwise
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome(sentence: str) -> bool:
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char 
    print(string)
    return string[::-1].casefold() == string.casefold()


def palindrome2(sentence):
    string = ""
    for char in sentence:
        if char.isalpha(): # works with numbers
            string += char 
    print(string)
    return is_palindrome(string)    # calling another function: more efficient 


def main():

    # answer = multiply(10.5,4)
    # print(answer)

    # forty_two = multiply(6,7)
    # print(forty_two)

    # for val in range(1, 5):
    #     two_times = multiply(2, val)
    #     print(two_times)

#_____________________________________________________________

    # word = input("Please enter a word to check: ")
    # if is_palindrome(word):
    #     print("'{}' is a palidrome".format(word))
    # else:
    #     print("'{}' is not a palindrome".format(word))

#_____________________________________________________________


    # word = input("Please enter a word to check: ")
    # if palindrome(word):
    #     print("'{}' is a palidrome".format(word))
    # else:
    #     print("'{}' is not a palindrome".format(word))

#_____________________________________________________________

    answer = multiply(18, 3)
    print(answer)

#_____________________________________________________________








if __name__ == "__main__":
    main()
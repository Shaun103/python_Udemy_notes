def Fizz_Buzz(index:int) -> str:
    if index % 3 == 0:
        return "fizz"
    elif index % 5 == 0:
        return "buzz"
    elif index % 3 == 0 and index % 5 == 0:
        return "fizz buzz"
    else:
        return str("{}".format(index))



# for index in range(1,101):
#     print(Fizz_Buzz(index))


input("Play Fiz_Buzz. Press ENTER to start: ")
print()

next_number = 0 

while next_number < 99:
    next_number += 1
    print(Fizz_Buzz(next_number))
    next_number += 1
    correct_answer = Fizz_Buzz(next_number)
    players_answer = input("Your go: ")
    # players_answer = correct_answer
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("well done you reached {}".format(next_number))


#_________________________________________________________

# def fizz_buzz(number: int) -> str:
#     """
#     Play Fizz buzz
 
#     :param number: The number to check.
#     :return: 'fizz' if the number is divisible by 3.
#         'buzz' if it's divisible by 5.
#         'fizz buzz' if it's divisible by both 3 and 5.
#         The number, as a string, otherwise.
#     """
#     if number % 15 == 0:
#         return "fizz buzz"
#     elif number % 3 == 0:
#         return "fizz"
#     elif number % 5 == 0:
#         return "buzz"
#     else:
#         return str(number)
 
 
# for i in range(1, 101):
#     print(fizz_buzz(i))
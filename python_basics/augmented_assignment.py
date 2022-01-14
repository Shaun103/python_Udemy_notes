def main():

    x = 23

    x += 1
    print(x)

    x -= 4
    print(x)

    x*= 5
    print(x)

    x //= 4
    print(x)

    x /= 5
    print(x)

    x **= 2
    print(x)

    x %= 5
    print(x)  

    greeting = "Good "

    greeting += " morning "
    print(greeting)

    greeting *= 5
    print(greeting)

#____________________________________

number = 5
multiplier = 8
answer = 0
 
# add your loop after this comment
for i in range(multiplier):
    answer += number
 
print(answer)





if __name__ == "__main__":
    main()
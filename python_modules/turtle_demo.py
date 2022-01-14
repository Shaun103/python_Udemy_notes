# from turtle import forward, right, left, done

from turtle import * # this is frowned upon: no idea is imported

# import turtle 

import time

def main():
    print()

    # noinspection PyUnresolveedReference

    # turtle.forward(150)
    # turtle.right(250)
    # turtle.forward(150)
    # turtle.left(500)
    # turtle.circle(75)
    
    # time.sleep(1)


    # turtle.done()
#_______________________________________________________

    done = "Well done, you have finished your drawing"

    forward(150)
    right(250)
    forward(150)
    circle(75)

    done()

    # Error 
    # print(done) # error, string is not callable

if __name__ == "__main__":
    main()
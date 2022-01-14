# https://docs.python.org/3/library/time.html

import time 

# from time import time as my_timer
from time import perf_counter as my_timer # most useful 
# from time import monotonic as my_timer # cannot go backwards
# from time import process_time as my_timer # time the cpu used on the task
import random


def main():
    print()

    print(time.gmtime(0))
    # print(time.localtime())
    # print(time.localtime(time.time()))

    # # prints the number of seconds since the epoch
    # print(time.time())

    # prints the local time, month day year
    # time_here = time.localtime()
    # print(time_here)
    # print("Year: ", time_here[0], time_here.tm_year)
    # print("Month: ", time_here[1], time_here.tm_mon)
    # print("Day: ", time_here[2], time_here.tm_mday)

#________________________________________________________________________________


    # input("Please enter to start")

    # # program waits random set of time
    # wait_time = random.randint(1, 6) 
    # time.sleep(wait_time)
    
    # start_time = my_timer()
    
    # # displays prompt to stopprogram 
    # input("Press enter to stop")

    # end_time = my_timer()

    # # displays how long it took to stop program 
    # print("Started at " + time.strftime("%X", time.localtime(start_time)))
    # print("Ended at " + time.strftime("%X", time.localtime(end_time)))

    # print(f"You reaction time was {end_time - start_time} seconds")


#________________________________________________________________________________

# time challenge 


    # x = time.monotonic()
    # y = time.perf_counter()
    # z = time.process_time()
    # a = time.time()

    
    # print("Monotonic: ",x)
    # print("Perf_counter: ", y)
    # print("Process_Time: ", z)
    # print("Time: ", a)

    x = time.get_clock_info('monotonic')
    y = time.get_clock_info('perf_counter')
    z = time.get_clock_info('process_time')
    a = time.get_clock_info('time')


    print(x)
    print(y)
    print(z)
    print(a)



if __name__ == "__main__":
    main()
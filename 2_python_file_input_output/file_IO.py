

def main():
    print()

    # readline - reads a single line from a file; returns a single string
    # readlines - reads entire file; returns a list of strings (not good for large files)
    # read - reads the entire file, and returns a string if it is a txt file; 




    # jabber = open(r'\Users\User\Desktop\Python_Udemy\file_input_output\sample.txt', 'r')
    jabber = open('\\Users\\User\Desktop\\Python_Udemy\\file_input_output\\sample.txt', 'r')
    jabber1 = '\\Users\\User\Desktop\\Python_Udemy\\file_input_output\\sample.txt'



    # reads complete line from text file

    # for line in  jabber:
    #     if "jabberwock" in line.lower():
    #         print(line, end='')
    #     # print(line, end='')
    
    # jabber.close()

#______________________________________________________________

    # # BEST WAY
    # # reads complete line from text file

    with open(jabber1, 'r') as jabber:
        for line in jabber:
            if "JAB" in line.upper():
                print(line, end='')
    print()


#_________
            # other ways a file can be read 


    # with open(jabber1, 'r') as jabber:
    #     line = jabber.readline()
    #     while line:
    #         print(line, end='')
    #         line = jabber.readline()

#___________

    # with open(jabber1, 'r') as jabber:
    #     lines = jabber.readlines()
    # # print(lines, end='')

    # for line in lines:
    #     print(line, end='')
#__________

    # with open(jabber1, 'r') as jabber:
    #     lines = jabber.readlines()
    # # print(lines, end='')

    # for line in lines[::-1]:
    #     print(line, end='')


#______________________________________________________________ 

    # # reads complete text file backwards

    # with open(jabber1, 'r') as jabber:
    #     lines = jabber.read() # read 
    # # print(lines, end='')

    # for line in lines[::-1]:  # reversed 
    #     print(line, end='')


#______________________________________________________________ 


















if __name__ == "__main__":
    main()
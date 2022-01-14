import webbrowser



def main():
    print()


    # webbrowser.open("https://www.python.org/", new=1)

    # chrome = webbrowser.get(using='google-chrome')
    # chrome.open_new_tab("https://www.python.org/")
    print()


#_________________________________________________________________


    safari = webbrowser.get(using='safari')
    safari.open_new_tab("https://www.python.org/")

    print()

#_________________________________________________________________


    # help(webbrowser)


    # for i in range(10):
    #     print(1,2,3,4,5,6,7,8,9,sep=",", end=" ")
    #     print(i)

 



if __name__ == "__main__":
    main()
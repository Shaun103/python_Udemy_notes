import shelve

def main():
    print()

    file = '\\Users\\User\\Desktop\\Python_Udemy\\recipes'

    # variables to add data into dictionaries 

    blt = ["bacon", "lettuce", "tomato", "bread"]
    beans_on_toast = ["beans", "bread"]
    scrambled_eggs = ["eggs", "butter", "milk"]
    soup = ["tin of soup"]
    pasta = ["noodles", "cheese"]

    # setting variables with data 

    with shelve.open(file) as recipes:
        recipes["blt"] = blt
        recipes["beans on toast"] = beans_on_toast
        recipes["scrambled eggs"] = scrambled_eggs
        recipes["pasta"] = pasta
        recipes["soup"] = soup
    
#_________

        # # AVOID this method
        # # incorrect way of updating information 

        # # recipes["blt"].append("butter")
        # # recipes["pasta"].append("tomato")
#_________

        # 1st method for updating dict information 

        # temp_list = recipes["blt"]
        # temp_list.append("butter")
        # recipes["blt"] = temp_list

        # temp_list = recipes["pasta"]
        # temp_list.append("tomato")
        # recipes["pasta"] = temp_list


#__________________________________________________________________

    # 2nd method for updating information
    # heavier memory usage 

    # writeback=True

    with shelve.open(file, writeback=True) as recipes:
        # appending information 
        # recipes["soup"].append("croutons") # object we are updating
        
    # reading information from dictionary 
        for snack in recipes:
            print(snack, recipes[snack])

#__________________________________________________________________













if __name__ == "__main__":
    main()
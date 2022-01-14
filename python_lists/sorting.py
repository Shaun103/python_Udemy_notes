def main():
    
    # even = [2, 4, 6, 8]
    # odd = [1, 3, 5, 7, 9]
    
    # another_even = even # copy of the even list
    # print(another_even)
    # print()
    
    # even.extend(odd) # combining the lists 
    # print(even)

    # even.sort() # sorting the combined list
    # print(even)
    
    # even.sort(reverse=True) 
    # print(even)
    # # even.reverse() # another way to reverse
    
    # print()
    # print(another_even)


#_______________________________________________________

    # pangram = "The quick brown fox jumps over the lazy dog"

    # letter = sorted(pangram)
    # print(letter)

    # numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
    # sorted_numbers = sorted(numbers) # creates new list
    # print(sorted_numbers)
    # print(numbers)

    # numbers.sort()  # changes original list
    # print(numbers)

    # # another_sorted_nmbers = numbers.sort() # returns None
    # # print(another_sorted_nmbers)
    
    # missing_letter = sorted("The quick brown fox jumps over the lazy dog")
    # print(missing_letter)

#_______________________________________________________

    pangram = "The quick brown fox jumps over the lazy dog"

    letter = sorted(pangram)
    print(letter)

    numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
    sorted_numbers = sorted(numbers) # creates new list
    print(sorted_numbers)
    print(numbers)

    numbers.sort()  # changes original list
    print(numbers)

    # another_sorted_nmbers = numbers.sort() # returns None
    # print(another_sorted_nmbers)
    
    missing_letter = sorted("The quick brown fox jumps over the lazy dog", 
                            key=str.casefold)
    print(missing_letter)

#_______________________________________________________

    names = ["Grahm", "John", "Terry", "eric", "terry", "michael"]

    names.sort(key=str.casefold)
    print(names)

if __name__ == "__main__":
    main()
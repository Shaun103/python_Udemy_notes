
def main():
    print()

    # Rewrite the following code to use a list comprehension, instead of a for loop.
    #
    # Add your solution below the loop, so that the resulting list is printed out
    # below output - that makes it easier to check that it's producing exactly
    # the same list (and avoids entering the input text twice).
    
    # text = input("Please enter your text: ")
    text = "What have the romans ever done for us!?"
    text = "the input text contain repeated words in the input"
    print("Chalenge 1: ")
    output1 = []
    for x in text.split():
        output1.append(len(x))
    output2 = [len(x) for x in text.split()]
    print(output1)
    print(output2)
    
    # type your solution here:
    
    
    # It could be useful to store the original words in the list, as well.
    # The for loop would look like this (note the extra parentheses, so
    # that we get tuples in the list):
    print("Chalenge 2: ")
    output = []
    for x in text.split():
        output.append((x, len(x)))
    output = {(x, len(x)) for x in text.split()}
    print(output)
    
    # type the corresponding comprehension here:

#_________________________________________________________________


    inch_measurement = (3, 8, 20)
    cm_measurement = [2.54 * x for x in inch_measurement]
    print(cm_measurement)

    cm_measurement = tuple([inch * 2.54 for inch in inch_measurement])

    print(cm_measurement)
if __name__ == "__main__":
    main()
import hashlib
def main():
    print()


    # print(sorted(hashlib.algorithms_guaranteed))
    # print()
    # print(sorted(hashlib.algorithms_available))


#________________________________________________________________________


    python_program = """for i in range(10):
    print(i)
    """
    print(python_program)

    original_hash = hashlib.sha256(python_program.encode('utf8'))

    # # prints the encoded values for each character
    # for b in python_program.encode('utf8'):
    #     print(b, chr(b))


    print(f"SHA256: {original_hash.hexdigest}")

    python_program += "print('code change')"
    print(python_program)

    new_hash = hashlib.sha256(python_program.encode('utf8'))
    print()
    print(f"SHA256: {new_hash.hexdigest()}")


    if new_hash.hexdigest() == original_hash.hexdigest():
        print("The code has not been changed")
    else:
        print("The code has been modified")

#________________________________________________________________________



















if __name__ == "__main__":
    main()
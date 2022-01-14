from primes_and_squares import squares_generator, primes_generator

def main():
    print()


    evens = set(range(0,50, 2))
    odds = set(range(1, 50, 2))
    print(evens)
    print(odds)

    primes = set(primes_generator(100))
    print(primes)
    squares = set(squares_generator(100))
    print(squares)

#_________________________________________________________
    
    print(odds.difference(primes))
    print(odds - primes)

    print(primes - odds)









if __name__ == "__main__":
    main()
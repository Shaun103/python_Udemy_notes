def sum_eo(n, t):

    if t == 'e':
        start = 2
    elif t == 'o':
        start = 1
    else:
        return - 1
    
    return sum(range(start,n,2))

def main():
    x = sum_eo(21, 'as')
    print(x)


if __name__ == "__main__":
    main()
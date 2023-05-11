if __name__ == '__main__':
    n = input("Enter a starting number (greater than 0) or QUIT: ")
    if n != "QUIT":
        n = int(n)
        while n != 1:
            print(n, end=', ')
            if n % 2 == 0:
                n //= 2
            else:
                n *= 3
                n += 1
        print(n)

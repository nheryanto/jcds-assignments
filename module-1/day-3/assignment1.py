if __name__ == '__main__':
    upTo = int(input("Enter a number: "))
    for number in range(1, upTo+1):
        mod_3 = number % 3
        mod_5 = number % 5
        if mod_3 == 0 and mod_5 == 0:
            print("FizzBuzz", end=' ')
        elif mod_3 == 0 and mod_5 != 0:
            print("Fizz", end=' ')
        elif mod_3 != 0 and mod_5 == 0:
            print("Buzz", end=' ')
        else:
            print(number, end=' ')
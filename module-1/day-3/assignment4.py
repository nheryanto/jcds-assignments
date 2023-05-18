if __name__ == '__main__':
    n = input("Enter the Nth Fibonacci number you wish to calculate or QUIT to quit: ")
    if n != "QUIT":
        result = ''
        n = int(n)
        if n >= 100:
            print("Number entered >= 100. It may take a while to display all Fibonacci numbers.")
        i = 0
        while i < n:
            if i == 0:
                fib_0 = 0
                result += f"{fib_0}"
            elif i == 1:
                fib_1 = 1
                result += f", {fib_1}"
            else:
                fib = fib_0 + fib_1
                result += f", {fib}"
                fib_0 = fib_1
                fib_1 = fib
            i += 1
        print(result)
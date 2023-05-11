if __name__ == '__main__':
    message = input("Enter the message to hack: ")
    #message = "QIIX QI FC XLI VSWI FYWLIW XSRMKLX."
    source = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n_key = 0
    while n_key < 26:
        print(f"Key #{n_key}: {message}")
        new_message = ''
        for i in message:
            if i.isalpha():
                new_message += source[source.index(i)-1]
            else:
                new_message += i
        message = new_message
        n_key += 1

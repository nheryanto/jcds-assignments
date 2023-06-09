def caesar_cipher(message, key):
    encription = ''
    source = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in message.upper():
        if char.isalpha():
            idx = (source.index(char) + key) % len(source)
            encription += source[idx]
        else:
            encription += char
    return encription

if __name__ == '__main__':
    #message = input("Enter a text: ")
    message = "Meet me by the rose bushes tonight."
    key = 4
    encription = caesar_cipher(message, key)
    print(encription)
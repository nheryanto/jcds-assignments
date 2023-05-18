import random

def generatePassword(length):
    if length < 12:
        length = 12

    password = []
    password.append(random.choice(LOWER_LETTERS))
    password.append(random.choice(UPPER_LETTERS))
    password.append(random.choice(NUMBERS))
    password.append(random.choice(SPECIAL))
    random.shuffle(password)

    tmp = list(LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL)
    random.shuffle(tmp)

    password.extend(random.choices(tmp, k=length-len(password)))
    random.shuffle(password)

    return ''.join(password)
    
if __name__ == '__main__':
    LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    NUMBERS = '1234567890'
    SPECIAL = '~!@#$%^&*()_+'

    password = generatePassword(8)
    hasLowerCase = False
    hasUpperCase = False
    hasNumber = False
    hasSpecial = False

    for char in password:
        if char in LOWER_LETTERS:
            hasLowerCase = True
        if char in UPPER_LETTERS:
            hasUpperCase = True
        if char in NUMBERS:
            hasNumber = True
        if char in SPECIAL:
            hasSpecial = True

    assert hasLowerCase and hasUpperCase and hasNumber and hasSpecial
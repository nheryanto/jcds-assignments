def customReverse(myList):
    for i in range(len(myList)//2):
        myList[i], myList[len(myList)-1-i] = myList[len(myList)-1-i], myList[i]
    return myList

def digitsToNumber(myList):
    return int(''.join([str(i) for i in myList]))
    #return sum([val*10**(len(myList)-1-i) for i,val in enumerate(myList)])

def numberToDigits(number):
    return [int(i) for i in str(number)]
     
def add(myList1, myList2):
    num1 = digitsToNumber(customReverse(myList1))
    num2 = digitsToNumber(customReverse(myList2))
    result = customReverse(numberToDigits(num1 + num2))
    return result

if __name__ == '__main__':
    l1 = [2,4,3]
    l2 = [5,6,4]
    print(f"{l1} + {l2} = ", end=' ')
    result = add(l1, l2)
    print(result)

    l1 = [9,4,7]
    l2 = [3,5,4]
    print(f"{l1} + {l2} = ", end=' ')
    result = add(l1, l2)
    print(result)
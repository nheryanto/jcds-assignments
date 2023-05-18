def commaFormat(number):
    # cast number into string using repr() to include decimals
    str_number = repr(number)

    # check if decimal exists, marked with '.'
    decimal = None
    if '.' in str_number:
        # separate integer and decimal parts
        str_number, decimal = str_number.split(sep='.')
        decimal = '.' + decimal

    # empty list tmp to store temporary result
    tmp = []

    # while str_number is not empty
    while str_number:
        # append last three digits in str_number to tmp
        tmp.append(str_number[-3:])
        
        # store remaining digits in str_number
        str_number = str_number[:-3]

    # reverse tmp to get original number order
    tmp.reverse()

    # concatenate each number in tmp using ',' separator
    result = ','.join(tmp)
    # concatenate decimal if it exists
    if decimal:
        result +=  decimal
        
    return result

if __name__ == '__main__':
    assert commaFormat(1) == '1'
    assert commaFormat(10) == '10'
    assert commaFormat(100) == '100'
    assert commaFormat(1000) == '1,000'
    assert commaFormat(10000) == '10,000'
    assert commaFormat(100000) == '100,000'
    assert commaFormat(1000000) == '1,000,000'
    assert commaFormat(1234567890) == '1,234,567,890'
    assert commaFormat(1000.123456) == '1,000.123456'
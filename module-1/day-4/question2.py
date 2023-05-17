def isLeapYear(year):
    result = None
    if year % 400 == 0:
        result = True
    elif year % 4 == 0 and year % 100 != 0:
        result = True
    else:
        result = False
    return(result)
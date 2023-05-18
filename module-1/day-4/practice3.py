def getChessSquareColor(column, row):
    column -= 1
    row -= 1
    
    if column in range(0,8) and row in range(0,8):
        if (column + row) % 2 == 0:
            result = 'white'
        else:
            result = 'black'
    else:
        result = ''
    
    return result

if __name__ == '__main__':
    assert getChessSquareColor(1, 1) == 'white'
    assert getChessSquareColor(2, 1) == 'black'
    assert getChessSquareColor(1, 2) == 'black'
    assert getChessSquareColor(8, 8) == 'white'
    assert getChessSquareColor(0, 8) == ''
    assert getChessSquareColor(2, 9) == ''
def printBoard(board):
    print()
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print()

def checkWin(board):
    win_condition = [
        board['top-L'] == 'X' and board['top-M'] == 'X' and board['top-R'] == 'X',
        board['mid-L'] == 'X' and board['mid-M'] == 'X' and board['mid-R'] == 'X',
        board['low-L'] == 'X' and board['low-M'] == 'X' and board['low-R'] == 'X',
        board['top-L'] == 'X' and board['mid-L'] == 'X' and board['low-L'] == 'X',
        board['top-M'] == 'X' and board['mid-M'] == 'X' and board['low-M'] == 'X',
        board['top-R'] == 'X' and board['mid-R'] == 'X' and board['low-R'] == 'X',
        board['top-L'] == 'X' and board['mid-M'] == 'X' and board['low-R'] == 'X',
        board['low-L'] == 'X' and board['mid-M'] == 'X' and board['top-R'] == 'X',

        board['top-L'] == 'O' and board['top-M'] == 'O' and board['top-R'] == 'O',
        board['mid-L'] == 'O' and board['mid-M'] == 'O' and board['mid-R'] == 'O',
        board['low-L'] == 'O' and board['low-M'] == 'O' and board['low-R'] == 'O',
        board['top-L'] == 'O' and board['mid-L'] == 'O' and board['low-L'] == 'O',
        board['top-M'] == 'O' and board['mid-M'] == 'O' and board['low-M'] == 'O',
        board['top-R'] == 'O' and board['mid-R'] == 'O' and board['low-R'] == 'O',
        board['top-L'] == 'O' and board['mid-M'] == 'O' and board['low-R'] == 'O',
        board['low-L'] == 'O' and board['mid-M'] == 'O' and board['top-R'] == 'O'
    ]

    for condition in win_condition:
        if(condition):
            return condition

def printGuide():
    print()
    print('top-L | top-M | top-R')
    print('------+-------+------')
    print('mid-L | mid-M | mid-R')
    print('------+-------+------')
    print('low-L | low-M | low-R')
    print()

def ticTacToe():
    board = {'top-L': ' ',
             'top-M': ' ',
             'top-R': ' ',
             'mid-L': ' ',
             'mid-M': ' ',
             'mid-R': ' ',
             'low-L': ' ',
             'low-M': ' ',
             'low-R': ' '}
    
    listCell = ['top-L','top-M','top-R',
                  'mid-L','mid-M','mid-R',
                  'low-L','low-M','low-R']

    val = None
    i = 0    
    while True:
        printGuide()
        key = input(f"Enter tic-tac-toe cell to fill in:\n({', '.join(listCell)})\n>> ")

        if not val:
            listVal = ['O', 'X', 'skip']
        elif val == 'O':
            listVal = ['X', 'skip']
        elif val == 'X':
            listVal = ['O', 'skip']
        
        val = input(f"Enter value ({', '.join(listVal)}):\n>> ")
        if val == 'skip':
            listVal.remove(val)
            val = listVal[0]
        elif val == 'X' or val == 'O':
            listCell.remove(key)
            board[key] = val

        printBoard(board)

        win = checkWin(board) 
        if win:
            print(f'Player {val} wins!\n')
            break
        elif all(v!=' ' for v in board.values()):
            break

        i += 1
    
if __name__ == '__main__':
    ticTacToe()
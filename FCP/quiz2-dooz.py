def move(board, column, color):
    '''
    get the board of the game and the col of move and color of the player and update the board of the game
    '''
    # check from bottom of the board
    for i in range(5,-1,-1):
        if board[i][column-1] == '0':
            board[i][column-1] = color
            return
    
    return board

def render(board):
    '''
    get the board of the game and visualize it
    '''
    for it in board :
        print(' '.join(it))

def win_check(l):
    '''
    get a list of data from game and check if there is 4 taw in a row
    output : name of the color if someone wins and 0 if not 
    '''
    if len(l) < 4 :
        return 0

    last = ''
    counter = 0
    for it in l:
        if it == last :
            counter += 1
        elif it != '0':
            last = it
            counter = 1
        else:
            last = ''
            counter = 0

        if counter == 4:
            return last

    return 0


def winner(board):
    '''
    get the board and find out who wins the game
    '''

    # check Horizontally
    for it in board:
        check = win_check(it)
        if check != 0:
            return check
        

    # check Vertically
    l = [ [ board[j][i] for j in range(6)] for i in range(7)] # transpose the list
    for it in l:
        check = win_check(it)
        if check != 0:
            return check

    # check Diagonally

     # create a list of all diagonals of the board
    import numpy as np 
    array = np.array(board)
    diagonals = [array.diagonal(i) for i in range(-5,6)]
    diagonals.extend(array[::-1,:].diagonal(i) for i in range(-5,6))
    diagonals = [it.tolist() for it in diagonals]

     # go thru the list and check each one
    for it in diagonals:
        check = win_check(it)
        if check != 0:
            return check

    


# create the board of the game
board = [ ['0' for j in range(7)] for i in range(6)]

# get the data and update the table
n = int(input())
moves = input().split()
red = True
for it in moves:
    if red:
        move(board, int(it), 'r')
        red = False
    else:
        move(board, int(it), 'y')
        red = True
    

# Display the winner and the final board
print('Winner =', winner(board))
render(board)

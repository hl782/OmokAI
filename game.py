from __future__ import print_function


def createBoard():
    board = [['_' for x in xrange(9)] for x in xrange(9)]
    return board

def createInitialMoves():
    initialMoves = set()
    for x in range(9):
        for y in range(9):
            initialMoves.add((x,y))
    return sorted(initialMoves)

def printBoard(board):
    topLine = '+---+---+---+---+---+---+---+---+---+'
    print('  0   1   2   3   4   5   6   7   8')
    print(topLine)
    for x in range(9):
        for y in range(9):
            print('|', board[x][y], end=" ")
        print('|', x)
        print(topLine)

def checkWinner(board, turn):
    if turn == True:
        player = 'O'
    else:
        player = 'X'

    #horizontal check
    for x in range(9):
        for y in range(5):
            if board[x][y] == board[x][y+1] == board[x][y+2] == board[x][y+3] == board[x][y+4] and board[x][y] == player:
                return player
    #vertical check
    for y in range(9):
        for x in range(5):
            if board[x][y] == board[x+1][y] == board[x+2][y] == board[x+3][y] == board[x+4][y] and board[x][y] == player:
                return player
    #downward diagonal check
    for x in range(5):
        for y in range(5):
            if board[x][y] == board[x+1][y+1] == board[x+2][y+2] == board[x+3][y+3] == board[x+4][y+4] and board[x][y] == player:
                return player
    #right diagonal check
    for x in range(4, 9):
        for y in range(5):
            if board[x][y] == board[x-1][y+1] == board[x-2][y+2] == board[x-3][y+3] == board[x-4][y+4] and board[x][y] == player:
                return player
    return None

def playOmok(board, turn, playerA, playerB, candidateMoves, playedMoves):
    winner = None

    while winner == None:
        printBoard(board)
        if len(candidateMoves) == 0:
            print('TIE GAME')
            winner = 'tie'
            break

        if turn == True:
            print('Move for playerA')
            playerA.move(board, candidateMoves, playedMoves, turn)
        else:
            print('Move for playerB')
            playerB.move(board, candidateMoves, playedMoves, turn)

        winner = checkWinner(board, turn)
        turn = not turn

    printBoard(board)
    if winner != None and turn == 0:
        print('Player A is the Winner!')
    elif winner != None and turn == 1:
        print('Player B is the Winner!')
    return winner

# Naive AI
# First checks to see if it can play a move to win the game. If there is such a move, plays it.
# Then checks to see if opponent has a move to win the game. If there is such a move, plays to block the opponent from winning.
# Then checks to see if it can create a situation to create a 4 in a row. If there is such a move, plays it.
# Then checks to see if opponent has a move to create a 4 in a row. If there is such a move, plays sto block the opponent from doing so.
# Then it tries to create its own 3 in a row to take initiative
# Else it plays random move.

import random

class NaiveAI:
    def __init__(self, color):
        self.color = color

        if color == 'O':
            self.antiColor = 'X'
        elif color == 'X':
            self.antiColor = 'O'


    def checkFour(self, board, checkSelf, possibleMoves):
        if checkSelf == True:
            char = self.color
        else:
            char = self.antiColor

        candidateMoves = set()
        #horizontal check
        for x in range(9):
            for y in range(6):
                if board[x][y] == board[x][y+1] == board[x][y+2] == board[x][y+3] and board[x][y] == char:
                    if (x, y-1) in possibleMoves:
                        candidateMoves.add((x, y-1))
                    if (x, y+4) in possibleMoves:
                        candidateMoves.add((x, y+4))
        #vertical check
        for y in range(9):
            for x in range(6):
                if board[x][y] == board[x+1][y] == board[x+2][y] == board[x+3][y] and board[x][y] == char:
                    if (x-1, y) in possibleMoves:
                        candidateMoves.add((x-1, y))
                    if (x+4, y) in possibleMoves:
                        candidateMoves.add((x+4, y))
        #downward diagonal check
        for x in range(6):
            for y in range(5):
                if board[x][y] == board[x+1][y+1] == board[x+2][y+2] == board[x+3][y+3] and board[x][y] == char:
                    if (x-1, y-1) in possibleMoves:
                        candidateMoves.add((x-1, y-1))
                    if (x+4, y+4) in possibleMoves:
                        candidateMoves.add((x+4, y+4))
        #right diagonal check
        for x in range(3, 9):
            for y in range(5):
                if board[x][y] == board[x-1][y+1] == board[x-2][y+2] == board[x-3][y+3] and board[x][y] == char:
                    if (x+1, y-1) in possibleMoves:
                        candidateMoves.add((x+1, y-1))
                    if (x-4, y+4) in possibleMoves:
                        candidateMoves.add((x-4, y+4))

        if len(candidateMoves) == 0:
            return False, candidateMoves
        else:
            return True, candidateMoves


    def checkThree(self, board, checkSelf, possibleMoves):
        if checkSelf == True:
            char = self.color
        else:
            char = self.antiColor

        #horizontal check
        candidateMoves = set()
        for x in range(9):
            for y in range(7):
                if board[x][y] == board[x][y+1] == board[x][y+2] and board[x][y] == char:
                    if (x, y-1) in possibleMoves:
                        candidateMoves.add((x, y-1))
                    if (x, y+3) in possibleMoves:
                        candidateMoves.add((x, y+3))
        #vertical check
        for y in range(9):
            for x in range(7):
                if board[x][y] == board[x+1][y] == board[x+2][y] and board[x][y] == char:
                    if (x-1, y) in possibleMoves:
                        candidateMoves.add((x-1, y))
                    if (x+3, y) in possibleMoves:
                        candidateMoves.add((x+3, y))
        #downward diagonal check
        for x in range(7):
            for y in range(6):
                if board[x][y] == board[x+1][y+1] == board[x+2][y+2] and board[x][y] == char:
                    if (x-1, y-1) in possibleMoves:
                        candidateMoves.add((x-1, y-1))
                    if (x+3, y+3) in possibleMoves:
                        candidateMoves.add((x+3, y+3))
        #right diagonal check
        for x in range(2, 9):
            for y in range(6):
                if board[x][y] == board[x-1][y+1] == board[x-2][y+2] and board[x][y] == char:
                    if (x+1, y-1) in possibleMoves:
                        candidateMoves.add((x+1, y-1))
                    if (x-3, y+3) in possibleMoves:
                        candidateMoves.add((x-3, y+3))
        if len(candidateMoves) == 0:
            return False, candidateMoves
        else:
            return True, candidateMoves

    def move(self, board, possibleMoves, playedMoves, turn):
        opponentHasFour, fourblockingMoves = self.checkFour(board, False, possibleMoves)
        opponentHasThree, threeblockingMoves = self.checkThree(board, False, possibleMoves)
        selfHasFour, fourAidingMoves = self.checkFour(board, True, possibleMoves)
        selfHasThree, threeAidingMoves = self.checkThree(board, True, possibleMoves)

        if selfHasFour:
            move = random.choice(list(fourAidingMoves))
            board[move[0]][move[1]] = self.color
            possibleMoves.remove(move)
            playedMoves.add(move)
        else:
            if opponentHasFour:
                move = random.choice(list(fourblockingMoves))
                board[move[0]][move[1]] = self.color
                possibleMoves.remove(move)
                playedMoves.add(move)
            elif selfHasThree:
                move = random.choice(list(threeAidingMoves))
                board[move[0]][move[1]] = self.color
                possibleMoves.remove(move)
                playedMoves.add(move)
            elif opponentHasThree:
                move = random.choice(list(threeblockingMoves))
                board[move[0]][move[1]] = self.color
                possibleMoves.remove(move)
                playedMoves.add(move)
            else:
                move = random.choice(list(possibleMoves))
                board[move[0]][move[1]] = self.color
                possibleMoves.remove(move)
                playedMoves.add(move)

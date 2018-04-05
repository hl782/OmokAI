from copy import deepcopy
from collections import Counter
from randomAI import RandomAI
from naiveAI import NaiveAI
from minimaxAI import MinimaxAI
import game
import random

class MonteCarloAI:
    def __init__(self, color):
        self.color = color
        if color == 'O':
            self.antiColor = 'X'
        elif color == 'X':
            self.antiColor = 'O'

    def generateCandidateMoves(self, board, possibleMoves, playedMoves):
        cardinalDirections = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        if len(playedMoves) == 0:
            firstMoveSet = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)]
            return [random.choice(firstMoveSet)]
        else:
            #check if a winning move exists for either side
            for move in possibleMoves:
                if self.isWinningMove(board, move, True, playedMoves) or self.isWinningMove(board, move, False, playedMoves):
                    return [move]

            candidateMoves = set()
            for move in playedMoves:
                for direction in cardinalDirections:
                    if (move[0]+direction[0], move[1]+direction[1]) in possibleMoves:
                        candidateMoves.add((move[0]+direction[0], move[1]+direction[1]))
            return candidateMoves

    def isWinningMove(self, board, move, isSelf, playedMoves):
        myChar = self.color if isSelf == True else self.antiColor
        if ((move[0], move[1]+1) in playedMoves and (move[0],move[1]+2) in playedMoves and (move[0],move[1]+3) in playedMoves and (move[0],move[1]+4) in playedMoves):
            if (board[move[0]][move[1]+1] == board[move[0]][move[1]+2] == board[move[0]][move[1]+3] == board[move[0]][move[1]+4] == myChar):
                return True
        elif ((move[0],move[1]-1) in playedMoves and (move[0],move[1]+1) in playedMoves and (move[0],move[1]+2) in playedMoves and (move[0],move[1]+3) in playedMoves):
            if (board[move[0]][move[1]-1] == board[move[0]][move[1]+1]== board[move[0]][move[1]+2]== board[move[0]][move[1]+3] == myChar):
                return True
        elif ((move[0],move[1]-2) in playedMoves and (move[0],move[1]-1) in playedMoves and (move[0],move[1]+1) in playedMoves and (move[0],move[1]+2) in playedMoves):
            if(board[move[0]][move[1]-2] == board[move[0]][move[1]-1]== board[move[0]][move[1]+1]== board[move[0]][move[1]+2] == myChar):
                return True
        elif ((move[0],move[1]-3) in playedMoves and (move[0],move[1]-2) in playedMoves and (move[0],move[1]-1) in playedMoves and (move[0],move[1]+1) in playedMoves):
            if(board[move[0]][move[1]-3] == board[move[0]][move[1]-2]== board[move[0]][move[1]-1]== board[move[0]][move[1]+1] == myChar):
                return True
        elif ((move[0],move[1]-4) in playedMoves and (move[0],move[1]-3) in playedMoves and (move[0],move[1]-2) in playedMoves and (move[0],move[1]-1) in playedMoves):
            if(board[move[0]][move[1]-4] == board[move[0]][move[1]-3]== board[move[0]][move[1]-2]== board[move[0]][move[1]-1] == myChar):
                return True
        elif ((move[0]+1,move[1]) in playedMoves and (move[0]+2,move[1]) in playedMoves and (move[0]+3,move[1]) in playedMoves and (move[0]+4,move[1]) in playedMoves):
            if(board[move[0]+1][move[1]] == board[move[0]+2][move[1]]== board[move[0]+3][move[1]]== board[move[0]+4][move[1]] == myChar):
                return True
        elif ((move[0]-1,move[1]) in playedMoves and (move[0]+1,move[1]) in playedMoves and (move[0]+2,move[1]) in playedMoves and (move[0]+3,move[1]) in playedMoves):
            if(board[move[0]-1][move[1]] == board[move[0]+1][move[1]]== board[move[0]+2][move[1]]== board[move[0]+3][move[1]] == myChar):
                return True
        elif ((move[0]-2,move[1]) in playedMoves and (move[0]-1,move[1]) in playedMoves and (move[0]+1,move[1]) in playedMoves and (move[0]+2,move[1]) in playedMoves):
            if(board[move[0]-2][move[1]] == board[move[0]-1][move[1]]== board[move[0]+1][move[1]]== board[move[0]+2][move[1]] == myChar):
                return True
        elif ((move[0]-3,move[1]) in playedMoves and (move[0]-2,move[1]) in playedMoves and (move[0]-1,move[1]) in playedMoves and (move[0]+1,move[1]) in playedMoves):
            if(board[move[0]-3][move[1]] == board[move[0]-2][move[1]]== board[move[0]-1][move[1]]== board[move[0]+1][move[1]] == myChar):
                return True
        elif ((move[0]-4,move[1]) in playedMoves and (move[0]-3,move[1]) in playedMoves and (move[0]-2,move[1]) in playedMoves and (move[0]-1,move[1]) in playedMoves):
            if(board[move[0]-4][move[1]] == board[move[0]-3][move[1]]== board[move[0]-2][move[1]]== board[move[0]-1][move[1]] == myChar):
                return True
        elif ((move[0]+1,move[1]+1) in playedMoves and (move[0]+2,move[1]+2) in playedMoves and (move[0]+3,move[1]+3) in playedMoves and (move[0]+4,move[1]+4) in playedMoves):
            if(board[move[0]+1][move[1]+1] == board[move[0]+2][move[1]+2]== board[move[0]+3][move[1]+3]== board[move[0]+4][move[1]+4] == myChar):
                return True
        elif ((move[0]-1,move[1]-1) in playedMoves and (move[0]+1,move[1]+1) in playedMoves and (move[0]+2,move[1]+2) in playedMoves and (move[0]+3,move[1]+3) in playedMoves):
            if(board[move[0]-1][move[1]-1] == board[move[0]+1][move[1]+1]== board[move[0]+2][move[1]+2]== board[move[0]+3][move[1]+3] == myChar):
                return True
        elif ((move[0]-2,move[1]-2) in playedMoves and (move[0]-1,move[1]-1) in playedMoves and (move[0]+1,move[1]+1) in playedMoves and (move[0]+2,move[1]+2) in playedMoves):
            if(board[move[0]-2][move[1]-2] == board[move[0]-1][move[1]-1]== board[move[0]+1][move[1]+1]== board[move[0]+2][move[1]+2] == myChar):
                return True
        elif ((move[0]-3,move[1]-3) in playedMoves and (move[0]-2,move[1]-2) in playedMoves and (move[0]-1,move[1]-1) in playedMoves and (move[0]+1,move[1]+1) in playedMoves):
            if(board[move[0]-3][move[1]-3] == board[move[0]-2][move[1]-2]== board[move[0]-1][move[1]-1]== board[move[0]+1][move[1]+1] == myChar):
                return True
        elif ((move[0]-4,move[1]-4) in playedMoves and (move[0]-3,move[1]-3) in playedMoves and (move[0]-2,move[1]-2) in playedMoves and (move[0]-1,move[1]-1) in playedMoves):
            if(board[move[0]-4][move[1]-4] == board[move[0]-3][move[1]-3]== board[move[0]-2][move[1]-2]== board[move[0]-1][move[1]-1] == myChar):
                return True
        elif ((move[0]-1,move[1]+1) in playedMoves and (move[0]-2,move[1]+2) in playedMoves and (move[0]-3,move[1]+3) in playedMoves and (move[0]-4,move[1]+4) in playedMoves):
            if(board[move[0]-1][move[1]+1] == board[move[0]-2][move[1]+2]== board[move[0]-3][move[1]+3]== board[move[0]-4][move[1]+4] == myChar):
                return True
        elif ((move[0]+1,move[1]-1) in playedMoves and (move[0]-1,move[1]+1) in playedMoves and (move[0]-2,move[1]+2) in playedMoves and (move[0]-3,move[1]+3) in playedMoves):
            if(board[move[0]+1][move[1]-1] == board[move[0]-1][move[1]+1]== board[move[0]-2][move[1]+2]== board[move[0]-3][move[1]+3] == myChar):
                return True
        elif ((move[0]+2,move[1]-2) in playedMoves and (move[0]+1,move[1]-1) in playedMoves and (move[0]-1,move[1]+1) in playedMoves and (move[0]-2,move[1]+2) in playedMoves):
            if(board[move[0]+2][move[1]-2] == board[move[0]+1][move[1]-1]== board[move[0]-1][move[1]+1]== board[move[0]-2][move[1]+2] == myChar):
                return True
        elif ((move[0]+3,move[1]-3) in playedMoves and (move[0]+2,move[1]-2) in playedMoves and (move[0]+1,move[1]-1) in playedMoves and (move[0]-1,move[1]+1) in playedMoves):
            if(board[move[0]+3][move[1]-3] == board[move[0]+2][move[1]-2]== board[move[0]+1][move[1]-1]== board[move[0]-1][move[1]+1] == myChar):
                return True
        elif ((move[0]+4,move[1]-4) in playedMoves and (move[0]+3,move[1]-3) in playedMoves and (move[0]+2,move[1]-2) in playedMoves and (move[0]+1,move[1]-1) in playedMoves):
            if(board[move[0]+4][move[1]-4] == board[move[0]+3][move[1]-3]== board[move[0]+2][move[1]-2]== board[move[0]+1][move[1]-1] == myChar):
                return True
        return False



    def move(self, board, possibleMoves, playedMoves, turn):
        counter = Counter()
        chosenMove = None
        candidateMoves = self.generateCandidateMoves(board, possibleMoves, playedMoves)
        for move in candidateMoves:
            for i in range(100):
                tempBoard = deepcopy(board)
                temppossiblemoves = deepcopy(possibleMoves)
                tempplayedMoves = deepcopy(playedMoves)
                tempBoard[move[0]][move[1]]=self.color
                temppossiblemoves.remove(move)
                tempplayedMoves.add(move)
                winner = game.playOmok(tempBoard, False, NaiveAI(self.color), NaiveAI(self.antiColor), temppossiblemoves, tempplayedMoves)
                if winner == self.color:
                    counter[move] += 1
        if len(counter) > 0:
            chosenMove = counter.most_common(1)[0][0]
        else:
            chosenMove = random.choice(list(candidateMoves))
        board[chosenMove[0]][chosenMove[1]] = self.color
        possibleMoves.remove(chosenMove)
        playedMoves.add(chosenMove)

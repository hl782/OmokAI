import random
import game
from copy import deepcopy

class MinimaxAI:
    def __init__(self, color, n):
        self.color = color
        if color == 'O':
            self.antiColor = 'X'
        elif color == 'X':
            self.antiColor = 'O'
        self.n = n

    def minimax(self, helper):
        candidateTriplet= []
        maxMove = None
        maxChild = None
        minMove = None
        minChild = None
        maxScore = -float("inf")
        minScore = float("inf")
        for (move, score, child) in helper.children:
            candidateTriplet.append((move, score, self.minimax(child)))

        for (move, score, child) in candidateTriplet:
            if(score > maxScore):
                maxScore = score
                maxMove = move
                maxChild = child
            if(score < minScore):
                minScore = score
                minMove = move
                minChild = child


        if (helper.level % 2 == 0):
            if (helper.level == 0):
                return maxMove
            else:
                return maxChild
        else:
            if (helper.level == 0):
                return minMove
            else:
                return minChild

    def move(self, board, possibleMoves, playedMoves, turn):
        helper = MinimaxHelper(board, self.color, self.antiColor, 0, self.n, possibleMoves, playedMoves)
        move = self.minimax(helper)
        board[move[0]][move[1]] = self.color
        possibleMoves.remove(move)
        playedMoves.add(move)

class MinimaxHelper:
    def __init__(self, board, color, antiColor, level, maxdepth, possibleMoves, playedMoves):
        self.board = board
        self.color = color

        if color == 'O':
            self.antiColor = 'X'
        elif color == 'X':
            self.antiColor = 'O'

        self.level = level
        self.maxdepth = maxdepth
        self.possibleMoves = possibleMoves
        self.playedMoves = playedMoves
        self.children = []

        if level < maxdepth:
            self.getChildren()

    def generateCandidateMoves(self):
        cardinalDirections = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]
                             ,[0, 2], [2, 2], [2, 0], [2, -2], [0, -2], [-2, -2], [-2, 0], [-2, 2]]
        if len(self.playedMoves) == 0:
            firstMoveSet = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)]
            return [random.choice(firstMoveSet)]
        else:
            #check if a winning move exists for either side
            for move in self.possibleMoves:
                if self.isWinningMove(self.board, move, True) or self.isWinningMove(self.board, move, False):
                    return [move]

            candidateMoves = set()
            for move in self.playedMoves:
                for direction in cardinalDirections:
                    if (move[0]+direction[0], move[1]+direction[1]) in self.possibleMoves:
                        candidateMoves.add((move[0]+direction[0], move[1]+direction[1]))
            return candidateMoves

    def isWinningMove(self, board, move, isSelf):
        myChar = self.color if isSelf == True else self.antiColor
        if ((move[0], move[1]+1) in self.playedMoves and (move[0],move[1]+2) in self.playedMoves and (move[0],move[1]+3) in self.playedMoves and (move[0],move[1]+4) in self.playedMoves):
            if (board[move[0]][move[1]+1] == board[move[0]][move[1]+2] == board[move[0]][move[1]+3] == board[move[0]][move[1]+4] == myChar):
                return True
        elif ((move[0],move[1]-1) in self.playedMoves and (move[0],move[1]+1) in self.playedMoves and (move[0],move[1]+2) in self.playedMoves and (move[0],move[1]+3) in self.playedMoves):
            if (board[move[0]][move[1]-1] == board[move[0]][move[1]+1]== board[move[0]][move[1]+2]== board[move[0]][move[1]+3] == myChar):
                return True
        elif ((move[0],move[1]-2) in self.playedMoves and (move[0],move[1]-1) in self.playedMoves and (move[0],move[1]+1) in self.playedMoves and (move[0],move[1]+2) in self.playedMoves):
            if(board[move[0]][move[1]-2] == board[move[0]][move[1]-1]== board[move[0]][move[1]+1]== board[move[0]][move[1]+2] == myChar):
                return True
        elif ((move[0],move[1]-3) in self.playedMoves and (move[0],move[1]-2) in self.playedMoves and (move[0],move[1]-1) in self.playedMoves and (move[0],move[1]+1) in self.playedMoves):
            if(board[move[0]][move[1]-3] == board[move[0]][move[1]-2]== board[move[0]][move[1]-1]== board[move[0]][move[1]+1] == myChar):
                return True
        elif ((move[0],move[1]-4) in self.playedMoves and (move[0],move[1]-3) in self.playedMoves and (move[0],move[1]-2) in self.playedMoves and (move[0],move[1]-1) in self.playedMoves):
            if(board[move[0]][move[1]-4] == board[move[0]][move[1]-3]== board[move[0]][move[1]-2]== board[move[0]][move[1]-1] == myChar):
                return True
        elif ((move[0]+1,move[1]) in self.playedMoves and (move[0]+2,move[1]) in self.playedMoves and (move[0]+3,move[1]) in self.playedMoves and (move[0]+4,move[1]) in self.playedMoves):
            if(board[move[0]+1][move[1]] == board[move[0]+2][move[1]]== board[move[0]+3][move[1]]== board[move[0]+4][move[1]] == myChar):
                return True
        elif ((move[0]-1,move[1]) in self.playedMoves and (move[0]+1,move[1]) in self.playedMoves and (move[0]+2,move[1]) in self.playedMoves and (move[0]+3,move[1]) in self.playedMoves):
            if(board[move[0]-1][move[1]] == board[move[0]+1][move[1]]== board[move[0]+2][move[1]]== board[move[0]+3][move[1]] == myChar):
                return True
        elif ((move[0]-2,move[1]) in self.playedMoves and (move[0]-1,move[1]) in self.playedMoves and (move[0]+1,move[1]) in self.playedMoves and (move[0]+2,move[1]) in self.playedMoves):
            if(board[move[0]-2][move[1]] == board[move[0]-1][move[1]]== board[move[0]+1][move[1]]== board[move[0]+2][move[1]] == myChar):
                return True
        elif ((move[0]-3,move[1]) in self.playedMoves and (move[0]-2,move[1]) in self.playedMoves and (move[0]-1,move[1]) in self.playedMoves and (move[0]+1,move[1]) in self.playedMoves):
            if(board[move[0]-3][move[1]] == board[move[0]-2][move[1]]== board[move[0]-1][move[1]]== board[move[0]+1][move[1]] == myChar):
                return True
        elif ((move[0]-4,move[1]) in self.playedMoves and (move[0]-3,move[1]) in self.playedMoves and (move[0]-2,move[1]) in self.playedMoves and (move[0]-1,move[1]) in self.playedMoves):
            if(board[move[0]-4][move[1]] == board[move[0]-3][move[1]]== board[move[0]-2][move[1]]== board[move[0]-1][move[1]] == myChar):
                return True
        elif ((move[0]+1,move[1]+1) in self.playedMoves and (move[0]+2,move[1]+2) in self.playedMoves and (move[0]+3,move[1]+3) in self.playedMoves and (move[0]+4,move[1]+4) in self.playedMoves):
            if(board[move[0]+1][move[1]+1] == board[move[0]+2][move[1]+2]== board[move[0]+3][move[1]+3]== board[move[0]+4][move[1]+4] == myChar):
                return True
        elif ((move[0]-1,move[1]-1) in self.playedMoves and (move[0]+1,move[1]+1) in self.playedMoves and (move[0]+2,move[1]+2) in self.playedMoves and (move[0]+3,move[1]+3) in self.playedMoves):
            if(board[move[0]-1][move[1]-1] == board[move[0]+1][move[1]+1]== board[move[0]+2][move[1]+2]== board[move[0]+3][move[1]+3] == myChar):
                return True
        elif ((move[0]-2,move[1]-2) in self.playedMoves and (move[0]-1,move[1]-1) in self.playedMoves and (move[0]+1,move[1]+1) in self.playedMoves and (move[0]+2,move[1]+2) in self.playedMoves):
            if(board[move[0]-2][move[1]-2] == board[move[0]-1][move[1]-1]== board[move[0]+1][move[1]+1]== board[move[0]+2][move[1]+2] == myChar):
                return True
        elif ((move[0]-3,move[1]-3) in self.playedMoves and (move[0]-2,move[1]-2) in self.playedMoves and (move[0]-1,move[1]-1) in self.playedMoves and (move[0]+1,move[1]+1) in self.playedMoves):
            if(board[move[0]-3][move[1]-3] == board[move[0]-2][move[1]-2]== board[move[0]-1][move[1]-1]== board[move[0]+1][move[1]+1] == myChar):
                return True
        elif ((move[0]-4,move[1]-4) in self.playedMoves and (move[0]-3,move[1]-3) in self.playedMoves and (move[0]-2,move[1]-2) in self.playedMoves and (move[0]-1,move[1]-1) in self.playedMoves):
            if(board[move[0]-4][move[1]-4] == board[move[0]-3][move[1]-3]== board[move[0]-2][move[1]-2]== board[move[0]-1][move[1]-1] == myChar):
                return True
        elif ((move[0]-1,move[1]+1) in self.playedMoves and (move[0]-2,move[1]+2) in self.playedMoves and (move[0]-3,move[1]+3) in self.playedMoves and (move[0]-4,move[1]+4) in self.playedMoves):
            if(board[move[0]-1][move[1]+1] == board[move[0]-2][move[1]+2]== board[move[0]-3][move[1]+3]== board[move[0]-4][move[1]+4] == myChar):
                return True
        elif ((move[0]+1,move[1]-1) in self.playedMoves and (move[0]-1,move[1]+1) in self.playedMoves and (move[0]-2,move[1]+2) in self.playedMoves and (move[0]-3,move[1]+3) in self.playedMoves):
            if(board[move[0]+1][move[1]-1] == board[move[0]-1][move[1]+1]== board[move[0]-2][move[1]+2]== board[move[0]-3][move[1]+3] == myChar):
                return True
        elif ((move[0]+2,move[1]-2) in self.playedMoves and (move[0]+1,move[1]-1) in self.playedMoves and (move[0]-1,move[1]+1) in self.playedMoves and (move[0]-2,move[1]+2) in self.playedMoves):
            if(board[move[0]+2][move[1]-2] == board[move[0]+1][move[1]-1]== board[move[0]-1][move[1]+1]== board[move[0]-2][move[1]+2] == myChar):
                return True
        elif ((move[0]+3,move[1]-3) in self.playedMoves and (move[0]+2,move[1]-2) in self.playedMoves and (move[0]+1,move[1]-1) in self.playedMoves and (move[0]-1,move[1]+1) in self.playedMoves):
            if(board[move[0]+3][move[1]-3] == board[move[0]+2][move[1]-2]== board[move[0]+1][move[1]-1]== board[move[0]-1][move[1]+1] == myChar):
                return True
        elif ((move[0]+4,move[1]-4) in self.playedMoves and (move[0]+3,move[1]-3) in self.playedMoves and (move[0]+2,move[1]-2) in self.playedMoves and (move[0]+1,move[1]-1) in self.playedMoves):
            if(board[move[0]+4][move[1]-4] == board[move[0]+3][move[1]-3]== board[move[0]+2][move[1]-2]== board[move[0]+1][move[1]-1] == myChar):
                return True
        return False

    def nearWin(self, board, color, antiColor):
        oneCount = 0
        twoCount = 0
        threeCount = 0
        for x in range(9):
            for y in range(5):
                curRow = board[x][y]+board[x][y+1]+board[x][y+2]+board[x][y+3]+board[x][y+4]
                if (antiColor not in curRow):
                    if curRow.count(color) == 4:
                        oneCount = oneCount+1
                    elif curRow.count(color) == 3:
                        twoCount = twoCount+1
                    elif curRow.count(color) == 2:
                        threeCount = threeCount+1

        for y in range(9):
            for x in range(5):
                curCol = board[x][y]+board[x+1][y]+board[x+2][y]+board[x+3][y]+board[x+4][y]
                if (antiColor not in curCol):
                    if curCol.count(color) == 4:
                        oneCount = oneCount+1
                    elif curCol.count(color) == 3:
                        twoCount = twoCount+1
                    elif curCol.count(color) == 2:
                        threeCount = threeCount+1

        for x in range(5):
            for y in range(5):
                curDiag = board[x][y]+board[x+1][y+1]+board[x+2][y+2]+board[x+3][y+3]+board[x+4][y+4]
                if (antiColor not in curDiag):
                    if curDiag.count(color) == 4:
                        oneCount = oneCount+1
                    elif curDiag.count(color) == 3:
                        twoCount = twoCount+1
                    elif curDiag.count(color) == 2:
                        threeCount = threeCount+1

        for x in range(4, 9):
            for y in range(5):
                curDiag = board[x][y]+board[x-1][y+1]+board[x-2][y+2]+board[x-3][y+3]+board[x-4][y+4]
                if (antiColor not in curDiag):
                    if curDiag.count(color) == 4:
                        oneCount = oneCount+1
                    elif curDiag.count(color) == 3:
                        twoCount = twoCount+1
                    elif curDiag.count(color) == 2:
                        threeCount = threeCount+1

        return oneCount, twoCount, threeCount


    def evalFunction(self, board, myBool):
        myChar = self.color if myBool == True else self.antiColor
        opponentChar = self.antiColor if myBool == True else self.Color
        oneMoveWin, twoMoveWin, threeMoveWin = self.nearWin(board, myChar, opponentChar)
        oneMoveLoss, twoMoveLoss, threeMoveLoss = self.nearWin(board, opponentChar,myChar)
        return (oneMoveWin*10000)+(twoMoveWin*100)+(threeMoveWin*1)-(oneMoveLoss*5000)-(twoMoveLoss*500)-(threeMoveLoss*0.5)

    def getChildren(self):
        newDepth = self.level+1
        candidateMoves = self.generateCandidateMoves()
        for move in candidateMoves:
            copyboard = deepcopy(self.board)
            copypossiblemoves = deepcopy(self.possibleMoves)
            copyplayedMoves = deepcopy(self.playedMoves)
            copyboard[move[0]][move[1]]=self.color
            copypossiblemoves.remove(move)
            copyplayedMoves.add(move)
            movescore = self.evalFunction(copyboard, True)
            self.children.append((move, movescore ,MinimaxHelper(copyboard, self.antiColor, self.color, newDepth, self.maxdepth, copypossiblemoves, copyplayedMoves)))

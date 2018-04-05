import random

class RandomAI:
    def __init__(self, color):
        self.color = color

    def move(self, board, possibleMoves, playedMoves, turn):
        randomMove = random.choice(possibleMoves)
        board[randomMove[0]][randomMove[1]] = self.color
        possibleMoves.remove(randomMove)
        playedMoves.add(randomMove)

import game
import time
from human import Human
from randomAI import RandomAI
from naiveAI import NaiveAI
from minimaxAI import MinimaxAI
from learningAI import MonteCarloAI

def selectAI(n, player):
    command = int(n)
    if n == 0:
        return Human(player)
    elif n == 1:
        return RandomAI(player)
    elif n == 2:
        return NaiveAI(player)
    elif n == 3:
        return MinimaxAI(player, 1)
    elif n == 4:
        return MinimaxAI(player, 2)
    elif n == 5:
        return MinimaxAI(player, 3)
    elif n == 6:
        return MonteCarloAI(player)

    else:
        command = input("Not a valid option. Enter a number from 0 to 6")
        selectAI(command, player)


def omok(isTest, playerA, playerB):
    cleanBoard = game.createBoard()
    cleanMoves = game.createInitialMoves()
    cleanPlayedMoves = set()

    if isTest == True:
        print ("Do nothing for now")
    else:
        playerA = selectAI(3, 'O')
        playerB = selectAI(2, 'X')

    return game.playOmok(cleanBoard, True, playerA, playerB, cleanMoves, cleanPlayedMoves)

if __name__ == '__main__':
    # start_time = time.time()
    winner = omok(False, None, None)
    # print("--- %s seconds ---" % (time.time() - start_time))

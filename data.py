import game
import main
import time

oWinner = 0
xWinner = 0
tie = 0

start_time = time.time()

for i in range(10000):
	winner = main.omok(False, None, None)
	if (winner == 'O'):
		oWinner += 1
	elif (winner == 'X'):
		xWinner += 1
	elif (winner == 'tie'):
		tie += 1
print("O won %d times out of 10000" % (oWinner))
print("X won %d times out of 10000" % (xWinner))
print("There were %d tied games out of 10000" % (tie))

print("--- %s seconds ---" % (time.time() - start_time))


class Human:
    def __init__(self, color):
        self.color = color

    def move(self, board, possibleMoves, playedMoves, turn):
        while True:
            try:
                move1 = raw_input("Enter X Coordinate: ")
                move2 = raw_input("Enter Y Coordinate: ")
                # print moveInput
                chosenMove = (int(move2), int(move1))
            except EOFError:
                print("Invalid Input. Check your format and try again.")
            except (IndexError, ValueError):
                print("Invalid Input. Check your format and try again.")
            else:
                break

        if chosenMove in possibleMoves:
            board[chosenMove[0]][chosenMove[1]] = self.color
            possibleMoves.remove(chosenMove)
            playedMoves.add(chosenMove)
        else:
           print("Not a valid move or your opponent has already played there!")
           self.move(board, possibleMoves, playedMoves, turn)

playerOne = 'Player 1'
playerTwo = 'Player 2'
currPlayer = playerOne

def setPlayer():
    global currPlayer
    if currPlayer == playerOne:
        currPlayer = playerTwo
    else:
        currPlayer = playerOne


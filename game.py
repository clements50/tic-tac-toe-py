playerOne = 'Player 1'
playerTwo = 'Player 2'
currPlayer = playerOne

def setPlayer():
    global currPlayer
    if currPlayer == playerOne:
        currPlayer = playerTwo
    else:
        currPlayer = playerOne

board = [['','',''],
         ['','',''],
         ['','','']]

def getUserInput():
    inpStr = 'Please enter a number between 1 and 9 '
    while True:
        try:
            x = int(input(inpStr))
            if x <= 0 or x > 9:
                print(inpStr)
            else:
                return x
        except:
            print('You did not enter a valid number ')


CONNECT = 4 # You can change this value to change 
            # the number of counters that need to be connected to win

board = [[" ", " ", " ", " ", " ", " ", " "] for i in range(6)]
# Extension: Change the board size to whatever you want!

def printBoard(board): # No Bugs Here!
    print("1 2 3 4 5 6 7")
    for i in list(reversed(board)):
        print("|".join(i))

def checkWin(row):
    connected = 0
    connection = ""
    for i in row:
        if i == connection:
            connected += 1
        else:
            connected = 1
            connection = i
        if connected == 7 and connection != " ":
            # TASK 1) change the 7 to a constant defined above so we can change the game size
            return True
    return False

def RunGame():

    players = ["Red", "Yellow"] 
    # Task 2) change the values in this list to be the first letter of the color to make the board look nicer!
    
    player = 0 

    while True:
        printBoard(board)
        print("Player " + players[player] + "'s turn")
        column = int(input("Enter column: "))
        if column < 0 or column > 8:
            # Task 3) Fix the game boundaries so the player can only enter a number between 1 and 7
            print("Invalid column")
            continue

        # Checking if the column is full (no bugs here!)
        column -= 1
        row = -1
        placed = False
        for i in range(6):
            if (board[i][column] == " ") and (not placed):
                board[i][column] = players[player]
                row = i
                placed = True 
        # End of column full check

        if not placed:
            # Task 4) Don't let the user place a counter in a full column
            pass 

        #Diagonal Win Checking (no bugs here!)
        posDiagonal = [board[row][column]]
        negDiagonal = [board[row][column]]
        for i in range(5): 
            if i == 0: 
                continue
            if (row + i <= 5) and (column + i <= 6):
                posDiagonal.append(board[row + i][column + i])
            if (row - i >= 0) and (column - i >= 0):
                posDiagonal.insert(0, board[row - i][column - i])
            if (row + i <= 5) and (column - i >= 0):
                negDiagonal.append(board[row + i][column - i])
            if (row - i >= 0) and (column + i <= 6):
                negDiagonal.insert(0, board[row - i][column + i])
        # Diagonal Win Checking end

        if any([checkWin(posDiagonal),
               checkWin(negDiagonal),
               checkWin(board[row]),
               checkWin([row[column] for row in board])]):
            
            print()
            # Task 5) print the board and the winner
            
            return
        
        elif (sum([row.count(" ") for row in board]) == 0):
            
            print()
            # Task 6) Let the user know there are no more blank squares

            return

        player = (player + 1) % 2


RunGame()
CONNECT = 4 # You can change this value to change 
            # the number of counters that need to be connected to win

board = [[" ", " ", " ", " ", " ", " ", " "] for i in range(6)]

def printBoard(board):
    print("1 2 3 4 5 6 7")
    for i in list(reversed(board)):
        print("|".join(i))

def checkWin(row):

    # given a list [] find any four repeating characters
    connected = 0
    connection = ""
    for i in row:
        if i == connection:
            connected += 1
        else:
            connected = 1
            connection = i
        if connected == 4 and connection != " ":
            # Change four to a constant defined above so we can change the game size
            return True
    return False

def RunGame():
    # Run the game
    players = ["R", "Y"]
    player = 0 
    # the player alternates from 0 to 1


    while True:
        printBoard(board)
        print("Player " + players[player] + "'s turn")
        column = int(input("Enter column: "))
        if column < 0 or column > 8:
            # Fix the game boundaries
            print("Invalid column")
            continue

        column -= 1
        row = -1
        placed = False
        for i in range(6):
            if (board[i][column] == " ") and (not placed):
                board[i][column] = players[player]
                row = i
                placed = True 

        if not placed:
            print("Column is full")
            continue # Skip the rest of the loop

        #checkWin(board[row])
        #checkWin([row[column - 1] for row in board])
        ## Check diagonals based on column and row
        
        posDiagonal = [board[row][column]]
        negDiagonal = [board[row][column]]
        for i in range(1): # This is the number of diagonals to check 

            # TASK 3) make this loop continue for longer so it checks the entire board.

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


        if any([checkWin(posDiagonal),
               checkWin(negDiagonal),
               checkWin(board[row]),
               checkWin([row[column] for row in board])]):
            
            # Task 2) print the board and the winner (hint: the winner is the player variable)
            return
        
        elif (sum([row.count(" ") for row in board]) == 0):
            
            # Task 3) print the board and let the user know there are no more blank squares

            return

        player = (player + 1) % 2


RunGame() # Uncomment this line to run the game!!
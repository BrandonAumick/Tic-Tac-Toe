import sys

#Active player
player = 1

#2D array for the board
board = [[" "," "," "], [" "," "," "], [" "," "," "]]

#Function for displaying the board
def displayBoard():
    c = 1
    for x in board:
        print(x[0], '|', x[1], '|', x[2], '         ', c, '|', (c+1), '|', (c+2))
        
        #Print horizontal lines, but not for the last set
        c+=3
        if c == 10:
            break
        print('--|---|--           --|---|--')
        
#Function to check if a player has won        
def checkWin():
    c = 0
    winner = "Player " + str((player % 2) + 1) +" wins!\n"
    #Checks each row for a win
    for x in board:
        if x[0] == x[1] == x[2]:
            if x[0] != " ":
                print(winner)
                return False
    
    #First symbol in each column
    columnFirstSymbol = [board[0][0], board[0][1], board[0][2]]
    
    #Checks columns for a win
    column = 0
    while c < 3:
        columnCount = 0
        for x in board:
            if x[c] == columnFirstSymbol[column] and columnFirstSymbol[column] != " ":
                columnCount += 1
        if columnCount == 3:
            print (winner)
            return False
        else:
            column += 1
            c += 1
    
    #Checks for diagonals
    if board[1][1] != " ":
        if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
            print(winner)
            return False
    
    return True
    
#Function to end game
def endGame():
    global player
    player = 1
    global board
    board = [[" "," "," "], [" "," "," "], [" "," "," "]]
    again = input('Play again? (y or n): ')
    while (again != 'y'):
        if again == 'n':
            sys.exit('Bruh')
        again = input('Please enter y or n: ')
    print("\n\n\n\n\n\n")


#Loop for multiple games
while(True):

    #Single game loop
    while(checkWin()):

        #Sets player symbol
        symbol = 'X'
        if player == 1:
            symbol = 'X'
        else:
            symbol = 'O'
            
        #Player input variable
        spot = 0

        #Displays places on board, what the current player is, and what their symbol is
        print('Player ', player, ':', symbol)
        displayBoard()
        
        try:
            #Takes player input for where to play
            spot = int(input('Choose where to play: '))
            print('\n\n\n\n\n\n')
            
            if 1 <= spot <= 3:
                row = 0
            elif 4 <= spot <= 6:
                row = 1
            elif 7 <= spot <= 9:
                row = 2
            #If the input is not a number in the valid range
            else:
                print("!!!Please enter a valid number!!!\n")
                continue
            
            #Checks if the chosen spot has already been played in
            if board[row][(spot + 2)%3] != " ":
                print("Please choose an empty space\n")
                continue
            else:
                #Adds spot on board and displays it
                board[row][(spot + 2)%3] = symbol
                                
            #Changes player
            if player == 1:
                player = 2
            else:
                player = 1
                
        #If the input is not a number        
        except:
            print('\n\n\n\n\n\n!!!Please enter a number!!!\n')
    endGame()
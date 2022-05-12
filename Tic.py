import sys
import random

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



def checkRow():
    global row
    if 1 <= spot <= 3:
        row = 0
    elif 4 <= spot <= 6:
        row = 1
    elif 7 <= spot <= 9:
        row = 2
    #If the input is not a number in the valid range
    else:
        print("!!!Please enter a valid number!!!\n")
        return True
    return False

       
       
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



#Checks for a tie
def checkTie():
    symbolCount = 0
    for x in board:
        for c in range(3):
            if x[c] != " ":
                symbolCount += 1
    if symbolCount == 9:
        print("Tie game!")
        return False
    return True



#Function for selecting a game mode
def selectMode():
    mode = input("Select a mode:\n1 - Player vs AI\n2 - Player vs Player\n")
    while mode != '1' and mode != '2':
        print("Please select a present mode\n")
        mode = input("Select a mode:\n1 - Player vs AI\n2 - Player vs Player\n")
        print()  
    return int(mode)


    
#Function to end game
def endGame():
    displayBoard()
    global gMode
    global player
    player = 1
    global board
    #Resets the board
    board = [[" "," "," "], [" "," "," "], [" "," "," "]]
    #Gives the player the option to keep playing, stop, or change their mode with the selectMode function
    again = input('\nPlay again or change mode?\ny: Play Again\nn: Stop Playing\nc: Change Mode\n')
    while (again != 'y'):
        if again == 'n':
            sys.exit('Bruh')
        elif again == 'c':
            #Prompts player to change the mode and sets again = y to keep the game playing
            gMode = selectMode()
            again = 'y'
            continue
        again = input('Please enter y or n: ')
    print("\n\n\n\n\n\n")



#Initial mode selection
gMode = selectMode()
#Loop for multiple games
while(True):

    #Single game loop
    while(checkWin() and checkTie()):

        #Sets player symbol
        symbol = 'X'
        if player == 1:
            symbol = 'X'
        else:
            symbol = 'O'
            
        
        #Displays places on board, what the current player is, and what their symbol is   
        """If game mode 2 was selected (Player vs Player) gMode will = 2 and this will run for manual placement
        instead of the bot code since when palyer = 2, it will equal gMode and the if statement will be true.
        If game mode 1 is selected, player 2 will not equal gMode and it will go to the bot code."""
        if player == 1 or player == gMode:
            print('Player ', player, ':', symbol)
            displayBoard()
            try:
                #Takes player input for where to play
                spot = int(input('Choose where to play: '))
                print('\n\n\n\n\n\n')
                
                if checkRow():
                    continue
                
                #Checks if the chosen spot has already been played in
                if board[row][(spot + 2)%3] != " ":
                    print("Please choose an empty space\n")
                    continue
                else:
                    #Adds spot on board and displays it
                    board[row][(spot + 2)%3] = symbol
                                    
                #Changes player
                player = (player % 2) + 1
                    
            #If the input is not a number        
            except:
                print('\n\n\n\n\n\n!!!Please enter a number!!!\n')
                
                
        else:
            
            #Checks to see if it can win or stop a win in a row
            """The placed variable is set to false when the bot plays, preventing any of its other checks from running
            which would cause it to play twice"""
            placed = True
            boardPlaceRow = 0
            winStopPossibilities = []
            
            #Function for appending a symbol to the array winStopPossibilities if it appears twice
            def appendWinPossibilities():
                global winStopPossibilities
                if oCount == 2:
                    winStopPossibilities.append('O')
                elif xCount == 2:
                    winStopPossibilities.append('X')
                else:
                    winStopPossibilities.append(' ')
                
            """It goes through every row and sees if there are two of the same symbol in that row, if there are it
            appends that symbol to the winStopPossibilities array."""
            for x in board:
                boardPlaceColumn = 0
                xCount = 0
                oCount = 0
                for c in x:
                
                    if c == 'X':
                        xCount += 1
                    elif c == 'O':
                        oCount += 1
                appendWinPossibilities()
                    
            """Using the appended symbols, it checks first if it can play its own symbol to win in one of the rows.
            If it sees a blank space in one of the rows that has 2 of its own symbols, it will play it. If it can't
            play to win, it then sees if any of the other symbol were appended and it there is a blank space it can
            play to prevent the other player from winning."""        
            def rowFindAndPlace(sym):
                global board
                global placed
                winStopCount = 0
                for x in winStopPossibilities:
                    if x == sym:
                        for i in range(3):
                            if board[winStopCount][i] == ' ':
                                board[winStopCount][i] = symbol
                                placed = False
                                break
                    winStopCount += 1
                    
            rowFindAndPlace('O')
            if placed:
                rowFindAndPlace('X')
                
                
            #Cehcks to see if it can win or stop a win in a column
            if placed:
                winStopPossibilities = []
                for j in range(3):
                    xCount = 0
                    oCount = 0
                    for x in board:
                        if x[j] == 'X':
                            xCount += 1
                        elif x[j] == 'O':
                            oCount += 1
                    appendWinPossibilities()
                
                #This function uses the same method as the row function, but checks if it should play in a column
                def columnFindAndPlace(sym):
                    global board
                    global placed
                    winStopCount = 0
                    for x in winStopPossibilities:
                        if x == sym:
                            for i in range(3):
                                if board[i][winStopCount] == ' ':
                                    board[i][winStopCount] = symbol
                                    placed = False
                                    break
                        winStopCount += 1
                        
                columnFindAndPlace('O')
                if placed:
                    columnFindAndPlace('X')
                
                    
                if placed:
                    oCount = 0
                    xCount = 0
                    winStopPossibilities = []
                    """leftDiagCount will = j for the first loop, allowing for the downward sloping diagonal to be checked
                    and on the second loop it will be set = 2 and will be decremented by 1 every j loop, allowing the
                    upward sloping diagonal to be checked"""
                    leftDiagCount = 0
                    #Checks diagonal going right for 2 of the same symbol
                    for i in range(2):
                        for j in range(3):
                            if board[j][j] == 'O':
                                oCount += 1
                            elif board[j][leftDiagCount] == 'X':
                                xCount += 1
                            if i == 0:
                                leftDiagCount += 1
                            else:
                                leftDiagCount -= 1
                        appendWinPossibilities()
                        leftDiagCount = 2
                    def diagonalFindAndPlace(sym):
                        leftDiagCount = 0
                        for i in range(2):
                            if winStopPossibilities[i] == sym:
                                for j in range(3):  
                                    if board[j][leftDiagCount] == ' ':
                                        board[j][leftDiagCount] = symbol
                                        placed = False
                                        break
                                    if i == 0:
                                        leftDiagCount += 1
                                    else:
                                        leftDiagCount -= 1
                            leftDiagCount = 2
                                    
                                
                        
                        
                            
                        
                
                
            #Plays random if it can't stop a win or win    
            if placed:
                spot = random.randint(1, 9)
                
                checkRow()
                #Checks if the chosen spot has already been played in
                if board[row][(spot + 2)%3] != " ":
                    continue
                    print("Please choose an empty space\n")
                else:
                    #Adds spot on board and displays it
                    board[row][(spot + 2)%3] = symbol
                                    
            #Changes player
            player = (player % 2) + 1
            
    endGame()
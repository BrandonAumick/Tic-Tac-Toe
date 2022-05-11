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
    board = [[" "," "," "], [" "," "," "], [" "," "," "]]
    again = input('\nPlay again or change mode?\ny: Play Again\nn: Stop Playing\nc: Change Mode\n')
    while (again != 'y'):
        if again == 'n':
            sys.exit('Bruh')
        elif again == 'c':
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
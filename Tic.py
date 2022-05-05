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

#Loop for multiple games
while(True):

    #Single game loop
    while(True):

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
            print('\n\n\n')
            
            if 1 <= spot <= 3:
                row = 0
            elif 4 <= spot <= 6:
                row = 1
            elif 7 <= spot <= 9:
                row = 2
            #If the input is not a number in the valid range
            else:
                print("Please enter a valid number\n")
                continue
            
            #Checks if the chosen spot has already been played in
            if board[row][(spot + 2)%3] != " ":
                print("Please choose an empty space\n")
                continue
            else:
                #Adds spot on board and displays is
                board[row][(spot + 2)%3] = symbol
            
            
            #Changes player
            if player == 1:
                player = 2
            else:
                player = 1
                
        #If the input is not a number        
        except:
            print('\nPlease enter a number\n')
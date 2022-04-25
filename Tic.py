#Active player
player = 1

#2D array for the board
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#Function for displaying the board
def displayBoard():
    c = 0
    for x in board:
        print(x[0], '|', x[1], '|', x[2])
        
        #Print horizontal lines, but not for the last set
        c+=1
        if c == 3:
            break
        print('--|---|--')


#Game loop
while(True):

    #Sets player symbol
    symbol = 'X'
    displayBoard()
    if player == 1:
        symbol = 'X'
    else:
        symbol = 'O'
        
    #Player input
    spot = 0    
    print('Player ', player, ', you are, ', symbol, 'please select where to place')
    print(1, '|', 2, '|', 3)
    print('--|---|--')
    print(4, '|', 5, '|', 6)
    print('--|---|--')
    print(7, '|', 8, '|', 9)
    input(spot)
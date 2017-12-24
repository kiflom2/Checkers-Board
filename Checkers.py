#R ='Red' piece
#B ='Black' Piece
from __future__ import print_function

#Formatting change
#TODO: don't mix numbers and characters
brd = [
    [0,'B',0,'B',0,'B',0,'B'],
    ['B',0,'B',0,'B',0,'B',0],
    [0,'B',0,'B',0,'B',0,'B'],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    ['R',0,'R',0,'R',0,'R',0],
    [0,'R',0,'R',0,'R',0,'R'],
    ['R',0,'R',0,'R',0,'R',0]
]

###################FUNCTIONS###############
# Will print the checkers board
def pretty_print(brd):
    counter = 0
    for row in brd:
        for cell in row:
            #print(counter,end=' ')
            print(cell, end='  ')
            if (counter == 7):
                counter = 0
                print("\n",end='')
            else:
                counter += 1
            #print(str(cell), end=' ')



#TODO:incorporate a test to verify these functions
# prints 'valid move' if the move is valid
def is_valid_move(brd,(x, y),(x2, y2)):
    if 0<=x>=7 and 0<=x2>=7 and 0<=y>=7 and 0<=y2>=7:
        if brd[x2][y2] == 0: # is the destination space free
            if brd[x][y] =='R':   #for the Red piece
                if x2==x-1:
                    if y2==y-1 or y2==y+1:
                        print ('valid move') # move is valid

            elif brd[x][y]=='B': # for the Black piece
                if x2==x+1:
                    if y2==y-1 or y2== y+1:
                        print ('valid move')  #move is valid
    else:
        print ('invalid move')

# moves the piece; considering the move is valid
#TODO:Error throwing and handling would be ideal here
def move_piece(brd, (x, y), (x2, y2)):
    brd[x][y], brd[x2][y2] = brd[x2][y2], brd[x][y]


#TODO:This is an ideal place to use help functions this is long and very hard
#to fix if something were to go wrong

# carry out capturing move.
def capturing_move(brd, (x1, y1), (x3, y3), (x2, y2)):
    if brd[x1][y1] == 'R': # if it is R's turn
        if brd[x2][y2] == brd[x1-2][y1-2] == 0:  # if the destination space is free
            if brd[x3][y3] == brd[x1-1][y1-1] =='B':  # Situation 1
                brd[x3][y3] = 0 # cancel B and change it by 0
                brd[x1][y1], brd[x2][y2] = brd[x2][y2],brd[x1][y1] # exchange between R and empty space
        elif brd[x2][y2] == brd[x1-2][y1+2] == 0:
            if brd[x3][y3] == brd[x1-1][y1+1] == 'B': # Situation 2
                brd[x3][y3] = 0 # cancel B and change it by 0
                brd[x1][y1], brd[x2][y2] = brd[x2][y2],brd[x1][y1] # exchange between R and empty space
    elif brd[x1][y1] == 'B': # if it is B's turn
        if brd[x2][y2] == brd[x1+2][y1+2] == 0:  # if the destination space is free
            if brd[x3][y3] == brd[x1+1][y1+1] =='R':  # situation 1
                brd[x3][y3]=0  # cancel R and change it by 0
                brd[x1][y1], brd[x2][y2] = brd[x2][y2],brd[x1][y1] # exchange between B and empty space
        elif brd[x2][y2] == brd[x1+2][y1-2] == 0:
            if brd[x3][y3] == brd[x1+1][y1-1] =='R': # situation 1
                brd[x3][y3]=0  # cancel R and change it by 0
                brd[x1][y1], brd[x2][y2] = brd[x2][y2],brd[x1][y1] # exchange between B and empty space



#TODO: works great for top pieces but not for bottom pieces
#print(list_possible_moves(brd,(2,1))) works great got (3,0) (3,2)
#print(list_possible_moves(brd,(5,0))) NOT Working got (4,1) (4,-1)
# prints possible available moves for (x, y)
def list_possible_moves(brd, (x, y)):
    # add how to avoid outputs which are out of the range (x-2)(y+2),(y-2),(x+2), (x-1), (y+1), (y-1), ,(x+1),
    if brd[x][y]=='R':
        if brd[x-1][y+1] =='B' and brd[x-1][y-1] =='B':
            if brd[x-2][y+2]==0 and brd[x-2][y-2]==0:
                print ((x-2, y+2), (x-2, y-2))
            elif brd[x-2][y+2]==0 and brd[x-2][y-2]!=0:
                print (x-2, y+2)
            elif brd[x-2][y+2]!=0 and brd[x-2][y-2]==0:
                print (x-2, y-2)
        elif brd[x-1][y+1] =='B' and brd[x-1][y-1] !='B':
            if brd[x-2][y+2]==0:
                print (x-2, y+2)
        elif brd[x-1][y+1] !='B' and brd[x-1][y-1] =='B':
            if brd[x-2][y-2]==0:
                print (x-2, y-2)
        elif brd[x-1][y+1] ==0 and brd[x-1][y-1] ==0:
            print ((x-1, y+1), (x-1, y-1))
        elif brd[x-1][y+1] ==0 and brd[x-1][y-1] !=0:
            print (x-1, y+1)
        elif brd[x-1][y+1] !=0 and brd[x-1][y-1] ==0:
            print (x-1, y-1)
        else:
            print ('No available moves')
    elif brd[x][y]=='B':
        if brd[x+1][y-1]=='R' and brd[x+1][y+1]=='R':
            if brd[x+2][y-2]==0 and brd[x+2][y+2] ==0:
                print ((x+2, y-2), (x+2, y+2))
            elif brd[x+2][y-2]==0 and brd[x+2][y+2] !=0:
                print (x+2, y-2)
            elif brd[x+2][y-2]!=0 and brd[x+2][y+2] ==0:
                print (x+2, y+2)
        elif brd[x+1][y-1]=='R' and brd[x+1][y+1]!='R':
            if brd[x+2][y-2]==0:
                print(x+2, y-2)
        elif brd[x+1][y-1]!='R' and brd[x+1][y+1]=='R':
            if brd[x+2][y+2] ==0:
                print (x+2, y+2)
        elif brd[x+1][y-1]==0 and brd[x+1][y+1]==0:
            print ((x+1, y-1), (x+1, y+1))
        elif brd[x+1][y-1]==0 and brd[x+1][y+1]!=0:
            print (x+1, y-1)
        elif brd[x+1][y-1]!=0 and brd[x+1][y+1]==0:
            print (x+1, y+1)
        else:
            print ('No available moves')
    else:
        print ('No available moves')


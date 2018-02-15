#R ='Red' piece
#B ='Black' Piece
#E ='Empty'place

###################FUNCTIONS###############

PIECE_RED   = "R"
PIECE_BLACK = "B"
PIECE_EMPTY = "E"

#Generate board
GlobalBoard = [['E', 'B','E','B','E','B','E','B'],
                ['B','E','B','E','B','E','B','E'],
                ['E','B','E','B','E','B','E','B'],
                ['E','E','E','E','E','E','E','E'],
                ['E','E','E','E','E','E','E','E'],
                ['R','E','R','E','R','E','R','E'],
                ['E','R','E','R','E','R','E','R'],
                ['R','E','R','E','R','E','R','E']]

#TODO: generate empty board


def pretty_print(b):
    counter = 0
    for row in b:
        for cell in row:
            #print(counter,end=' ')
            #print(cell, end='  ')
            print(cell, '  ')
            if (counter == 7):
                counter = 0
                #print('\n',end='' '')
                print('\n','')
            else:
                counter += 1
            #print(str(cell), end=' ')

def isValid(cord):
    return cord[0]>=0 and cord[0] <8 and cord[1] >=0 and cord[1]<8

def isEmpty(b,cord):
    return b[cord[0]][cord[1]] == PIECE_EMPTY

def getType(b,cord):
    if isRed(b,cord):
        return PIECE_RED
    elif isEmpty(b,cord):
        return PIECE_EMPTY
    elif isBlack(b,cord):
        return PIECE_BLACK
    else:
        print "What the hell how did you get here"

def isBlack(b,cord):
    return b[cord[0]][cord[1]] == PIECE_BLACK

def isRed(b,cord):
    return b[cord[0]][cord[1]] == PIECE_RED

#def toLeft(x,y,PieceType="B",times=1):
    #return [(x-(direction*times)),(y-(times *direction))]
def toLeft(cord,PieceType=PIECE_RED,times = 1):
    direction = -1
    if PieceType == PIECE_BLACK:
        direction *= -1*times
    cord[0]= cord[0]-direction
    return cord
#toRight(toLeft(x,y))

def toRight(cord,PieceType=PIECE_RED,times = 1):
    direction = 1
    if PieceType == PIECE_BLACK:
        direction *= -1*times
    cord[0] -=direction
    return cord

def toFront(cord,PieceType=PIECE_RED,times = 1):
    direction = 1
    if PieceType == PIECE_BLACK:
        direction *= -1*times
    cord[1]+=direction
    return cord

def toBack(cord,PieceType=PIECE_RED,times = 1):
    direction = -1
    if PieceType == PIECE_BLACK:
        direction *= -1*times
    cord[1]+=direction
    return cord

def jumpRight(cord,PieceType=PIECE_RED,Forward= True):
    if Forward:
        return toRight(toFront(cord,PieceType,2),PieceType,2)
    else:
        return toRight(toBack(cord,PieceType,2),PieceType,2)

def jumpLeft(x,y,PieceType=PIECE_RED,Forward= True):
    if Forward:
        return  toLeft(toFront(x,y,PieceType,2),PieceType,2)
    else:
        return toLeft(toBack(x,y,PieceType,2),PieceType,2)

def possible_moves(b, x, y):
    moves = []
    pieceType = getType(b,[x,y])
    if isEmpty(b,[x,y]):
        return []
    #try right
    moves.append(toRight(b,toFront(b,[x,y],pieceType),pieceType))
    moves.append(toLeft(b,toFront(b,[x,y],pieceType),pieceType))
    moves.append(toRight(b,toBack(b,[x,y],pieceType),pieceType))
    moves.append(toLeft(b,toBack(b,[x,y],pieceType),pieceType))
    moves.append(toRight(b,toFront(b,[x,y],pieceType,2),pieceType,2))
    moves.append(toLeft(b,toFront(b,[x,y],pieceType,2),pieceType,2))
    moves.append(toRight(b,toBack(b,[x,y],pieceType,2),pieceType,2))
    moves.append(toLeft(b,toBack(b,[x,y],pieceType,2),pieceType,2))

    result = []
    for m in moves:
        if isValid(m) and isEmpty(b,m):
            result.append(m)


    return result

#TODO: finish the jumps there should be four jumps

# possible moves
#TODO: Break down into smaller functions
def possible_moves_prev(b, x, y):
    if is_capture_move_r1_valid(
        b, x, y, x-1, y-1, x-2, y-2) == 'valid capturing move':
        print(x-2, y-2)
    if is_capture_move_r2_valid(
        b, x, y, x-1, y+1, x-2, y+2) == 'valid capturing move':
        print(x-2, y+2)
    if is_capture_move_b1_valid(
        b, x, y, x+1, y+1, x+2, y+2) == 'valid capturing move':
        print(x+2, y+2)
    if is_capture_move_b2_valid (
        b, x, y, x+1, y-1, x+2, y-2) == 'valid capturing move':
        print(x+2, y-2)
    if is_valid_move(b, x, y, x-1, y-1) == 'valid move':
        print(x-1, y-1)
    if is_valid_move(b, x, y, x-1, y+1) == 'valid move':
        print(x-1, y+1)
    if is_valid_move(b, x, y, x+1, y-1) == 'valid move':
        print(x+1, y-1)
    if is_valid_move(b, x, y, x+1, y+1) == 'valid move':
        print(x+1, y+1)

#Legal lmoves
def is_valid_move(b, x, y, x2, y2):
    if 0 <= x <= 7 and 0 <= x2 <= 7  and 0 <= y <= 7 and 0 <= y2 <= 7:
        if b[x2][y2] == 'E':  # is the destination space free
            if b[x][y] == 'R':   #for the Red piece
                if x2 == x-1:
                    if y2 == y-1 or y2 == y+1:
                        return 'valid move'  # move is valid
                    else:
                        return 'invalid move'
                else:
                    return 'invalid move'

            elif b[x][y] == 'B':  # for the Black piece
                if x2 == x+1:
                    if y2 == y-1 or y2 == y+1:
                        return 'valid move'  #move is valid
                    else:
                        return 'invalid move'
                else:
                    return 'invalid move'

        else:
            return 'invalid move'
    else:
        return 'invalid move'

legalmoves =[]

#Test legal moves
import unittest
class Testlegalmoves(unittest.TestCase):
    def test_is_valid_move(self):
        self.assertEqual(legalmoves.is_valid_move(
            GlobalBoard, 2, 3, 3, 4), 'valid move')
        self.assertEqual(legalmoves.is_valid_move(
            GlobalBoard, 5, 2, 4, 1), 'valid move')
        self.assertEqual(legalmoves.is_valid_move(
            GlobalBoard, 6, 1, 5, 0), 'invalid move')
        self.assertEqual(legalmoves.is_valid_move(
            GlobalBoard, 5, 2, 4, 2), 'invalid move')
        self.assertEqual(legalmoves.is_valid_move(
            GlobalBoard, 6, 7, 5, 8), 'invalid move')


#if __name__ == '__main__':
    unittest.main()

# Move a piece with error handling and throwing
# it couldnt catche when i put 6 variables instead of 5 ???
def move_piece(b, x, y, x2, y2):
    try:
        b[x][y], b[x2][y2] = b[x2][y2], b[x][y]

    except TypeError as e:
        return 'Invalid input:' + str(e)

    except IndexError as e:
        return 'Out of range input:' + str(e)

    except Exception as e:
        return e


def isR(b, x,y):
    return b[x][y] == 'R'

# verifies capturing move
def is_capture_move_r1_valid(b, x1, y1, x3, y3, x2, y2):
    if 0 <= x1 <= 7 and \
    0 <= x2 <= 7 and 0 <= x3 <= 7 and \
    0 <= y1 <= 7 and 0 <= y2 <= 7 and \
    0 <= y3 <= 7:
#           isR(x1,y1)
        if b[x1][y1] == 'R':  # if it is R's turn
            if b[x2][y2] == b[x1 - 2][y1 - 2] == 'E' \
               and b[x3][y3] == b[x1 - 1][y1 - 1] \
               == 'B':  # if destspace is free
                return 'valid capturing move'
            else:
                return 'invalid capturing move'
    else:
        return 'invalid capturing move'


def is_capture_move_r2_valid(b, x1, y1, x3, y3, x2, y2):
    if 0 <= x1 >= 7 and 0 <= x2 >= 7 \
       and 0 <= x3 >= 7 and 0 <= y1 >= 7 \
       and 0 <= y2 >= 7 and 0 <= y3 >= 7:
        if b[x1][y1] == 'R':  # if it is R's turn
            if b[x2][y2] == b[x1 - 2][y1 + 2] == 'E'\
               and b[x3][y3] == b[x1 - 1][y1 + 1] == 'B':
#               if dest space is free
                return 'valid capturing move'
            else:
                return 'invalid capturing move'
    else:
        return 'invalid capturing move'


def is_capture_move_b1_valid(b, x1, y1, x3, y3, x2, y2):
    if 0 <= x1 >= 7 and 0 <= x2 >= 7 and \
       0 <= x3 >= 7 and 0 <= y1 >= 7 and \
       0 <= y2 >= 7 and 0 <= y3 >= 7:
# if it is B's turn
        if b[x1][y1] == 'B':
            if b[x2][y2] == b[x1 + 2][y1 + 2] == 'E' \
               and b[x3][y3] == b[x1 + 1][y1 + 1] == 'R':
# if dest.space is free
                return 'valid capturing move'
            else:
                return 'invalid capturing move'
    else:
        return 'invalid capturing move'



def is_capture_move_b2_valid(b, x1, y1, x3, y3, x2, y2):
    if 0 <= x1 >= 7 and 0 <= x2 >= 7 and \
       0 <= x3 >= 7 and 0 <= y1 >= 7 and \
       0 <= y2 >= 7 and 0 <= y3 >= 7:
        if b[x1][y1] == 'B':  # if it is B's turn
            if b[x2][y2] == b[x1 + 2][y1 - 2] == 'E' \
               and b[x3][y3] == b[x1 + 1][y1 - 1] == 'R':
# if dest. space free
                return 'valid capturing move'
            else:
                return 'invalid capturing move'
    else:
        return 'invalid capturing move'


# make capturing move,  considering the move is legal
def capturring_move(b, x1, y1, x3, y3, x2, y2):
    b[x3][y3] = 'E'
    b[x1][y1], b[x2][y2] = b[x2][y2], b[x1][y1]
    pretty_print(b)  # why this became necessary?



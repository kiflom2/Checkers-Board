#R ='Red' piece
#B ='Black' Piece
#E ='Empty'place

###################FUNCTIONS###############

#Generate board
b = [['E', 'B','E','B','E','B','E','B'],
     ['B','E','B','E','B','E','B','E'],
     ['E','B','E','B','E','B','E','B'],
     ['E','E','E','E','E','E','E','E'],
     ['E','E','E','E','E','E','E','E'],
     ['R','E','R','E','R','E','R','E'],
     ['E','R','E','R','E','R','E','R'],
     ['R','E','R','E','R','E','R','E']]

def pretty_print(b):
    counter = 0
    for row in b:
        for cell in row:
            #print(counter,end=' ')
            print(cell, end='  ')
            if (counter == 7):
                counter = 0
                print('\n',end='' '')
            else:
                counter += 1
            #print(str(cell), end=' ')


# possible moves
def possible_moves(b, x, y):
    if is_capture_move_r1_valid(b, x, y, x-1, y-1, x-2, y-2) == 'valid capturing move':
        print(x-2, y-2)
    if is_capture_move_r2_valid(b, x, y, x-1, y+1, x-2, y+2) == 'valid capturing move':
        print(x-2, y+2)
    if is_capture_move_b1_valid(b, x, y, x+1, y+1, x+2, y+2) == 'valid capturing move':
        print(x+2, y+2)
    if is_capture_move_b2_valid (b, x, y, x+1, y-1, x+2, y-2) == 'valid capturing move':
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

#Test legal moves
import unittest
class Testlegalmoves(unittest.TestCase):
    def test_is_valid_move(self):
        self.assertEqual(legalmoves.is_valid_move(b, 2, 3, 3, 4), 'valid move')
        self.assertEqual(legalmoves.is_valid_move(b, 5, 2, 4, 1), 'valid move')
        self.assertEqual(legalmoves.is_valid_move(b, 6, 1, 5, 0), 'invalid move')
        self.assertEqual(legalmoves.is_valid_move(b, 5, 2, 4, 2), 'invalid move')
        self.assertEqual(legalmoves.is_valid_move(b, 6, 7, 5, 8), 'invalid move')


#if __name__ == '__main__':
    unittest.main()

# Move a piece with error handling and throwing
def move_piece(b, x, y, x2, y2):  # it couldnt catche when i put 6 variables instead of 5 ???
    try:
        b[x][y], b[x2][y2] = b[x2][y2], b[x][y]

    except TypeError as e:
        return 'Invalid input:' + str(e)

    except IndexError as e:
        return 'Out of range input:' + str(e)

    except Exception as e:
        return e


# verifies capturing move
def is_capture_move_r1_valid(b, x1, y1, x3, y3, x2, y2):
    if 0 <= x1 <= 7 and 0 <= x2 <= 7 and 0 <= x3 <= 7 and 0 <= y1 <= 7 and 0 <= y2 <= 7 and 0 <= y3 <= 7:
        if b[x1][y1] == 'R':  # if it is R's turn
            if b[x2][y2] == b[x1 - 2][y1 - 2] == 'E' and b[x3][y3] == b[x1 - 1][y1 - 1] == 'B':  # if destspace is free
                return 'valid capturing move'
            else:
                return 'invalid capturing move'
    else:
        return 'invalid capturing move'


def is_capture_move_r2_valid(b, x1, y1, x3, y3, x2, y2):
    if 0 <= x1 >= 7 and 0 <= x2 >= 7 and o <= x3 >= 7 and 0 <= y1 >= 7 and 0 <= y2 >= 7 and 0 <= y3 >= 7:
        if b[x1][y1] == 'R':  # if it is R's turn
            if b[x2][y2] == b[x1 - 2][y1 + 2] == 'E' and b[x3][y3] == b[x1 - 1][y1 + 1] == 'B':  # if dest space is free
                return 'valid capturing move'
            else:
                return 'invalid capturing move'
    else:
        return 'invalid capturing move'


def is_capture_move_b1_valid(b, x1, y1, x3, y3, x2, y2):
    if 0 <= x1 >= 7 and 0 <= x2 >= 7 and o <= x3 >= 7 and 0 <= y1 >= 7 and 0 <= y2 >= 7 and 0 <= y3 >= 7:
        if b[x1][y1] == 'B':  # if it is B's turn
            if b[x2][y2] == b[x1 + 2][y1 + 2] == 'E' and b[x3][y3] == b[x1 + 1][y1 + 1] == 'R':  # if dest.space is free
                return 'valid capturing move'
            else:
                return 'invalid capturing move'
    else:
        return 'invalid capturing move'



def is_capture_move_b2_valid(b, x1, y1, x3, y3, x2, y2):
    if 0 <= x1 >= 7 and 0 <= x2 >= 7 and o <= x3 >= 7 and 0 <= y1 >= 7 and 0 <= y2 >= 7 and 0 <= y3 >= 7:
        if b[x1][y1] == 'B':  # if it is B's turn
            if b[x2][y2] == b[x1 + 2][y1 - 2] == 'E' and b[x3][y3] == b[x1 + 1][y1 - 1] == 'R':  # if dest. space free
                return 'valid capturing move'
            else:
                return 'invalid capturing move'
    else:
        return 'invalid capturing move'


# make capturing move,  considering the move is legal
def capturring_move(b, x1, y1, x3, y3, x2, y2):
    b[x3][y3] = 'E'
    b[x1][y1], b[x2][y2] = b[x2][y2], b[x1][y1]
    pretty_print(b)  # why this became necessary??



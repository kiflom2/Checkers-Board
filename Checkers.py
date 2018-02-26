# R ='Red' piece
# B ='Black' Piece
# E ='Empty'place

###################FUNCTIONS###############

PIECE_RED = "R"
PIECE_BLACK = "B"
PIECE_EMPTY = "_"

# Generate board
GlobalBoard = [[PIECE_EMPTY, PIECE_BLACK, PIECE_EMPTY, PIECE_BLACK, PIECE_EMPTY, PIECE_BLACK, PIECE_EMPTY, PIECE_BLACK],
               [PIECE_BLACK, PIECE_EMPTY, PIECE_BLACK, PIECE_EMPTY, PIECE_BLACK, PIECE_EMPTY, PIECE_BLACK, PIECE_EMPTY],
               [PIECE_EMPTY, PIECE_BLACK, PIECE_EMPTY, PIECE_BLACK, PIECE_EMPTY, PIECE_BLACK, PIECE_EMPTY, PIECE_BLACK],
               [PIECE_EMPTY, PIECE_EMPTY, PIECE_EMPTY, PIECE_EMPTY, PIECE_EMPTY, PIECE_EMPTY, PIECE_EMPTY, PIECE_EMPTY],
               [PIECE_EMPTY, PIECE_EMPTY, PIECE_EMPTY, PIECE_EMPTY, PIECE_EMPTY, PIECE_EMPTY, PIECE_EMPTY, PIECE_EMPTY],
               [PIECE_RED, PIECE_EMPTY, PIECE_RED, PIECE_EMPTY, PIECE_RED, PIECE_EMPTY, PIECE_RED, PIECE_EMPTY],
               [PIECE_EMPTY, PIECE_RED, PIECE_EMPTY, PIECE_RED, PIECE_EMPTY, PIECE_RED, PIECE_EMPTY, PIECE_RED],
               [PIECE_RED, PIECE_EMPTY, PIECE_RED, PIECE_EMPTY, PIECE_RED, PIECE_EMPTY, PIECE_RED, PIECE_EMPTY]]

# pretty_print(GlobalBoard)
# print("\n\n")
# pretty_print(GlobalBoard[::-1])

GlobalBoard = GlobalBoard[::-1]


# TODO: generate empty board
# TODO: convert all to tupple

def transpose(cord):
    # return [cord[1],cord[0]]
    return (cord[1], cord[0])

def transposeBoard(brd):
    # TODO: Assignment FEB 25
    return brd[::-1]
    # return [cord[1],cord[0]]
    # return (cord[1], cord[0])


def pretty_print(b):
    brd = b[::-1]
    counter = 0
    for row in brd:
        for cell in row:
            # print(counter,end=' ')
            print(cell, end='      ')
            if (counter == 7):
                counter = 0
                print("\n\n", end='')
            else:
                counter += 1
            # print(str(cell), end=' ')



def isValid(cord):
    return cord[0] >= 0 and cord[0] < 8 and cord[1] >= 0 and cord[1] < 8  # k what is this going to retun ?


def isEmpty(b, cord):
    return b[cord[0]][cord[1]] == PIECE_EMPTY  # k is this going to return PIECE_EMPTY  for every isEmpty(b, cord)?


def getType(b, cord):
    if isRed(b, cord):  # k do we need to add this?,  if isRed(b, cord) == PIECE_RED
        return PIECE_RED  # return PIECE_RED
    elif isEmpty(b, cord):
        return PIECE_EMPTY
    elif isBlack(b, cord):
        return PIECE_BLACK
    else:
        print("What the hell how did you get here")


def isBlack(b, cord):
    cord = transpose(cord)
    return b[cord[0]][cord[1]] == PIECE_BLACK


# k isnt this should be like:
# k def isBlack(b,cord):
# k     if b[cord[0]][cord[1]] == PIECE_BLACK
# k     return PIECE_BLACK


def isRed(b, cord):
    cord = transpose(cord)
    return b[cord[0]][cord[1]] == PIECE_RED


# setCord(GlobalBoard, (3,3), PIECE_RED)
def setCord(b, cord, color):
    cord = transpose(cord)
    # b[3][3]=PIECE_RED
    # b[x][y]=color
    # b(cord)=color
    b[cord[0]][cord[1]] = color



# k isnt this should be like
# k def isRed(b,cord):
# k     if b[cord[0]][cord[1]] == PIECE_RED
# k     return PIECE_RED

# def toLeft(x,y,PieceType="B",times=1):
# return [(x-(direction*times)),(y-(times *direction))]
def toLeft(cord, PieceType=PIECE_RED, times=1):
    cord = transpose(cord)
    direction = -1 * times
    if PieceType == PIECE_BLACK:
        direction *= -1 * times
    return (cord[0] + direction, cord[1])


# toRight(toLeft(x,y))
# K why we do need times?, cant we use 1 on the function?


def toRight(cord, PieceType=PIECE_RED, times=1):
    cord = transpose(cord)
    direction = 1 * times
    if PieceType == PIECE_BLACK:
        direction *= -1 * times
    return (cord[0] + direction, cord[1])


def toFront(cord, PieceType=PIECE_RED, times=1):
    direction = 1 * times
    if PieceType == PIECE_BLACK:
        direction *= -1 * times  # can we say, direction = -1 or direction = -1*times
    return (cord[0], cord[1] + direction)


def toBack(cord, PieceType=PIECE_RED, times=1):
    cord = transpose(cord)
    direction = -1 * times
    if PieceType == PIECE_BLACK:
        direction *= -1 * times  # K can we say, direction = 1 or direcetion = 1*times
    return (cord[0], cord[1] + direction)


def jumpRight(cord, PieceType=PIECE_RED, Forward=True):  # do we need to define Forward?
    cord = transpose(cord)
    if Forward:
        return toRight(toFront(cord, PieceType, 2), PieceType, 2)
    else:
        return toRight(toBack(cord, PieceType, 2), PieceType, 2)


def jumpLeft(x, y, PieceType=PIECE_RED, Forward=True):
    cord = transpose(cord)
    if Forward:
        return toLeft(toFront(x, y, PieceType, 2), PieceType, 2)
    else:
        return toLeft(toBack(x, y, PieceType, 2), PieceType, 2)


def jumpRightBlack(cord, pieceType=PIECE_BLACK, Forward=True):
    cord = transpose(cord)
    if Forward:
        return toRight(toFront(cord, PieceType, 2), PieceType, 2)
    else:
        return toRight(toback(cord, PieceType, 2), pieceType, 2)


def jumpLeftBlack(cord, pieceType=PIECE_BLACK, Forward=True):
    cord = transpose(cord)
    if Forward:
        return toLeft(toFront(cord, PieceType, 2), PieceType, 2)
    else:
        return toLeft(toback(cord, PieceType, 2), pieceType, 2)


# TODO: verify this works and fix
# TODO: right a test for this function
def possible_moves(b, cord):
    cord = transpose(cord)
    moves = []
    pieceType = getType(b, cord)
    if isEmpty(b, cord):
        return []
    # try right
    moves.append(toRight(toFront(cord, pieceType), pieceType))
    moves.append(toLeft(toFront(cord, pieceType), pieceType))
    moves.append(toRight(toBack(cord, pieceType), pieceType))
    moves.append(toLeft(toBack(cord, pieceType), pieceType))
    # TODO: below part isn't working using *times for multiple jump moves
    moves.append(toRight(toFront(cord, pieceType, 2), pieceType, 2))
    moves.append(toLeft(toFront(cord, pieceType, 2), pieceType, 2))
    moves.append(toRight(toBack(cord, pieceType, 2), pieceType, 2))
    moves.append(toLeft(toBack(cord, pieceType, 2), pieceType, 2))
    result = []
    for m in moves:
        if isValid(m) and isEmpty(b, m):
            result.append(m)
    return result


# TODO: finish the jumps there should be four jumps


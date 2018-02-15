# Test legal moves
import unittest

import Checkers

legalmoves = []


cell = (2, 2)
pieceType = Checkers.PIECE_RED

class Testlegalmoves(unittest.TestCase):

    def test_ToFront(self):
        self.assertEqual(cell[0],2)
        self.assertEqual(cell[1],2)
        # result = toRight(toFront(cell,pieceType),pieceType)
        result = Checkers.toFront(cell, pieceType)
        self.assertEqual(result[0], 2)
        self.assertEqual(result[1], 3)
        result = Checkers.toFront(cell, pieceType,2)
        self.assertEqual(result[0], 2)
        self.assertEqual(result[1], 4)
        self.assertEqual(cell[0],2)
        self.assertEqual(cell[1],2)


    def test_ToBack(self):
        self.assertEqual(cell[0],2)
        self.assertEqual(cell[1],2)
        result = Checkers.toBack(cell,pieceType)
        self.assertEqual(result[0],2)
        self.assertEqual(result[1],1)
        result = Checkers.toBack(cell, pieceType,2)
        self.assertEqual(result[0], 2)
        self.assertEqual(result[1], 0)
        self.assertEqual(cell[0],2)
        self.assertEqual(cell[1],2)

    def test_ToRight(self):
        self.assertEqual(cell[0],2)
        self.assertEqual(cell[1],2)
        result = Checkers.toRight(cell,pieceType)
        self.assertEqual(result[0],3)
        self.assertEqual(result[1],2)
        result = Checkers.toRight(cell,pieceType,2)
        self.assertEqual(result[0],4)
        self.assertEqual(result[1],2)
        self.assertEqual(cell[0],2)
        self.assertEqual(cell[1],2)

    def test_ToLeft(self):
        self.assertEqual(cell[0],2)
        self.assertEqual(cell[1],2)
        result = Checkers.toLeft(cell,pieceType)
        self.assertEqual(result[0],1)
        self.assertEqual(result[1],2)
        result = Checkers.toLeft(cell,pieceType,2)
        self.assertEqual(result[0],0)
        self.assertEqual(result[1],2)

# print("left:",Checkers.toLeft(cell))
# print("right:",Checkers.toRight(cell))
# print("front:",Checkers.toFront(cell))
# print("back:",Checkers.toBack(cell))
#
# print("leftback",Checkers.toLeft(Checkers.toBack(cell,pieceType),pieceType))
# print("leftback x 2",Checkers.toLeft(Checkers.toBack(cell,pieceType,2),pieceType,2))
# print("rightback",Checkers.toRight(Checkers.toBack(cell,pieceType),pieceType))
# print("rightback x 2",Checkers.toRight(Checkers.toBack(cell,pieceType,2),pieceType,2))
# print("rightfront",Checkers.toRight(Checkers.toFront(cell,pieceType),pieceType))
# print("rightfront x 2",Checkers.toRight(Checkers.toFront(cell,pieceType,2),pieceType,2))
# print("leftfront",Checkers.toLeft(Checkers.toFront(cell,pieceType),pieceType))
# print("leftfront x 2",Checkers.toLeft(Checkers.toFront(cell,pieceType,2),pieceType,2))

if __name__ == '__main__':
    unittest.main()

# print(possible_moves(GlobalBoard,[2,1]))
# pieceType = PIECE_BLACK
cell = [2, 2]
# print(cell)
# cell = transpose(cell)
# print(toRight(toFront(cell,pieceType),pieceType))
# print("front",toFront([2,2],pieceType))
# print("back",toBack([2,2],pieceType))
# print("right",toRight([2,2],pieceType))
# print("left",toLeft([2,2],pieceType))

# print(possible_moves(GlobalBoard,[2,2]))


# moves.append(toRight(toFront([x,y],pieceType),pieceType))
# moves.append(toLeft(toFront([x,y],pieceType),pieceType))
# moves.append(toRight(toBack([x,y],pieceType),pieceType))
# moves.append(toLeft(toBack([x,y],pieceType),pieceType))
# moves.append(toRight(toFront([x,y],pieceType,2),pieceType,2))
# moves.append(toLeft(toFront([x,y],pieceType,2),pieceType,2))
# moves.append(toRight(toBack([x,y],pieceType,2),pieceType,2))
# moves.append(toLeft(toBack([x,y],pieceType,2),pieceType,2))

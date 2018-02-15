
#Test legal moves
import unittest
import Checkers

legalmoves =[]

class Testlegalmoves(unittest.TestCase):
    def test_helpers(self):
        cell = [2,2]
        #result = toRight(toFront(cell,pieceType),pieceType)
        pieceType= Checkers.PIECE_BLACK
        result = Checkers.toFront(cell,pieceType)
        self.assertEqual(result[0],2)
        self.assertEqual(result[1],3)
        result = Checkers.toBack([2,2],pieceType)
        self.assertEqual(result[0],2)
        self.assertEqual(result[1],1)
    #def test_is_valid_move(self):
        # self.assertEqual(1,2)
        # self.assertEqual(legalmoves.is_valid_move(
        #     Checkers.GlobalBoard, 2, 3, 3, 4), 'valid move')
        # self.assertEqual(legalmoves.is_valid_move(
        #     Checkers.GlobalBoard, 5, 2, 4, 1), 'valid move')
        # self.assertEqual(legalmoves.is_valid_move(
        #     Checkers.GlobalBoard, 6, 1, 5, 0), 'invalid move')
        # self.assertEqual(legalmoves.is_valid_move(
        #     Checkers.GlobalBoard, 5, 2, 4, 2), 'invalid move')
        # self.assertEqual(legalmoves.is_valid_move(
        #     Checkers.GlobalBoard, 6, 7, 5, 8), 'invalid move')


if __name__ == '__main__':
    unittest.main()




#print(possible_moves(GlobalBoard,[5,2]))
#print(possible_moves(GlobalBoard,[2,1]))
#pieceType = PIECE_BLACK
cell = [2,2]
#print(cell)
#cell = transpose(cell)
#print(toRight(toFront(cell,pieceType),pieceType))
#print("front",toFront([2,2],pieceType))
#print("back",toBack([2,2],pieceType))
#print("right",toRight([2,2],pieceType))
#print("left",toLeft([2,2],pieceType))

#print(possible_moves(GlobalBoard,[2,2]))



    #moves.append(toRight(toFront([x,y],pieceType),pieceType))
    #moves.append(toLeft(toFront([x,y],pieceType),pieceType))
    #moves.append(toRight(toBack([x,y],pieceType),pieceType))
    #moves.append(toLeft(toBack([x,y],pieceType),pieceType))
    #moves.append(toRight(toFront([x,y],pieceType,2),pieceType,2))
    #moves.append(toLeft(toFront([x,y],pieceType,2),pieceType,2))
    #moves.append(toRight(toBack([x,y],pieceType,2),pieceType,2))
    #moves.append(toLeft(toBack([x,y],pieceType,2),pieceType,2))

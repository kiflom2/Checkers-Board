# Checkers-Board
rd = [['W0','B1','W0','B1','W0','B1','W0','B1'], ['B1','W0','B1','W0','B1','W0','B1','W0'], ['W0','B1','W0','B1','W0','B1','W0','B1'],['B0','W0','B0','W0','B0','W0','B0','W0'], ['W0','B0','W0','B0','W0','B0','W0','B0'], ['B2','W0','B2','W0','B2','W0','B2','W0'], ['W0','B2','W0','B2','W0','B2','W0','B2'], ['B2','W0','B2','W0','B2','W0','B2','W0']] 
from __future__ import print_function
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
pretty_print(brd)

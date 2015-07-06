import math
import sys

def shift(line, step):
    line_new = []
    for i in range(len(line)):
        line_new.append(line[(i+step)%len(line)])
    return line_new

def  make_sudoku(size):
    matrix = []
    line_1 = []
    for i in range(size**2):
        line_1.append(i+1)
    for i in range(size**2):
        matrix.append(shift(line_1,(i*size)%(size**2)+i/size))
    return matrix



size = int(sys.argv[1])

print make_sudoku(size)

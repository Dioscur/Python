import sys
import math

def saddle_point(matrix):
    sadd_el = None
    sadd_i = None
    sadd_j = None
    for i in range(len(matrix)):
        if matrix[i].count(min(matrix[i])) == 1:
            sadd_temp = min(matrix[i])
            sadd_ti = i
            sadd_tj = matrix[i].index(sadd_temp)
            max_j = None
            for m in range(len(matrix)):
                if max_j < matrix[m][sadd_tj] and (m != i):
                    max_j = matrix[m][sadd_tj]
            if sadd_temp > max_j:
                sadd_el = sadd_temp
                sadd_i = i
                sadd_j = sadd_tj
            print i, sadd_temp, sadd_i, sadd_j

    if sadd_i != None : return (sadd_i,sadd_j)
    else: return False


matrix = [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [11, 10, 9, 8, 7, 6, 5, 4, 3, 2], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3], [13, 12, 11, 10, 9, 8, 7, 6, 5, 4], [14, 13, 12, 11, 10, 9, 8, 7, 6, 5], [15, 14, 13, 12, 11, 10, 9, 8, 7, 6], [16, 15, 14, 13, 12, 11, 10, 9, 8, 7], [17, 16, 15, 14, 13, 12, 11, 10, 9, 8], [18, 17, 16, 15, 14, 13, 12, 11, 10, 9], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10]]
print saddle_point(matrix)

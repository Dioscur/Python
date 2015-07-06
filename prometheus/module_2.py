import math
import sys

def convert_n_to_m(x, n, m):
    pryme = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if not isinstance (x, (int, long, str)):
        return False
    if n == 1:
        for i in str(x):
            if i != '0':
                return False
    try:
        if n == 1:
            x_10 = len (x)
        else:
            x_str = str(x)
#            x_10 = 0
#            x_m = ''
#            for i in range(len(x_str)):
#                x_10 += int(pryme.index(x[i]))*n**(len(x_str)-i-1)
            x_10 = int(x_str, n)
            if x_10 < 0: 
                return False
    except ValueError:
        return False
    if m == 1:
        return '0'*x_10
    x_m = pryme [x_10%m]
    x_10 = int (x_10/m)
    while x_10 > 0:
        y = pryme[x_10%m]
        x_m = y + x_m
        x_10 = int (x_10/m)
    return x_m


x = sys.argv[1]
n = int(sys.argv[2])
m = int(sys.argv[3])

print convert_n_to_m(x, n, m)

import math
import sys

def is_simple(a, b):
    a1 = max (a,b)
    b1 = min (a,b)
    c = 1
    while c > 0:
        c = a1 % b1
        a1, b1 = b1, c
    if a1 != 1: return False
    else: return True

def find_fraction(summ):
    if summ in (0, 1, 2):
        return False
    if is_simple(1,summ-1):
        answ = (1, summ-1)
    else: return False
    i = summ / 2
    while i > 0:
        if is_simple(i,summ-i) and float(i)/(summ-i) > float(answ[0])/answ[1]:
            answ = (i, summ-i)
            return answ
        i = i - 1
    return answ


#a1 = int(sys.argv[1])
#b1 = int(sys.argv[2])
summ = int (sys.argv[1])

print find_fraction(summ)

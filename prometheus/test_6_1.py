import math
import sys

def count_holes(n):
    dic = {'0':1, '4':1, '6':1, '8':2, '9':1}
    num = 0
    try:
        if isinstance (n, float):
            return 'ERROR'
        n_int = int(n)
        n_str = str(n_int)
        for i in n_str:
            if i in dic:
                num = num + dic[i]
        return num
    except ValueError: return "ERROR"
    except TypeError: return "ERROR"

n = sys.argv[1]
print count_holes(n)

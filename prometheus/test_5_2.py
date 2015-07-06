import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])

def counter(a, b):
    result = 0
    a_str = str (a)
    b_str = str (b)
    count = 0
    index = 0

    while index < len (b_str):
        if b_str.find(b_str[index]) == index:
            if a_str.find(b_str[index]) != -1:
                count = count + 1
        index = index + 1
    return (count)
    
print counter (a, b)

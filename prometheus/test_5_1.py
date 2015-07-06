import sys
import math

a = [1,2,1,1,3,4,5,4,6,'2',7,8,9,0,1,2,3,4,5]

def clean_list(list_in):
    list_clean = []
    index = 0

    while index < len (list_in):
        count = 0
        for i in range(index):
            if type(list_in[i]) == type(list_in[index]) and list_in[i] == list_in[index]:
                count = count + 1
        if count == 0:
            list_clean.append(list_in[index])
        index = index + 1
    return list_clean

print a
print clean_list(a)

import math
import sys

class CombStr(object):

    def __init__ (self, s = str()):
        self.substr = s

    def count_substrings(self, length):
        answ_list = []
        if length == 0:
            return 0
        for i in range (len(self.substr)-length+1):
            if not self.substr[i:i+length] in answ_list:
                answ_list.append(self.substr[i:i+length])
        return len(answ_list)

s0 = CombStr('qqqqqqweqqq%')
print s0.count_substrings(0) # 0
print s0.count_substrings(1) # 4
print s0.count_substrings(2) # 5
print s0.count_substrings(5) # 7
print s0.count_substrings(15) # 0

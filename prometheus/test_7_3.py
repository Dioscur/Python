import sys
import math

class SuperStr(str):

    def is_repeatance(self, s):
        if not isinstance (s, str):
            return False
        if len(s)==0 or len(self)==0:
            return False
        return self == s * int(len(self) / len(s))

    def is_palindrom(self):
        self_cl = self.lower()
        flag = True
        for i in range(len(self_cl)/2):
            if self_cl[i] != self_cl[len(self_cl)-i-1]:
                flag = False
        return flag
####### Another variant #######
'''     try:
            return self.lower() == self[::-1].lower()
        except TypeError:
            return False          '''       


s = SuperStr('123123123123') # True
print s.is_repeatance('123') # True
print s.is_repeatance('123123') # True
print s.is_repeatance('123123123123') # True
print s.is_repeatance('12312') # False
print s.is_repeatance(123) # False
print s.is_palindrom() # False
print s # 123123123123 
print int(s) # 123123123123 
print s + 'qwe' # 123123123123qwe
p = SuperStr('123_321')
print p.is_palindrom() # True 
s = SuperStr('')
print s.is_palindrom()

print '4//////////////5'
s2 = SuperStr('')
print s2.is_repeatance('')
print s2.is_repeatance('a')

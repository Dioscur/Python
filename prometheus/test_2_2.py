import math
import sys
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])
f = 'Everybody sing a song:'+(' la'*min(1,x)+'-la'*(x-1))*y+'!'*z+'.'*(1-z)
print f

import math
import sys
x = float(sys.argv[1])
m = float(sys.argv[2])
s = float(sys.argv[3])
f = 1/(s*math.sqrt(2*math.pi))*math.exp(-(x-m)**2/(2*s**2))
print f

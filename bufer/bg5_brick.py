import sys
import math

a1 = int(sys.argv[1])
a2 = int(sys.argv[2])
a3 = int(sys.argv[3])
a4 = int(sys.argv[4])
a5 = int(sys.argv[5])
a6 = int(sys.argv[6])
a7 = int(sys.argv[7])
a8 = int(sys.argv[8])
a9 = int(sys.argv[9])
a0 = int(sys.argv[10])

a = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a0]
s = 0

for i in range(10):
  s += a[i]

print s % 3

print a

for i in range(9):
  for j in range(9-i):
    if a[j] != a [j+1]:
	a[j] = 6 - a[j] - a[j+1]
  print a[:j+1]

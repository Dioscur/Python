import sys

a = 0
b = 1
n = int(sys.argv[1])

if n == 0:
  print a
if n == 1:
  print b
if n > 1:
  for i in range(n-1):
    c = b + a
    a = b
    b = c
  print c

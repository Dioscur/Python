import sys

n = sys.argv[1]

if len(n)<6:
  n = '0'*(6-len(n))+n

print n

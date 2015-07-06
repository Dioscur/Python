import sys
import math

n = int(sys.argv[1])
m = int(sys.argv[2])

def super_fibonacci(n, m):
    if n <= m:
        return 1
    else:
        ring = []
        for i in range(m):
            ring.append(1)
        for i in range(n-m):
            ring.append(sum(ring[-m:]))
        return ring[len(ring)-1]

print super_fibonacci (n, m)

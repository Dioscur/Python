import sys

result = 0

for ticket in range(int(sys.argv[1]),int(sys.argv[2])+1):
  ticket = str(ticket)

  if len(ticket)<6:
    ticket = '0'*(6-len(ticket)) + ticket

  half1 = 0
  half2 = 0

  for i in ticket[:3]:
    half1 = half1 + int(i)
  for i in ticket[3:]:
    half2 = half2 + int(i)
  if half1 == half2:
    result = result + 1

print result

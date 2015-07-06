import sys

text = sys.argv[1:]
text.reverse()

output = text[0]
for i in text[1:]:
  output = output + ' ' + i

print output 

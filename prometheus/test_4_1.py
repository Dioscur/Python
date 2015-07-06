import sys

text_ = sys.argv[1].lower()
text_cl = ''

for letter in text_:
  if letter != ' ':
    text_cl = text_cl + letter
'''
Another variant
text_cl = text_.lower().replace(' ', '')
'''

flag = True
leng = len(text_cl)

for i in range(leng/2):
  if text_cl[i] != text_cl[(leng-i-1)]:
    flag = False

if flag: print 'YES'
else: print 'NO'

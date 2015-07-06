import sys

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_big = alphabet.upper()

text_or = sys.argv[1].replace(' ', '')
text_ab = ''
text_bl = []
text_answ = ''

for char in text_or:
  if alphabet.find(char) >= 0:
    text_ab = text_ab + 'a'
  elif alphabet_big.find(char) >= 0:
    text_ab = text_ab + 'b'

for i in range(len(text_ab)/5):
  text_bl.append(text_ab[(5*i):(5*(i+1))])

for block in text_bl:
  text_answ = text_answ + alphabet[key.find(block)]

print text_answ

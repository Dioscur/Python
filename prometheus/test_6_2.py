import math
import sys

def encode_morze(text):
    morse_code = {"A" : ".-", "B" : "-...", "C" : "-.-.", "D" : "-..", "E" : ".", "F" : "..-.", "G" : "--.", "H" : "....", "I" : "..", "J" : ".---", "K" : "-.-", "L" : ".-..", "M" : "--", "N" : "-.", "O" : "---", "P" : ".--.", "Q" : "--.-", "R" : ".-.", "S" : "...", "T" : "-", "U" : "..-", "V" : "...-", "W" : ".--", "X" : "-..-", "Y" : "-.--", "Z" : "--.."}
    text_dert = text.upper().strip().split()
    morse = ''
    for word in text_dert:
        signal = 0
        for char in word:
            if char in morse_code:
                signal += 1
        if signal:
            for char in word:
               if char in morse_code:
                   m = morse_code[char]
                   for item in m:
                       if item == '-':
                           morse += '^^^_'
                       elif item == '.':
                           morse += '^_'
                   morse += '__'
            morse += '____'
    morse = morse [:-7]
    return morse

text = sys.argv[1]
print encode_morze(text)

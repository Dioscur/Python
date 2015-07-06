import sys
import math

def find_most_frequent(text_dert):
    punkt = '(,.:;!?-);'
    text = ''
    text_dict = {0: []}
    for char in text_dert.lower().strip():
        if char in punkt: text += ' '
        else: text += char
    text_list = text.split()
    for word in text_list:
        numb = text_list.count(word)
        if numb in text_dict and not word in text_dict[numb]:
            text_dict[numb].append(word)
        elif not numb in text_dict:
            text_dict[numb] = [word]
    text_dict.get(max(text_dict.keys())).sort()
    return text_dict.get(max(text_dict.keys()))


text = sys.argv[1]
print find_most_frequent(text)

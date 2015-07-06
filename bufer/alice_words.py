import sys
import math

list_punkt = '(,.:;!?-);\'\"`\n'

dict_answ = {}

with open ('alice.txt') as file_alice:
#with open ('alice_1.txt') as file_alice:
    for line in file_alice:
        line = line.lower().strip()
        line_lst = line.split()
        for word in line_lst:
            word_cl = ''
            for char in word:
                if not char in list_punkt:
                    word_cl += char
            if word_cl not in dict_answ:
                dict_answ[word_cl] = 1
            else:
                dict_answ[word_cl] = dict_answ[word_cl] + 1

    print 'alice =', dict_answ['alice']

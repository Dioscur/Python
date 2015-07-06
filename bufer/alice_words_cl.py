import sys
import math

def top_words(top = 10, list_exclud = []):
    with open ('alice.txt') as file_alice:
        text = file_alice.read()

    dict_answ = {}

    text = text.lower().strip()
    line_lst = text.split()
    for word in line_lst:
        word = word.strip('(,.:;!-?);\'\"`\n')
        dict_answ[word] = dict_answ.get(word, 0) + 1

    list_reverce = []
    for tupl in dict_answ.items():
        list_reverce.append((tupl[1],tupl[0])) 
    list_reverce.sort(reverse = True)
#    for v, k in list_reverce[:top]:
#        print k, v
    j = 0
    for i in range(top):
        while list_reverce[j][1] in list_exclud:
            j += 1
        print list_reverce[j][1], '=', list_reverce[j][0]
        j += 1

#fil = sys.argv[2]
top = int(sys.argv[1])
list_exclud = ['the', 'it']
list_exclud = []

top_words (top, list_exclud)

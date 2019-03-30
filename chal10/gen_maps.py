#!/usr/bin/python3.7
from itertools import repeat
from string import ascii_uppercase
from json import dumps

def analyse_freq(text):
    freq = dict(zip(ascii_uppercase, repeat(0)))
    most_common = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'D', 'L', 'U', 'C', 'M', 'F', 'W', 'G', 'Y', 'P', 'B', 'V', 'K', 'X', 'J', 'Q', 'Z']
    for i in text:
        freq[i]+=1
    s = sorted(freq, key=(lambda x: freq[x]), reverse=True)
    return dict(zip(s, most_common))

texts = [open("spam/{}".format(i)).read() for i in range(7)]

for i, mapping in enumerate(map(analyse_freq, texts)):
    open("mappings/{}".format(i), "w").write(dumps(mapping))


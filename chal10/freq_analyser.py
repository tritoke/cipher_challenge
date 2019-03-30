#!/usr/bin/python3
from itertools import repeat
from string import ascii_uppercase
from argparse import ArgumentParser
import matplotlib.pyplot as plt
import numpy as np
from os import getcwd

CWD = getcwd() + "/"

parser = ArgumentParser(description="Analyse the frequency of letters in a text file.")
parser.add_argument("file", help="the file containing the text to analyse")

file = parser.parse_args().file
freq = dict(zip(ascii_uppercase, repeat(0)))

data = filter(lambda x: x<128, open(file, "rb").read())
letters = "".join(filter(lambda c:c.isalpha(), map(chr, data))).upper()
for i in letters:
	freq[i]+=1

text_length = len(letters)

percents = {i:j/text_length for i, j in freq.items()}
english_distribution = {i:float(j) for i,j in map(lambda x: x.split(','), open(CWD + "../resources/english_letter_freqs").read().split())}

# regenerate the english letter frequencies used as a comparison to the ciphertext
# open(CWD + "../resources/english_letter_freqs", "w").write("\n".join("{},{}".format(*i) for i in percents.items()))

fig, ax = plt.subplots()
index = np.arange(len(ascii_uppercase))
bar_width = 0.35
opacity = 0.8
r1 = plt.bar(index, english_distribution.values(), bar_width, alpha=opacity, color='b', label='english')
r1 = plt.bar(index+bar_width, percents.values(), bar_width, alpha=opacity, color='r', label='ciphertext')
plt.xlabel('letter')
plt.ylabel('frequency')
plt.title('Frequency Analysis')
plt.xticks(index+bar_width, list(ascii_uppercase))
plt.legend()

plt.savefig(CWD + "../freq_out.png")
plt.show()

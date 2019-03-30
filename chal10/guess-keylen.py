#!/usr/bin/python3
from os import getcwd
import sys
sys.path.append(getcwd()+"/../modules/")

from argparse import ArgumentParser
from string import ascii_uppercase
from score import ioc
from functools import reduce
from itertools import takewhile
from math import gcd

parser = ArgumentParser()
parser.add_argument("file", type=str, help="the file to analyse")
file = parser.parse_args().file

data = filter(lambda x: x<128, open(file, "rb").read())
letters = "".join("".join(filter(lambda x: x.upper() in ascii_uppercase, map(chr, data))).split())

scores = [sum(ioc("".join(letters[j::i])) for j in range(i))/i for i in range(1, 200)]
sorted_scores = sorted(scores, reverse=True)

def diff(x):
    i = sorted_scores.index(x)
    return abs(sorted_scores[i] - sorted_scores[i+1])

scores_of_multiples = takewhile(lambda x: diff(x)<0.1, sorted_scores)
indicies_of_multiples = map(lambda x: scores.index(x)+1, scores_of_multiples) # +1 to offset the array notation and get actual key length

keylen = reduce(gcd, indicies_of_multiples)

if keylen == 1: # probably failed to guess the key length so default and print the 
    print("Failed to find key length, try to look for high values of IOC that have key lengths that are multiples of each other in the below table.")
    print()
    print("Key Length : Index Of Coincidence")
    for i, j in enumerate(scores[:50]):
        print("{:<2}:{:.6f}".format(i+1, j))
else:
    print("found key length of {}".format(keylen))


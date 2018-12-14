#!/usr/bin/python3
from os import getcwd
import sys
sys.path.append(getcwd()+"/../modules/")

from argparse import ArgumentParser
from string import ascii_uppercase
from score import ioc
from functools import reduce

parser = ArgumentParser()
parser.add_argument("file", type=str, help="the file to analyse")
file = parser.parse_args().file

data = filter(lambda x: x<128, open(file, "rb").read())
letters = "".join("".join(filter(lambda x: x.upper() in ascii_uppercase, map(chr, data))).split())

scores = [sum(ioc("".join(letters[j::i])) for j in range(i))/i for i in range(1, 21)]
print("\n".join(map(lambda x: "{}:{:.5f}".format(x[0]+1, x[1]), enumerate(scores))))

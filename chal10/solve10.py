#!/usr/bin/python3.7
from os import getcwd
import sys
sys.path.append(getcwd()+"../modules/")

from string import ascii_uppercase
from itertools import zip_longest, cycle
from json import loads
data = filter(lambda x: x<128, open("../challenges/10b.txt", "rb").read())
text = "".join(map(chr, data))
letters = "".join("".join(filter(lambda x: x.upper() in ascii_uppercase, text)).split())

mono_alphabet_ciphers = ["".join(letters[j] for j in range(i, len(letters), 7)) for i in range(7)]

mappings = [loads(open("mappings/{}".format(i)).read()) for i in range(7)]

mapped = ["".join(map(lambda x: mappings[i][x], mono_alphabet_ciphers[i])) for i in range(7)]

def print_subbed(subbed_arr):
    deciphered_letters = "".join(map(lambda x: "".join(x), zip_longest(*subbed_arr, fillvalue="z")))
    pos = 0
    for i in text:
        if i in ascii_uppercase:
            sys.stdout.write(deciphered_letters[pos])
            pos += 1
        else:
            sys.stdout.write(i)
    print() # add a newline character to the end
    return deciphered_letters

deciphered = print_subbed(mapped)

open("helpful", "w").write(":".join(map(lambda x: "{}{}".format(*x), zip(cycle(range(7)), "".join(deciphered)))))

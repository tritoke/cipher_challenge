#!/usr/bin/python3.7
from string import ascii_uppercase
from os import mkdir
from os.path import isdir

if not isdir("./spam/"): mkdir("./spam/")

data = filter(lambda x: x<128, open("../challenges/10b.txt", "rb").read())
letters = "".join("".join(filter(lambda x: x.upper() in ascii_uppercase, map(chr, data))).split())

for i in range(7):
    open("./spam/{}".format(i), "w").write("".join(letters[i::7]))


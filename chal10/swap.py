#!/usr/bin/python3.7
from argparse import ArgumentParser
from string import ascii_lowercase
from json import loads, dumps

parser = ArgumentParser()
parser.add_argument("i", help="the mapping to change", type=int, choices=list(range(7)))
parser.add_argument("a", help="whatever mapped to char a will now map to b", type=str, choices=list(ascii_lowercase))
parser.add_argument("b", help="whatever mapped to char b will now map to a", type=str, choices=list(ascii_lowercase))
args = parser.parse_args()

i, a, b = args.i, args.a.upper(), args.b.upper()

mapping = loads(open("mappings/{}".format(i)).read())

# what maps to a and b?
new_mapping = {}
for key in mapping:
    if mapping[key] == a:
        new_mapping[key] = b
    elif mapping[key] == b:
        new_mapping[key] = a
    else:
        new_mapping[key] = mapping[key]

open("mappings/{}".format(i), "w").write(dumps(new_mapping))

from os import getcwd
import sys
sys.path.append(getcwd())

from score import *
from itertools import *
from functools import *

data = map(chr, filter(lambda x: x < 128, open("challenges/7.txt", "rb").read()))
text = "".join("".join(data).split())

def transpose(table, block):
	out = []
	try: 
		for i, j in enumerate(block):
			out.append(block[table[i]])
		return "".join(out)
	except IndexError:
		return "XXXXX"

plaintext_candidates = []

for num_columns in range(4, 11):
	step = len(text)//num_columns
	columns = [text[i:i+step] for i in range(0, len(text), step)][:num_columns]
	blocks = [[column[index] for column in columns] for index in range(len(columns[0]))]
	
	genTables = lambda blockLen: list(map(lambda x: partial(transpose, dict(zip(x, range(blockLen)))), permutations(range(blockLen))))
	
	tables = genTables(num_columns)
	func = lambda x: "".join(map(x, blocks)).lower()
	possible_plaintexts = sorted(filter(lambda x: "xxxxx" not in x, map(func, tables)), key=ioc)
	plaintext_candidates.append(max(possible_plaintexts[-10:], key=score))
print(max(plaintext_candidates, key=score))
	
	

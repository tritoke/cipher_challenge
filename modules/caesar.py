#!/usr/bin/python3.7
from string import ascii_lowercase, ascii_uppercase

alphabet = ascii_uppercase + ascii_lowercase

def cipher(offset, text):
    out = ""
    for i in text:
        if i in alphabet:
            caps_offset = ord("A") + (32*i.islower())
            beans = (ord(i) - caps_offset + offset) % 26
            out += chr(beans + caps_offset)
        else:
            out += i
    return out

if __name__ == '__main__':
	print("offset 13 of\n'Nqq guerr gb svir, gvzrf gung ahzore ol frira, gura unyir gung ahzore. Jung qb lbh trg?'\nis: ", end="\n'")
	print(cipher(13, "Nqq guerr gb svir, gvzrf gung ahzore ol frira, gura unyir gung ahzore. Jung qb lbh trg?"), end="'\n")


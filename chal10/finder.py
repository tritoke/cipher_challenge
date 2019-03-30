#!/usr/bin/python3.7
from re import findall
while True:
    find = "".join(input("> ").split())
    data = open("helpful").read()
    print(findall((".{}:"*len(find)).format(*find), data))

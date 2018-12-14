#!/usr/bin/python3.7
from requests import get
from bs4 import BeautifulSoup
from multiprocessing import Pool
from re import search
from functools import partial
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-v", "--verbose", type=bool, default=False)
verbose = parser.parse_args().verbose
base_url = "https://www.cipherchallenge.org/challenges/challenge-{}/"
urls = [base_url.format(i) for i in range(1, 11)]

def downloader(url):
    link_number = int(search(r"\d+", url).group())
    if link_number == 4: # look I don't know who's fantastic idea not having normal links was
        url = "https://www.cipherchallenge.org/challenges/35230-2/"
    elif link_number == 10:
        url = "https://www.cipherchallenge.org/challenges/competition-challenge-10"
    req = get(url)
    if req.ok:
        print("getting challenge {} succeded".format(link_number))
        return req.text
    else:
        print("getting challenge {} failed".format(link_number))
        return ""

p = Pool(10)
pages = p.map(downloader, urls)
p.close()
p.join()

soups = map(BeautifulSoup, filter(lambda x: x!="", pages))

if verbose:
    print()
    print("="*80 + "\n")
for index, soup in enumerate(soups):
    index+=1
    if verbose: print("-"*80)
    is_a = True
    for div in soup.find_all("div", {"class", "challenge__content"}):
        if is_a:
            is_a = False
            if index not in [2]:
                a = "".join(div.find("p").strings)
            else:
                a = "\n".join(map(lambda x: x.string, div.find_all("p")))
            if verbose:
                print("challenge {} part a".format(index))
                print(a)
            open("challenges/{}a.txt".format(index), "w").write(a)
        else:
            if index not in [2, 3]:
                b = "".join(div.find("p").strings)
            else:
                b = "\n".join(map(lambda x: x.string, div.find_all("p")))
            if verbose:
                print("challenge {} part b".format(index))
                print(b)
            open("challenges/{}b.txt".format(index), "w").write(b)
        if verbose: print("-"*80)
    if verbose: print("\n" + "="*80 + "\n")


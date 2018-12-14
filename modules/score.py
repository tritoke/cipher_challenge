#!/usr/bin/python3.7
from string import ascii_lowercase
words = open("../resources/wordlist.txt").read().split("\n")

def score(text):
    block = "".join(filter(lambda x: x in ascii_lowercase, text.lower()))
    return sum(map(lambda word: block.count(word), words))

def ioc(text):
    t = text.lower()
    def thing(x):
        nx = text.count(x)
        return nx*(nx-1)
    s = sum(map(thing, ascii_lowercase))
    c = 26
    N = len(t)
    return (c*(s/(N*(N-1))))

if __name__ == '__main__':
    wordSpam = "".join(words)
    from time import time
    t0 = time()
    score(wordSpam)
    t1 = time()
    score_taken = taken = t1-t0
    print("score took {} seconds to rank a {} character long text".format(taken, len(wordSpam)))

    t0 = time()
    ioc(wordSpam)
    t1 = time()
    ioc_taken = taken = t1-t0
    print("index of coincidence took {} seconds to rank a {} character long text".format(taken, len(wordSpam)))

    print("\nthis makes ioc {} times faster than score".format(score_taken/ioc_taken))
    print("however score is better at determining whether a given text is english, ioc merely gives a strong indication")

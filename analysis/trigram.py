#!/usr/bin/python3
from string import ascii_uppercase

def get_bigrams(letters):
    letters = "".join(filter(lambda x: x in ascii_uppercase, letters.upper()))
    bigrams = [letters[i:i+2] for i in range(0, len(letters), 2)]
    freq = {bigram:bigrams.count(bigram) for bigram in set(bigrams)}
    return freq

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("file")
    file = parser.parse_args().file
    data = open(file, "rb").read()
    letters = "".join("".join(map(chr, filter(lambda x: x<128, data))).split())
    bigram_frequencies = get_bigrams(letters)
    print("\n".join(list(map(lambda x: "{}:{}".format(x, bigram_frequencies[x]), sorted(bigram_frequencies, key=(lambda x:bigram_frequencies[x]), reverse=True)))[:10]))

#!/usr/bin/python3
from string import punctuation, digits
from sys import argv, exit as sysexit
from re import sub

# check for syntax errors
if len(argv)==1:
    print("usage: {} text".format(argv[0]))
    print("options: ")
    print("-f <file> ==> open file and analyse the text inside")
    sysexit(0)

elif len(argv)==2 and "python" in argv[0]:
    print("usage: {} text".format(argv[:2]))
    print("options: ")
    print("-f <file> ==> open file and analyse the text inside")
    sysexit(0)

def analyse(text):
    # make dictionaru to store the words and their counts
    most_common = {}

    # make a table relating all punctuation and digits characters to None
    table = str.maketrans(dict.fromkeys(punctuation + digits))

    # make the text lowercase then translate it with the table above
    # this translation relates to removing all punctuation and digits
    text = text.lower().translate(table)

    # this is a regex to remove all non ascii characters
    text = sub("[^\x00-\x7F]+", "", text)

    # split the text on white space and take all length three sections
    words = list(filter(lambda x: len(x)==2, text.split()))

    # for each unique word count how many times it appears and relate the word to that count in the most_common dict
    for word in set(words):
        most_common[word] = words.count(word)

    # get my list of the most common two letter words in the english language
    cleartext_common = open("../resources/two_letters").read().lower().translate(table).split()

    # sort the list from largest to smallest and return a two-tuple of the number of times the word appears and the word itself
    out = sorted([(most_common[word], word) for word in set(words)],reverse=True)

    # format the top 25 words along with the top 25 two letter words
    top = map(lambda x: "{}:\t{}\t==>\t{}".format(out[x][1],out[x][0],cleartext_common[x]), range(25))

    # not a clue what this line does but don't touch it for gods sake.
    print("\n".join(top))

if len(argv) == 2:
    analyse(argv[1])

elif len(argv) == 3:
    if "python" in argv[0]:
        analyse(argv[2])
    else:
        analyse(open(argv[2]).read())

elif len(argv) == 4:
    analyse(open(argv[3]).read())





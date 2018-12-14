#!/usr/bin/python3.7
from string import ascii_lowercase
from itertools import product
from functools import reduce

def cipher(text, encrypt_mode, keyword):
    # encrypt mode is a boolean which stores whether we are encrypting or decrypting
    alphabet = ascii_lowercase.replace("j", "")
    text = "".join(filter(lambda x: x in  ascii_lowercase, "".join(text.lower().replace("j","i").split())))
    keyword = keyword.lower().replace("j", "i")

    if len(text)%2==1:
        text+="x"

    blocks = [text[i:i+2] for i in range(0,len(text), 2)]

    for index, block in enumerate(blocks):
        if block[0] == block[1]:
            blocks[index] = block[0]+"x"

    matrix = []
    letters = []

    for i in (keyword.lower() + alphabet):
        if i not in letters: letters.append(i)

    for i in range(0, 25, 5):
        matrix.append(letters[i:i+5])

    def getPosition(x):
        for i, j in product(range(5), repeat=2):
            if matrix[i][j] == x:
                return i,j
        print("wtf: {}".format(x))

    cipherText = []

    for b1, b2 in blocks:
        x1, y1 = getPosition(b1)
        x2, y2 = getPosition(b2)
        if x1==x2:
            if y1==4: y1=-1
            if y2==4: y2=-1
            cipherText.append(matrix[x1][y1+(encrypt_mode)-(not encrypt_mode)])
            cipherText.append(matrix[x2][y2+(encrypt_mode)-(not encrypt_mode)])
        elif y1==y2:
            if x1==4: x1=-1
            if x2==4: x2=-1
            cipherText.append(matrix[x1+(encrypt_mode)-(not encrypt_mode)][y1])
            cipherText.append(matrix[x2+(encrypt_mode)-(not encrypt_mode)][y2])
        else:
            cipherText.append(matrix[x1][y2])
            cipherText.append(matrix[x2][y1])

    if not encrypt_mode:
        if cipherText[-1] == "x":
            cipherText.pop()
        for index, char in enumerate(cipherText):
            if char == "x":
                cipherText[index] = cipherText[index-1]
        return("".join(cipherText).lower())
    else:
        return "".join(cipherText).upper()

    table = {}

if __name__ == '__main__':
    original = "hide the gold in the tree stump"
    key = "playfairexample"
    ciphered = cipher(original, True, key)
    deciphered = cipher(ciphered, False, key)
    print("'{}' encrypted with key '{}' is: '{}'".format(original, key, ciphered))
    print("'{}' decrypted with key '{}' is: '{}'".format(ciphered, key, deciphered))
    open("../resources/small_playfaired", "w").write(cipher(open("../resources/small_text").read(), True, "shadow"))


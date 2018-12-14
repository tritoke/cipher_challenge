#!/usr/bin/python3.7
from string import ascii_uppercase as alphabet
from itertools import cycle

encrypt_table = {letter: {alphabet[i]:alphabet[(i+alphabet.find(letter))%len(alphabet)] for i in range(len(alphabet))} for letter in alphabet} 
decrypt_table = table = {letter: {alphabet[(i+alphabet.find(letter))%len(alphabet)]:alphabet[i] for i in range(len(alphabet))} for letter in alphabet} 

make_text = lambda text, key: zip(text.upper(), cycle(key.upper()))

def encipher(text):
    ciphertext = ""
    for plain, key in text:
        if plain in alphabet:
            ciphertext += encrypt_table[key][plain]
        else:
            ciphertext += plain
    return ciphertext

def lookup_decrypt(text):
    plaintext = ""
    for plain, key in text:
        if plain in alphabet:
            plaintext += decrypt_table[key][plain]
        else:
            plaintext += plain
    return plaintext.lower()

def decipher(text):
    plaintext = ""
    for ciphered, key in text:
        if ciphered in alphabet:
            for keys in table[key]:
                if encrypt_table[key][keys] == ciphered:
                    plaintext += keys
        else:
            plaintext += ciphered
    return plaintext.lower()

if __name__ == '__main__':
    print("test encryption and decryption:\n")
    original = "I think that bananas are just about, [({the fucking be/+c*#test thi#*28£pcngs evererrr})]"
    key = "supersecretkey"
    print(original, key)
    t = make_text(original, key)
    ciphered = encipher(t)
    print(ciphered)
    ct = make_text(ciphered, key)
    deciphered = lookup_decrypt(ct)
    print(deciphered)
    from time import time

    iterations = 10000
    print("\n\ntime trials")
    print("for {} iterations:".format(iterations))

    t0 = time()
    for _ in range(iterations):
        make_text(ciphered, key)
    t1 = time()

    zip_time = taken = t1-t0
    avg = taken/iterations

    print("\nmaking zip takes {} seconds".format(taken))
    print("for an average of: {} seconds".format(avg))

    t0 = time()
    for _ in range(iterations):
        lookup_decrypt(make_text(ciphered, key))
    t1 = time()

    taken = (t1-t0) - zip_time
    lookup_avg = avg = taken/iterations

    print("\nlookup takes {} seconds".format(taken))
    print("for an average of: {} seconds".format(avg))

    t0 = time()
    for _ in range(iterations):
        decipher(make_text(ciphered, key))
    t1 = time()

    taken = (t1-t0) - zip_time
    decipher_avg = avg = taken/iterations

    print("\noriginal takes {} seconds".format(taken))
    print("for an average of: {} seconds".format(avg))

    print("\nthis makes lookup {} times faster than the original function".format(decipher_avg/lookup_avg))


# p59

from itertools import *

def decrypt(pword, data):
    cpy = [_ for _ in data]
    key = [ord(_) for _ in pword]
    for i in range(len(cpy)):
        cpy[i] ^= key[i % 3]
    return cpy

def toText(data):
    msg = ''
    for n in data:
        msg += chr(n)
    return msg

f = open('./input/59_cipher.txt')
data = [int(n) for n in f.read().split(',')]

for pword in permutations('abcdefghijklmnopqrstuvwxyz', 3):
    decrypted = decrypt(pword, data)
    text = toText(decrypted)
    if ' and' in text:
        print(''.join(pword))
        print(text)
        print(sum(decrypted))

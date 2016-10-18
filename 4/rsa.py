#!/usr/bin/python3
import argparse
from bitarray import bitarray


def rsa_encrypt(bits, key):
    return bits


def rsa_decrypt(bits, key):
    return bits

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='RSA algorithm utility')
    parser.add_argument('path', help='path to file for encryption/decryption')
    parser.add_argument('--d', help='decrypt', action='store_true')
    args = parser.parse_args()
    path = args.path
    to_decrypt = args.d
    file = open(path, 'rb')
    text = bitarray()
    text.fromfile(file)
    file.close()
    if to_decrypt:
        print('Start decryption for file:', path)
        text = rsa_decrypt(text, 65537)
        print('Finish decryption.')
    else:
        print('Start encryption for file:', path)
        text = rsa_encrypt(text, 65537)
        print('Finish encryption.')
    file = open(path, 'wb')
    file.write(text.tobytes())
    file.close()

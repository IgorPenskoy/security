#!/usr/bin/python3
import argparse
from generate_keys import *
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Signature creating utility.')
    parser.add_argument('path', help='Path to file for signature')
    args = parser.parse_args()

    # creation of signature
    try:
        f = open(args.path, 'rb')
        plaintext = f.read()
        f.close()
        try:
            private_key = RSA.importKey(open(sender_private_file_name, 'rb').read())
            file_hash = SHA256.new(plaintext)
            signature = PKCS1_v1_5.new(private_key)
            signature = signature.sign(file_hash)

            # signature encrypt
            signature_file_name = args.path + '.sign'
            public_key = RSA.importKey(open(receiver_public_file_name, 'rb').read())
            cipher_rsa = PKCS1_OAEP.new(public_key)
            sig = cipher_rsa.encrypt(signature[:128])
            sig = sig + cipher_rsa.encrypt(signature[128:])
            f = open(signature_file_name, 'wb')
            f.write(bytes(sig))
            f.close()
        except OSError:
            print('Generate RSA keys first by running ./generate_keys.py')
            exit()
    except OSError:
        print('No such file or directory.')
        exit()

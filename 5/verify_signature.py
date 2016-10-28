#!/usr/bin/python3
import argparse
from generate_keys import *
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Signature creating utility.')
    parser.add_argument('path', help='Path to file')
    parser.add_argument('signature', help='Path to signature file')
    args = parser.parse_args()

    # decryption signature
    try:
        f = open(args.signature, 'rb')
        signature = f.read()
        f.close()
        try:
            private_key = RSA.importKey(open(receiver_private_file_name, 'rb').read())
            cipher_rsa = PKCS1_OAEP.new(private_key)
            sig = cipher_rsa.decrypt(signature[:256])
            sig = sig + cipher_rsa.decrypt(signature[256:])

            # signature verification
            try:
                f = open(args.path, 'rb')
                plaintext = f.read()
                f.close()
                try:
                    public_key = RSA.importKey(open(sender_public_file_name, 'rb').read())
                    file_hash = SHA256.new(plaintext)
                    signature = PKCS1_v1_5.new(public_key)
                    test = signature.verify(file_hash, sig)
                    if test:
                        print('Your signature is correct.')
                    else:
                        print('Your signature is not correct. File has been changed or corrupted')
                except OSError:
                    print('Keys not found.')
                    exit()
            except OSError:
                print('File not found.')
                exit()
        except OSError:
            print('Keys not found.')
            exit()
    except OSError:
        print('Signature not found.')
        exit()

#!/usr/bin/python3
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='RSA algorithm utility')
    parser.add_argument('path', help='path to file for encryption/decryption')
    parser.add_argument('--d', help='decrypt', action='store_true')
    args = parser.parse_args()
    path = args.path
    to_decrypt = args.d

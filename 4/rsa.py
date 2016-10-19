#!/usr/bin/python3
import argparse
import gmpy2


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def rsa_encrypt(byte_array, open_key, n):
    result = bytearray()
    size = int(gmpy2.ceil(n.bit_length() / 8))
    for decrypted_bytes in chunks(byte_array, size):
        decrypted = int.from_bytes(decrypted_bytes, byteorder='big', signed=False)
        encrypted = int(gmpy2.powmod(decrypted, open_key, n))
        encrypted_bytes = encrypted.to_bytes(size, byteorder='big', signed=False)
        # print(decrypted_bytes, decrypted, encrypted, encrypted_bytes)
        result.extend(encrypted_bytes)
    return result


def rsa_decrypt(byte_array, secret_key, n):
    result = bytearray()
    size = int(gmpy2.ceil(n.bit_length() / 8))
    for encrypted_bytes in chunks(byte_array, size):
        encrypted = int.from_bytes(encrypted_bytes, byteorder='big', signed=False)
        decrypted = int(gmpy2.powmod(encrypted, secret_key, n))
        decrypted_bytes = decrypted.to_bytes(int(gmpy2.ceil(decrypted.bit_length() / 8)), byteorder='big', signed=False)
        result.extend(decrypted_bytes)
        # print(decrypted_bytes, decrypted, encrypted, encrypted_bytes)
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='RSA algorithm utility')
    parser.add_argument('path', help='path to file for encryption/decryption')
    parser.add_argument('--d', help='decrypt', action='store_true')
    args = parser.parse_args()
    path = args.path
    to_decrypt = args.d
    file = open(path, 'rb')
    text = file.read()
    file.close()
    try:
        if to_decrypt:
            file = open('.rsaprivate', 'r')
            d = int(file.readline())
            print(d)
            n = int(file.readline())
            file.close()
            print('Start decryption for file:', path)
            text = rsa_decrypt(text, d, n)
            print('Finish decryption.')
        else:
            file = open('.rsapublic', 'r')
            e = int(file.readline())
            print(e)
            n = int(file.readline())
            file.close()
            print('Start encryption for file:', path)
            text = rsa_encrypt(text, e, n)
            print('Finish encryption.')
    except OSError:
        print('It looks like you do not have keys. Run rsa_keygen first.')
        exit()
    file = open(path, 'wb')
    file.write(text)
    file.close()

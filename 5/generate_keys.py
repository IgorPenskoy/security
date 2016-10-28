#!/usr/bin/python3
from Crypto.PublicKey import RSA

sender_private_file_name = '.sender_private_key'
sender_public_file_name = '.sender_public_key'
receiver_private_file_name = '.receiver_private_key'
receiver_public_file_name = '.receiver_public_key'


def generate_keys():
    key_bits_size = 2048

    # key generation sender
    private_key = RSA.generate(key_bits_size)
    f = open(sender_private_file_name, 'wb')
    f.write(bytes(private_key.exportKey('PEM')))
    f.close()
    public_key = private_key.publickey()
    f = open(sender_public_file_name, 'wb')
    f.write(bytes(public_key.exportKey('PEM')))
    f.close()

    # key generation receiver
    private_key = RSA.generate(key_bits_size)
    f = open(receiver_private_file_name, 'wb')
    f.write(bytes(private_key.exportKey('PEM')))
    f.close()
    public_key = private_key.publickey()
    f = open(receiver_public_file_name, 'wb')
    f.write(bytes(public_key.exportKey('PEM')))
    f.close()

if __name__ == '__main__':
    generate_keys()
    print('Keys for sender are in', sender_private_file_name, 'and', sender_public_file_name)
    print('Keys for receiver are in', receiver_private_file_name, 'and', receiver_public_file_name)

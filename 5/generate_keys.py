from Crypto.PublicKey import RSA

key_bits_size = 2048
# key generation sender
private_key = RSA.generate(key_bits_size)
f = open('.sender_private_key', 'wb')
f.write(bytes(private_key.exportKey('PEM')))
f.close()
public_key = private_key.publickey()
f = open('.sender_public_key', 'wb')
f.write(bytes(public_key.exportKey('PEM')))
f.close()
# key generation receiver
private_key = RSA.generate(key_bits_size)
f = open('.receiver_private_key', 'wb')
f.write(bytes(private_key.exportKey('PEM')))
f.close()
public_key = private_key.publickey()
f = open('.receiver_public_key', 'wb')
f.write(bytes(public_key.exportKey('PEM')))
f.close()

#!/usr/bin/python3
import argparse
import gmpy2

import time
RANDOM_STATE = gmpy2.random_state(int(round(time.time() * 1000)))


def get_prime_lt(num):
    prime = num - 1
    while gmpy2.is_prime(prime) is False:
        prime -= 1
    return prime


def get_coprime(x):
    y = int(gmpy2.mpz_random(RANDOM_STATE, (x - 1) // 2)) + (x - 1) // 3
    while gmpy2.gcd(x, y) != 1:
        y -= 1
    return y


def key_gen(size):
    p = get_prime_lt(2 ** (size // 2) - 1)
    q = get_prime_lt(p)
    n = gmpy2.mul(p, q)
    x = gmpy2.mul((p - 1), (q - 1))
    e = get_coprime(x)
    d = gmpy2.invert(e, x)
    return e, d, n

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='RSA algorithm utility')
    parser.add_argument('size', help='size of key in bits')
    args = parser.parse_args()
    e, d, n = key_gen(int(args.size))
    file = open('.rsapublic', 'w')
    file.write(str(e) + '\n')
    file.write(str(n))
    file.close()
    file = open('.rsaprivate', 'w')
    file.write(str(d) + '\n')
    file.write(str(n))
    file.close()

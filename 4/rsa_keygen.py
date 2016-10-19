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


def get_coprime_lt(x):
    y = x - 1
    while gmpy2.gcd(x, y) != 1:
        y -= 1
    return y


def key_gen(size):
    p = get_prime_lt(2 ** (size // 2))
    q = get_prime_lt(p)
    print(p, q)
    n = gmpy2.mul(p, q)
    print(n)
    x = gmpy2.mul((p - 1), (q - 1))
    print(x)
    e = 65537
    print(e)
    d = gmpy2.invert(e, x)
    print(d)
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

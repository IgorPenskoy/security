import argparse
from bitarray import bitarray

KEY = bitarray()
KEY.frombytes(b'ABCDEFGH')

PC_1 = [ 57, 49, 41, 33, 25, 17, 9,
			1, 58, 50, 42, 34, 26, 18,
			10, 2, 59, 51, 43, 35, 27,
			19, 11, 3, 60, 52, 44, 36,
			63, 55, 47, 39, 31, 23, 15,
			7, 62, 54, 46, 38, 30, 22,
			14, 6, 61, 53, 45, 37, 29,
			21, 13, 5, 28, 20, 12, 4]
PC_2 = [ 14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4,
			26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40,
			51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

IP = [ 58, 50, 42, 34, 26, 18, 10, 2,
				60, 52, 44, 36, 28, 20, 12, 4,
				62, 54, 46, 38, 30, 22, 14, 6,
				64, 56, 48, 40, 32, 24, 16, 8,
				57, 49, 41, 33, 25, 17,  9, 1,
				59, 51, 43, 35, 27, 19, 11, 3,
				61, 53, 45, 37, 29, 21, 13, 5,
				63, 55, 47, 39, 31, 23, 15, 7 ]

IP_REV = [40, 8, 48, 16, 56, 24, 64, 32, 
					39, 7, 47, 15, 55, 23, 63, 31,
					38, 6, 46, 14, 54, 22, 62, 30, 
					37, 5, 45, 13, 53, 21, 61, 29,
					36, 4, 44, 12, 52, 20, 60, 28, 
					35, 3, 43, 11, 51, 19, 59, 27,
					34, 2, 42, 10, 50, 18, 58, 26, 
					33, 1, 41,  9, 49, 17, 57, 25]

S1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
			0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
			4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
			15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]

S2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
				3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
				0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
				13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]

S3 = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8, 
				13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
				13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
				1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]

S4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15, 
				13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
				10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4, 
				3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]

S5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9, 
				14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
				4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14, 
				11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]

S6 = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11, 
				10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
				9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
				4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]

S7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
				13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
				1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
				6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]

S8 = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
				1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
				7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
				2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]

P = [	16,  7, 20, 21, 29, 12, 28, 17,
				 1, 15, 23, 26,  5, 18, 31, 10,
				 2,  8, 24, 14, 32, 27,  3,  9,
				19, 13, 30,  6, 22, 11,  4, 25]

E = [	32,  1,  2,  3,  4,  5,
				 4,  5,  6,  7,  8,  9,
				 8,  9, 10, 11, 12, 13,
				12, 13, 14, 15, 16, 17,
				16, 17, 18, 19, 20, 21,
				20, 21, 22, 23, 24, 25,
				24, 25, 26, 27, 28, 29,
				28, 29, 30, 31, 32,  1	]

SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1] 


def ip(bits_64):
	ip_result = bitarray()	
	for i in range(64):
		ip_result.append(bits_64[IP[i] - 1])
	return ip_result

def ip_rev(bits_64):
	ip_rev_result = bitarray()	
	for i in range(64):
		ip_rev_result.append(bits_64[IP_REV[i] - 1])
	return ip_rev_result

def bits_to_int(bits):
	out = 0
	for bit in bits:
		out = (out << 1) | bit
	return out

def int_to_bits_4(number):
	return '{:04b}'.format(number)

def s(bits_6, s_data):
	a = bitarray([bits_6[0], bits_6[-1]])
	b = bits_6[2:-1]
	a = bits_to_int(a)
	b = bits_to_int(b)
	return int_to_bits_4(s_data[a * 16 + b])

def s1(bits_6):
	return s(bits_6, S1)

def s2(bits_6):
	return s(bits_6, S2)

def s3(bits_6):
	return s(bits_6, S3)

def s4(bits_6):
	return s(bits_6, S4)

def s5(bits_6):
	return s(bits_6, S5)

def s6(bits_6):
	return s(bits_6, S6)

def s7(bits_6):
	return s(bits_6, S7)

def s8(bits_6):
	return s(bits_6, S8)

def p(bits_32):
	p_result = bitarray()
	for i in range(32):
		p_result.append(bits_32[P[i] - 1])
	return p_result

def e(bits_32):
	ext_result = bitarray()
	for i in range(48):
		ext_result.append(bits_32[E[i] - 1])
	return ext_result

def feistel(bits_32, key_48):
	bits_48 = e(bits_32)
	bits_48 ^= key_48
	b = [ bits_48[:6], bits_48[6:12], bits_48[12:18], bits_48[18:24],
			bits_48[24:30], bits_48[30:36], bits_48[36:42], bits_48[42:] ]
	s = bitarray(s1(b[0]) + s2(b[1]) + s3(b[2]) + s4(b[3]) + s5(b[4]) + s6(b[5]) + s7(b[6]) + s8(b[7]))
	return p(s)

def rotate_left(l, n):
	return l[n:] + l[:n]

def rotate_right(l, n):
	return l[-n:] + l[:-n]

def apply_permutation(num, perm):
	result = bitarray()
	for i in range(len(perm)):
		result.append(num[perm[i] - 1])
	return result

def key_gen(key_64, rev):	
	key_56 = apply_permutation(key_64, PC_1)
	keys = []
	c, d = key_56[:28], key_56[28:]
	for i in range(16):
		c = rotate_left(c, SHIFTS[i])
		d = rotate_left(d, SHIFTS[i])
		tmp = c[:]
		tmp.extend(d)
		key = apply_permutation(tmp, PC_2)
		keys.append(key)
	if rev:
		return list(reversed(keys))
	else:
		return keys

def cipher(bits_64, keys):
	bits_64 = ip(bits_64)
	l_prev = bits_64[:32]
	r_prev = bits_64[32:]
	for i in range(16):
		l_next = r_prev
		r_next = l_prev ^ feistel(r_prev, keys[i])
		l_prev = l_next
		r_prev = r_next
	l_prev.extend(r_prev)
	return ip_rev(l_prev)

def decipher(bits_64, keys):
	bits_64 = ip(bits_64)
	l_prev = bits_64[:32]
	r_prev = bits_64[32:]
	for i in range(16):
		r_next = l_prev
		l_next = r_prev ^ feistel(l_prev, keys[i])
		l_prev = l_next
		r_prev = r_next
	l_prev.extend(r_prev)
	return ip_rev(l_prev)

def encrypt(text, key_64):
	keys = key_gen(key_64, 0)
	result = bitarray()
	block = text[:64]
	i = 64
	while len(block) == 64 and i < len(text):
		result.extend(cipher(block, keys))
		i += 64
		block = text[i-64:i]
	a = bitarray('00000000')
	if len(block) != 0:
		a = bitarray(int_to_bits_4(64-len(block)))
		for i in range(8-len(a)):
			a.insert(0, 0)
		for i in range(64-len(block)):
			block.append(0)
		result.extend(cipher(block, keys))
	result.extend(a)
	return result

def decrypt(text, key_64):
	keys = key_gen(key_64, 1)
	result = bitarray()
	block = text[:64]
	i = 64
	while len(block) == 64 and i < len(text):
		result.extend(decipher(block, keys))
		i += 64
		block = text[i-64:i]
	if bits_to_int(block) != 0:
		for i in range(bits_to_int(block)):
			result.pop()
	return result

if __name__ == '__main__':
	try:
		parser = argparse.ArgumentParser(description='DES encryption application')
		parser.add_argument('path', help='path to required file')
		parser.add_argument('--d', help='decryption', action='store_true')
		args = parser.parse_args()
		path = args.path
		d = args.d
		file = open(path, 'rb')
		text = bitarray()
		text.fromfile(file)
		file.close()
		if d:
			print('Start decryption for file:', path)
			text = decrypt(text, KEY)
			print('Finish decryption. Results are in des_result')		
		else:
			print('Start encryption for file:', path)
			text = encrypt(text, KEY)
			print('Finish encryption. Results are in des_result')
		file = open('des_result', 'wb')
		file.write(text.tobytes())
		file.close()
	except OSError:
		print('File can not be processed.')
	except Exception as e:
		print('Unhandled exception occured:', e)
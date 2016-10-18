import argparse
import re
import sys
import string

REFLECTOR_B = [ 24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13,6, 14, 10, 12, 8, 4,
				1, 5, 25, 2, 22, 21, 9, 0, 19 ]

ROTOR_I 	= [ 4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23,
				20,	18, 15, 0, 8, 1, 17, 2, 9 ]

ROTOR_II 	= [ 0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6,
				25, 13, 15, 24, 5, 21, 14, 4 ]

ROTOR_III	= [ 1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22,
				6, 0, 10, 12, 20, 18, 16, 14 ]

def sum_mod_26(a, b):
	return (a + b) % 26

def diff_mod_26(a, b):
	return (a - b) % 26

class enigma(object):
	def __init__(self, l_key='A', m_key='A', r_key='A', ref='B', l_rot='3',
				 m_rot='2', r_rot='1'):
		self.config = {
			'B'       : REFLECTOR_B,
			'1'       : ROTOR_I,
			'2'       : ROTOR_II,
			'3'       : ROTOR_III,
			'1_KNOCK' : 17,
			'2_KNOCK' : 5,
			'3_KNOCK' : 22

		}
		self.ref = self.config[ref]
		self.l_rot = self.config[l_rot]
		self.m_rot= self.config[m_rot]
		self.r_rot = self.config[r_rot]
		self.l_key = ord(l_key.upper()) - ord('A')
		self.m_key = ord(m_key.upper()) - ord('A')
		self.r_key = ord(r_key.upper()) - ord('A')
		self.m_knock = self.config[m_rot + '_KNOCK']
		self.r_knock = self.config[r_rot + '_KNOCK']
	
	def encrypt(self, message):
		result = ''
		for char in message:
			result += self.char_change(char)
		return result

	def binary_encrypt(self, binary):
		result = bytearray()
		for byte in binary:
			byte = int(byte)
			result.append(self.byte_change(byte))
		return result

	def byte_change(self, byte):
		if byte in range(0, 26):
			return self.cycle(byte)
		else:
			return byte

	def char_change(self, char):
		if char in string.ascii_lowercase:
			char = ord(char) - ord('a') 
			char = self.cycle(char)
			return chr(char + ord('a'))
		elif char in string.ascii_uppercase:
			char = ord(char) - ord('A')
			char = self.cycle(char)
			return chr(char + ord('A'))
		else:
			return char

	def cycle(self, char):
		self.r_key = self.rotor_roll(self.r_key)
		if self.r_key == self.r_knock:
			self.m_key = self.rotor_roll(self.m_key)
			if self.m_key == self.m_knock:
				self.l_key = self.rotor_roll(self.l_key)
		char = sum_mod_26(char, self.r_key)
		char = self.r_rot[char]
		char = sum_mod_26(char, diff_mod_26(self.m_key, self.r_key))
		char = self.m_rot[char]
		char = sum_mod_26(char, diff_mod_26(self.l_key, self.m_key))
		char = self.l_rot[char]
		char = diff_mod_26(char, self.l_key)
		char = self.ref[char]
		char = sum_mod_26(char, self.l_key)
		char = self.l_rot.index(char)
		char = diff_mod_26(char, diff_mod_26(self.l_key, self.m_key))
		char = self.m_rot.index(char)
		char = diff_mod_26(char, diff_mod_26(self.m_key, self.r_key))
		char = self.r_rot.index(char)
		char = diff_mod_26(char, self.r_key)
		return char

	def rotor_roll(self, char):
		return (char + 1) % 26

if __name__ == '__main__':
	try:
		parser = argparse.ArgumentParser(description='Enigma encoding appllcation')
		parser.add_argument('path', help='path to required file')
		parser.add_argument('-config', help='string like "1 A 1 B 1 C" for indexes' 
							'of rotors and initial positions of left, middle and'
							'right rotor', default='1 A 2 A 3 A')
		args = parser.parse_args()
		path = args.path
		config = args.config
		print('Start encoding...')
		if not re.match(r'[1-3] [A-Z] [1-3] [A-Z] [1-3] [A-Z]', config):
			print('Wrong config string')
		else:
			ref = 'B'
			l_rot, l_key, m_rot, m_key, r_rot, r_key = config.split()
			try:
				file = open(path, 'r')
				message = file.read()
				file.close()
				machine = enigma(l_key, m_key, r_key, ref, l_rot, m_rot, r_rot)
				result = machine.encrypt(message)
				file = open('result.txt', 'w')
				file.write(result)
				file.close()
				print('Finish encoding. Results in ./result.txt')
			except UnicodeDecodeError:
				print('Text file is corrupted or it is a binary')
				file.close()
				file = open(path, 'rb')
				binary = file.read()
				file.close()
				machine = enigma(l_key, m_key, r_key, ref, l_rot, m_rot, r_rot)
				result = machine.binary_encrypt(binary)
				file = open('result_binary.out', 'wb')
				file.write(result)
				file.close()
				print('Finish encoding. Results in ./result_binary')
	except OSError as e:
		print('File ' + path + ' can not be processed:', e)
	except Exception as e:
		print('Unhandled exception:', e)
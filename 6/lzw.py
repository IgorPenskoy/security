import argparse
from bitarray import bitarray

def bits_from_int(number):
    a = bitarray(bin(number).replace('0b', ''))
    while len(a) < 8:
        a.insert(0, 0)
    return a

def int_from_bits(bits):
    return int(bits.to01(), 2)

def get_code(value, dictionary):
    if len(value) == 1:
        return bits_from_int(value[0])
    try:
        return bits_from_int(dictionary.index(value) + 256)
    except IndexError:
        return -1
    except ValueError:
        return -1

def compress(text):
    result = bitarray()
    dictionary = list()
    w = list()
    for k in text:
        tmp = list(w)
        tmp.append(k)
        if tmp in dictionary or len(tmp) == 1:
            w = list(tmp)
        else:
            dictionary.append(tmp)
            # print(get_code(w, dictionary))
            result.extend(get_code(w, dictionary))
            w = [k]
    if len(text) > 0:
        result.extend(get_code(w, dictionary))
    # print(get_code(w, dictionary))
    # print(result)
    return result

def decompress(text):
    result = bitarray()
    dictionary = list()
    result.extend(text[:8])
    w = [text[:8]]
    current_pos = 8
    while current_pos + 7 < len(text):
        length = (256 + len(dictionary)).bit_length()
        k = text[current_pos:length + current_pos]
        code = int_from_bits(k)
        if code > 255 and code <= len(dictionary) + 256:
            if code < len(dictionary) + 256:
                for byte in dictionary[code - 256]:
                    result.extend(byte)
                entry = dictionary[code - 256]
                # print(dictionary[code - 256])
            elif code == len(dictionary) + 256:
                entry = list(w)
                entry.append(w[0])
                for byte in entry:
                    result.extend(byte)
            current_pos += length
            tmp = list(w)
            tmp.append(entry[0])
            dictionary.append(tmp)
            w = list(dictionary[code - 256])
        else:
            k = text[current_pos:8 + current_pos]
            result.extend(k)
            current_pos += 8
            tmp = list(w)
            tmp.append(k)
            dictionary.append(tmp)
            w = [k]
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='LZW algorithm utility.')
    parser.add_argument('path', help='Path to file for compression.')
    parser.add_argument('--d', help='decomress', action='store_true')
    args = parser.parse_args()
    text = None
    if args.d:
        with open(args.path, 'rb') as file:
            text = bitarray()
            text.fromfile(file)
        text = decompress(text)
        with open(args.path + '.decompress', 'wb') as file:
            text.tofile(file)
    else:
        with open(args.path, 'rb') as file:
            text = file.read()
        text = compress(text)
        with open(args.path + '.lzw', 'wb') as file:
            text.tofile(file)

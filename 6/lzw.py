import argparse

def compress(text):
    return text

def decompress(text):
    return text

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='LZW algorithm utility.')
    parser.add_argument('path', help='Path to file for compression.')
    parser.add_argument('--d', help='decomress', action='store_true')
    args = parser.parse_args()
    text = None
    with open(args.path, 'rb') as file:
        text = file.read()
    if args.d:
        text = decomress(text)
    else:
        text = compress(text)
    with open(args.path + '.lzw', 'wb') as file:
        file.write(text)
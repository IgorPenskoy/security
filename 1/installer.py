import argparse
import shutil
import os

EXECUTABLE = 'hello_world.out'

def get_mac():
	with open('/sys/class/net/eth0/address') as f:
		mac = f.read()
		mac = mac.replace(':', '')
		mac = mac.replace('\n', '')
		return mac.upper()

if __name__ == '__main__':
	try:		
		print('INSTALLER WORKING...')
		mac = get_mac()
		exe = open(EXECUTABLE, 'rb')
		binary = exe.read()
		exe.close()
		binary = binary.replace(str.encode('DEADBEEFDEAD'), str.encode(mac))
		exe = open(EXECUTABLE, 'wb')
		exe.write(binary)
		exe.close()
		parser = argparse.ArgumentParser()
		parser.add_argument('-install_path', help='Path for new files', default='./install_dir/')
		args = parser.parse_args()
		install_path = args.install_path
		if not os.path.exists(install_path):
			os.makedirs(install_path)
		shutil.copy(EXECUTABLE, args.install_path)
		print('INSTALLATION COMPLETE')
	except Exception as e:
		print(e)

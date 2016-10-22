import zipfile


def main():
	"""
	Zipfile password cracker using a brute-force dictionary attack
	"""
	zipfilename = sys.argv[1]
	dictionary = sys.argv[2]

	password = None
	zip_file = zipfile.ZipFile(zipfilename)
	with open(dictionary, 'r') as f:
		for line in f.readlines():
			password = line.strip('\n')
			try:
				zip_file.extractall(pwd=password)
				password = 'Password found: %s' % password
				print password
				return
			except:
				pass
	print password

if __name__ == '__main__':
	main()

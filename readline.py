
# Ensure that you have the path c:/temp on your local drive.
filename = 'c:/temp/file.txt'

with open(filename, 'a') as fh:
	fh.write('Another line\n')
	fh.write('another line\n')
	fh.write('last line\n')

with open(filename) as fh:
	for line in fh:
		print('Line: ', line, end='')

# Converting lines to a list is another way to read all the lines.
# Note that this is not an efficient way when the file is very big.
fh = open(filename)
lines = list(fh)
fh.close()

print(lines)

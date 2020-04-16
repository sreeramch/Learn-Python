
# It is better to define the string used in one place to avoid duplication throughout the file.
filename = 'c:/temp/file.txt'

# open file using with constructor is very easy to use
# It is also less error prone and automatically closes the file handle when the block ends.
with open(filename, 'w') as fh:
	fh.write("Test string")

print('File is closed: ', fh.closed)

with open(filename) as fh:
	str = fh.read()
	print('Contents: ', str)

print()
# Without with constuct, the finally logic is required to close the file handle.
try:
	fh = open('c:/tmp/file.txt')
except:
	print('Could not open the file "c:/tmp/file.txt"')
finally:
	print('Closing the file handle')
	fh.close()



import sys
import argparse

both = False
if '-m' not in sys.argv and '-s' not in sys.argv:
	print('-s or -m is necessary')
	sys.exit()

if '-m' in sys.argv and '-s' in sys.argv:
	both = True

if both:
	print('Only one of -s, -m options is allowed at a time')
	sys.exit()

# Argument parsing using argparse library
floatparser = argparse.ArgumentParser()

# supports variable number of floating point numbers to be provided
floatparser.add_argument('float', type=float, nargs='+', help='enter a float value')

# command line argument to sum up all the provided floating point numbers
floatparser.add_argument('-s', dest='calculate', action='store_const', const=sum)

# optional argument
floatparser.add_argument('-m', dest='calculate', action='store_const', const=max)

# Now parse all the command line arguments
arguments = floatparser.parse_args()

print('Result: %0.2f' % arguments.calculate(arguments.float))

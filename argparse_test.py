import argparse

# Argument parsing using argparse library
floatparser = argparse.ArgumentParser()

floatparser.add_argument('float', type=float, nargs='+', help='enter a float value')

floatparser.add_argument('-s', dest='calculate', action='store_const', const=sum)

arguments = floatparser.parse_args()
print('Sum of all floating point number supplied: %0.2f' % arguments.calculate(arguments.float))

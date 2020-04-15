# First python example using python 3.8
# Note that the print has the python 3 format with "()"
# 
# Example shows how to invoke the main function.
# Also prints the current python version using the sys library.
import sys

def main():
	print("Hello World!")
	print("Python version: %s" % sys.version)


if __name__ == "__main__":
	main()


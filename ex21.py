# Exercise 21: Functions Can Return Something
import sys


# add
def add(a, b):
	try:
		print "Adding %d + %d" % (a, b)
		return a + b
	except TypeError:
		print "You can not add strings, please use a number."
		return 0

# subtract
def subtract(a, b):
	try:
		print "Subtracting %d - %d" % (a, b)
		return a - b
	except TypeError:
		print "You can not substract string, please use a number."

# multiply
def multiply(a, b):
	try:
		print "Multiplying %d * %d" % (a, b)
		return a * b
	except TypeError:
		print "Please use correct type."

# division
def divide(a, b):
	try:
		print "Dividing %d / %d" % (a, b)
		return a / b
	except TypeError:
		print "Please use correct type."

def main(argv=None):
	if argv is None:
		argv = sys.argv
# start of work
	print "Let's do some math with just functions."

	age = add(30, 5)
	height = subtract(78, 4)
	weight = multiply(215, 25)
	iq = divide(300, 2)

	print "\nAge: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

	# a puzzle for extra credit.
	print "\nHere is a puzzle."
	what = add(age, subtract(height, multiply(weight, divide(iq,2))))

	print "\nThat becomes: ", what, "Can you dit by hand?"

if __name__ == '__main__':
	main()


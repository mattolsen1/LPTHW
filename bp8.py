try:
	x = input('Enter first number: ')
	y = input('Enter second number: ')
	print x/y
	assert x/y != 0
except ZeroDivisionError:
	print "Can't use a zero here!"

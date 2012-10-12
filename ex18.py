# Exercise 18: Names, Variables, Code, Functions

# this one is like your scripts with argv

def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this jus ttake on argument

def print_line(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments

def print_none():
	print "I've got nothin dude."

# call functions to have them fire off

print_two("Matthew", "Olsen")
print_two_again("Better", "Way")
print_line("One line being printed out")
print_none()


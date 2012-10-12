# Exercise 20: Functions And Files
from sys import argv

script, input_file = argv

# function which excepts a file and reads it
def print_all(f):
	print f.read()

# function which sets the file back to the begin of file
def rewind(f):
	f.seek(0)

# function which take in a line count and file name and prints out the line number and the line itself
def print_a_line(line_count, f):
	print line_count, f.readline()

# this opens the input file being used.  
current_file = open(input_file)

print "First, let's print the whole file:\n"

# ok, on this we are using current file which is open, then pass it into the funciton to read it
print_all(current_file)

print "Now le's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"


current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
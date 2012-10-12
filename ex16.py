from sys import argv

script, filename = argv

# Give user some information
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you want that, hit RETURN."

# Prompt user 
raw_input("Enter or CTRL-C:")

print "Opening the file..."

# Open the file passed in by argv
target = open(filename, 'w+b')

# Truncate file contents
# print "Truncating the file called %r.  Goodbye contents!" % filename
# target.truncate()

# Ask user for three lines of info
print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

# Write data to file now
print "Now I'm going to write these to the file."

target.write("%s\n%s\n%s\n" %(line1,line2,line3))

# Read contents to make sure it looks good
print "Lets read the file one more time."

target.seek(0)

for line in target:
	print line

#Close out file
target.close()
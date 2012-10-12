def myTest(*args):
	for item in args:
		print "This is an arg:", item

myTest("This", 2, 3, "again") 


def myOtherTest(**kwargs):
	for key in kwargs:
		print "here is a kwarg: %r, %r" % (key, kwargs[key])

myOtherTest(arg1="one", arg2="two", arg3="three")


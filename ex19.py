# Exercise 19: Functions And Variables

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d pieces of cheese." % cheese_count
	print "You have %d boxes of crackers." % boxes_of_crackers
	print "Man, that's enough for a party." 
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "Or we can use variables to pass into our function:"
amt_of_cheese = 10
amt_of_crackers = 20

cheese_and_crackers(amt_of_cheese, amt_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 10, 20 + 20)

print "And we can even conbine the two varibles and math:"
cheese_and_crackers(amt_of_cheese + 10, amt_of_crackers + 20)
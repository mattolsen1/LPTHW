# print each letter in a set of words
def fnLetters (word):
	for i in word:
		print i

fnLetters("Hello there sir")

# print the words in a sentance
def fnWords(word):
	words = word.split()
	for i in words:
		print i

fnWords("Hello there sir")

# print the reverse of a string
def fnReverseWords(word):
	print word[::-1]

fnReverseWords("Matthew Olsen is cool!")

# upper case string
def fnCapWords(word):
	print word.upper()

fnCapWords("wow, this is cool stuff!")

# lower case string 
def fnLowerWords(word):
	print word.lower()

fnLowerWords("THIS WAS UPPER CASE")



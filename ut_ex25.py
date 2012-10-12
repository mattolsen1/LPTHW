import ex25

# try break words
sentance = "this is a test to show broken words."
words = ex25.break_words(sentance)
print words

# try sorted words
sorted_words = ex25.sort_words(words)
print sorted_words

# try printing first word
ex25.print_first_word(words)

# try printing last word
ex25.print_last_word(words)

# print just words, first and last were popped off
print words

# print out first sorted word
ex25.print_first_word(sorted_words)

# print out last sorted word
ex25.print_last_word(sorted_words)

print sorted_words

sorted_words = ex25.sort_sentence(sentance)
print sorted_words

ex25.print_first_and_last(sentance)

ex25.print_first_and_last_sorted(sentance)

#####################test



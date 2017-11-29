#line 2 to 4 use argv to get a filename
from sys import argv#get argv function from sys package

script, filename = argv
#command = open, preferred way to open a file, takes parameter and returns a value
txt = open(filename) #doesn't return contents, creates file object
#line 8 prints a little message
print "Here's your file %r:" % filename
#line 10: call a function on txt, named read, command with . and parameters
print txt.read()
#uses input from user to read file again, same command
print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)
#prints text again
print txt_again.read()

#warning: argv -> you have to add arguments when you want program to work, not only python ex15.py -> python ex15.py ex15_sample.txt
print txt.close()
print txt_again.close()

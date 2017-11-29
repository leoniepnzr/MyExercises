# -*- coding: utf-8 -*-
#The strings are set with the formatters inserted in them, variables are defined
#places one and two with strings inside strings (line 4 and 7)
x = "There are %d types of people." % 10
binary = 'binary'
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

#variable x and y are printed and sentences shown in Terminal
print x
print y

#Two more arguments are placed in form of strings, with formatters and variables x and y inserted
#places three and four with strings inside strings (line 14 and 15)
print "I said: %r." % x
print "I also said: '%s'." % y

#two more variables are defined, one is a string with another formatter
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#the two strings are printed with the variables inserted
print joke_evaluation % hilarious

#another two variables in strings are defined and printed together
w = "This is the left side of..."
e = "a string with a right side."

#the + operator adds up two numbers in general, in this case it adds two strings that makes a long string
print w + e

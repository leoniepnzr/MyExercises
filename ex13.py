#.py files = scripts
#ex13.py = argument

#import for Python feature sets (really: modules)
#argv = argument variable, holds arguments you pass to script when running
from sys import argv

#unpacks argv, assigned to four variables
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#another way of running it, attention!
#difference between argv and raw_input() = where you type the information needed to run program

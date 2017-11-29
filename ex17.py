from sys import argv
from os.path import exists #returns True/False, if file exists or doesn't
#argv - 3 parameters need input from user
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)
#input file opened and read
in_file = open(from_file)
indata = in_file.read()
#len counts byte length of input file, resolves in number
print "The input file is %d bytes long" %len(indata)
#checks if output file exists, resolves in true or false
print "Does the output file exist? %r" %exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()#needs input from user
#opens output file and writes input data to output file
out_file = open(to_file, 'w')
out_file.write(indata)
#little sentence to symbolise the end of program
print "Alright, all done."
#closes files
out_file.close()
in_file.close()

#deeper research: what does "echo" and "cat"? cat = prints file to screen,
#can be in one line with something like e.g. indata = open(from_file).read()

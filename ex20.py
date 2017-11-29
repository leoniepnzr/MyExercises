from sys import argv
#sets that script and input_file needs input from user
script, input_file = argv
#sets three functions, reads rewinds and counts lines
def print_all(f):
    print f.read()
#rewind?
def rewind(f):
    f.seek(0)#usually starting at top, seeks moves operator to right place in file
    #f.seek(0) -> start from top, f.readline() -> reading line from file, seek dealing in bytes (not lines)

def print_a_line(line_count, f):
    print line_count, f.readline()#readline -> reading file until \n, then stops and returns what it found
#opens current file
current_file = open(input_file)
#prints instruction
print "First let's print the whole file:\n"
#current_file = input file, prints content
print_all(current_file)
#prints second instruction
print "Now let's rewind, kind of like a tape."
#rewinds input file
rewind(current_file)
#sets instruction
print "Let's print three lines:"
#current line = first line, prints line of current line and current file
current_line = 1
print_a_line(current_line, current_file)
#current file increased by 1, prints second line of input file
current_line = current_line + 1
print_a_line(current_line, current_file)
#current file increased by 1, prints third line of input file
current_line = current_line + 1
print_a_line(current_line, current_file)

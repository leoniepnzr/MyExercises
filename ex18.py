#functions: name pieces of code, take arguments, lets you do mini-scripts
#created with def

#* tells Python to take all arguments and collect them in list, like argv for functions
def print_two(*args):#make a function with "def", giving function a name, *args in parantheses to work, just like argv, start with :
    arg1, arg2 = args #unpacks arguments
    print "arg1: %r, arg2: %r" % (arg1, arg2) #print arguments out

def print_two_again(arg1, arg2):#shorter way of doing it, setting names in brackets
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):#one argument
    print "arg1: %r" % arg1

def print_none():#function with no argument
    print "I got nothin'."

print_two("Leonie","Panzer")
print_two_again("Leonie","Panzer")
print_one("First!")
print_none()

#function checklist:
#function starts with def?
#function name only characters and underscores?
#open paranthesis after function name?
#arguments in paranthesis separated with commas?
#arguments unique?
#closing paranthesis and colon?
#indent 4 spaces after function?
#closing function with dedenting?

#run function checklist:
#run function by typing its name?
#put ( after name to run?
#values in paranthesis separated by commas?
#end function call with )?

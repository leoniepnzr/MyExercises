#functions can return values

#function call with two arguments, print ADDING (what we are doing), adding a and b then return them, Python adds numbers, any line will be able to assign this result to a variable
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
#(called return value)returns value in variable, add is now defined by 35 after function is run

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?"

#int(raw_input) for decimal, float(raw_input) for floating input of user

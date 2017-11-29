print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

print "What is the name of your mother?",
mother = raw_input()
print "What is the name of your father?",
father = raw_input()
print "What is the name of your sister?",
sister = raw_input()

print "So, you're mother's name is %r, your father's name is %r and your sister's name is %r." % (
    mother, father, sister)

#comma at the end of each print line so that print doesn't use newline character to start in a new line
#raw_input = doesn't interpret the typed in things, solves in a string
#'6\'2"' = escape sequence, for perfectly reading the measurement with ' and "

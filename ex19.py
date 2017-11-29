#set a function with different sentences and arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" %boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
#function filled with numbers directly
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#print a script, fill arguments with variables from script
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#calculating in function
print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

#building variables and calculations inside functions
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#arguments to a function are = to variable, if you cn use = you can pass it to a function
#infinite number of running functions
#if you use raw_input(), you need to use int() to convert results
#changing amount_of_cheese does not change cheese_count -> separated, live outside function

#sets the amount for the four variables
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
#sets some calculations with the given variables included for further spectation
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

#Study Drill solutions
#The variable car_pool_capacity is not defined since we connect "car" and "pool" - that is why you find the error
#Floating numbers drop the fractional part - it could invalid the solutions, with floating numbers the solution is more precise

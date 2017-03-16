cars = 100
space_in_a_car = 4.0 #Why use the floating numbers? cause 120.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven # NameError miss a "s"


print "There are", cars, "cars available."
print "There are only", drivers, "drivers avaliable."
print "There will be", cars_not_driven, "empty car today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool taday."
print "We need to put about", average_passengers_per_car, "in each car."

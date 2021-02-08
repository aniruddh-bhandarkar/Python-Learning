cars=100
space_in_a_car=4
drivers=30
passengers=90

cars_not_driven=cars-drivers # This shows how many cars are not driven on the basis of how many drivers are there
cars_driven=drivers # Line 6 negation 
carpool_capcity=cars_driven*space_in_a_car # Space in one car times number of cars driven
average_passengers_per_car = passengers/cars_driven # Self-explantory


print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available.")
print("There will be",cars_not_driven,"empty cars today")
print("We can transport",carpool_capcity,"People today.")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,
"in each car.")

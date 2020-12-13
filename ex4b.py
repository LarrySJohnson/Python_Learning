#Number of cars involved
cars = 100
#Amount of space avail in each car
space_in_a_car = 4.0
#Number of drives involved
drivers = 30
#Number of passengers involved
passengers = 90
#Number of cars currently not in use
cars_not_driven = cars - drivers
#Number of cars currently in use
cars_driven = drivers
#Number of passengers that can be serviced at this time
carpool_capacity = cars_driven * space_in_a_car
#Average number of passengers in the cars in service
average_passengers_per_car = passengers / cars_driven


print("There are", cars , "cars available.")
print("There are only ", drivers , "drivers available.")
print("There will be" , cars_not_driven , "empty cars today.")
print("We can transport" , carpool_capacity , "people today.")
print("We have " , passengers , "to carpool today.")
print("We need to put about ", average_passengers_per_car , "in each car.")


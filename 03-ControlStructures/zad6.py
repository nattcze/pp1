# The speed limit on the motorway is 130 km / h. Write a program that checks whether a car exceeded the speed limit.
speed_limit = 130
speed = int(input("Enter your speed"))

if speed <= speed_limit:
    print("You drive safe")
else:
    print("Too fast D:")

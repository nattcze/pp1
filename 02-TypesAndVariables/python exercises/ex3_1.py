# Exercise 1: Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.

hours = int(input("Enter number of hours worked"))
rate = int(input("Enter hour rate"))

if hours <= 40 :
    pay = hours * rate
else :
    pay = ((hours - 40) * (1.5 * rate)) + (40 * rate)

print (f"Pay : {pay}")

    

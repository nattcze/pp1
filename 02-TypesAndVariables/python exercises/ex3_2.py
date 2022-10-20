# Exercise 2: Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the
# program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

hours = int(input("Enter number of hours worked"))
rate = int(input("Enter hour rate"))


if hours >= 0:
    if hours <= 40 :
        pay = hours * rate
    else :
        pay = ((hours - 40) * (1.5 * rate)) + (40 * rate)
else :
    print("please enter numeric input")



print (f"Pay : {pay}")





#18.The length of the sides of the triangle is a, b and c. Write a program that calculates the area of the triangle using the Heron formula. Read the values of the sides of the triangle from the keyboard. Using the program, calculate the area of the triangle for the sides 3, 4 and 5.
print("Determine lenght of sides of the triangle")
import math
a = int(input("determine 1st side"))
b = int(input("determine 2nd side"))
c = int(input("determine 3rd side"))
p = (1/2)* (a + b + c)
s =  math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f"The area of the triangle is {s}")
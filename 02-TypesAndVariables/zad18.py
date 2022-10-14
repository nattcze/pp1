#calculating area of triangle
print("Determine lenght of sides of the triangle")
import math
a = int(input("determine 1st side"))
b = int(input("determine 2nd side"))
c = int(input("determine 3rd side"))
p = (1/2)* (a + b + c)
s =  math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f"The area of the triangle is {s}")
# Calculation of the area and circumference of a circle

print("Calculation of the area and circumference of a circle")

radius = int(input("determine radius"))
pi = float(input("determine pi"))

# calculating area
n1 = pi*radius**2
print(f"Area of the circle is {n1}")

# calculating circumference 
n2 = 2 * pi * radius
print(f"Circumference of the circle is {n2}")

#results
#print(f"Area of the circle is {n1} and circumference is {round(n2,2)}")
print(f"Area of the circle is {n1} and circumference is {n2}")
# 25.	The variables a and b contain the dimensions of the sides of the rectangle. 
# Write a program that creates the following rectangle with dimensions a and b. 
# Example result for a = 4 and b = 15:
# ***************
# *             *
# *             *
# ***************



a = int(input("Enter first dimension: "))
b = int(input("Enter second dimension: "))
for i in range(1,a+1):
    print("*", end = " ")

for i in range(1,(b-1)):
    print( ""*(b-2))

for i in range(1,a+1):
    print("*", end = " ")






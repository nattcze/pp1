# 25.	The variables a and b contain the dimensions of the sides of the rectangle. 
# Write a program that creates the following rectangle with dimensions a and b. 
# Example result for a = 4 and b = 15:
# ***************
# *             *
# *             *
# ***************

# nie działa

# a = int(input("Enter first dimension: "))
# b = int(input("Enter second dimension: "))
# for i in range(1, a+1):
#     print("*", end = " ")

# for i in range(1, (b-1)):
#     print( "" * (b-2))

# for i in range(1, a+1):
#     print("*", end = " ")


a = int(input("a = "))
b = int(input("b = "))

for i in range(0, a):
  if i == 0 or i == a - 1:
    printChar = "*"
  else:
    printChar = " "

  for j in range(0, b):
    if j == 0 or j == b - 1:
      print("*", end="")
    else:
      print(printChar, end="")

  print()



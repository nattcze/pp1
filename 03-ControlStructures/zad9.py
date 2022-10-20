# 9.	A user enters two integer numbers from the keyboard. Write a program that checks if at least one of them is positive.

first = int(input("First number: "))
second = int(input("Second number: "))

if first > 0 or second > 0:
  print("At least one of them is positive")
else:
  print("Both numbers are not positive")
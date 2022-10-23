# 29.	Write a program that calculates the sum and arithmetic mean of numbers entered from the keyboard. 
# Entering 0 ends entering numbers. Sample result:
# Enter number: 15
# Enter number: 8
# Enter number: 10
# Enter number: 0
# RESULT: Quantity=3, Sum=33, Mean=11

print("Input some integers to calculate their sum and average. Input 0 to exit.")

count = 0
sum = 0.0
number = 1

while number != 0:
	number = int(input(""))
	sum = sum + number
	count += 1

if count == 0:
	print("Input some numbers")
else:
	print("Average and Sum of the above numbers are: ", sum / (count-1), sum)
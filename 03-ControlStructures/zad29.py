# 29.	Write a program that calculates the sum and arithmetic mean of numbers entered from the keyboard. 
# Entering 0 ends entering numbers. Sample result:
# Enter number: 15
# Enter number: 8
# Enter number: 10
# Enter number: 0
# RESULT: Quantity=3, Sum=33, Mean=11
sum = 0
n = int(input("Enter the number: "))
q = 0

while n != 0:
    sum = sum + n
    q = q + 1
    n = int(input("Enter the number: "))
if q == 0:
    print("ijo ijo nie dzielimy przez 0")
else:
    print(f"Quantity={q}, Sum={sum}, Mean={round(sum/q)}")


# 16.	Write a program that displays two numbers entered from the keyboard in ascending order.
# Enter first number: 27
# Enter second number: 14
# Numbers in ascending order: 14, 27

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if n1 <= n2:
    print(f"Numbers in ascending order: {n1}, {n2}")
else:
    print(f"Numbers in ascending order: {n2}, {n1}")
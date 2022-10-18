# X contains any integer value. Write a program to check that the value is even.

x = int(input("enter your number"))
if x % 2 == 0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")
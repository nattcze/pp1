# 19.	Write a program that calculates a dog's age in dog’s years. 
# For the first two years, a dog's life is equal to 10.5 human years. 
# After that, each dog year is equal to 4 human years. Sample result:
# Enter the dog's age in human years: 15
# The dog's age in dog’s years is 73 years.

hy = int(input("Enter dogs age in human years "))

if hy <= 2:
    dy = hy * 10.5
    print(f"The dogs age in dogs years is : {dy}")
else: 
    dy = (2*10.5 + (hy-2)*4)
    print(f"The dogs age in dogs years is : {dy}")



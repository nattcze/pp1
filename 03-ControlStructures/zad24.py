# 24.	Write a program that creates the following pattern. Sample result:
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# n = int(input("Enter the number of rows: "))
# for i in range(0,n):
#     for j in range(0, i+1):
#         print("*", end="")
# for i in range(n -1, -1,-1):
#     for j in range(0,i):
#         print("*", end = "")

rows = int(input("Enter Right Pascals Star Triangle Pattern Rows = "))
i = 0
while(i < rows):
    j = 0
    while(j <= i):
        print('*', end = ' ')
        j = j + 1
    print()
    i = i + 1

i = rows - 1
while(i >= 0):
    j = 0
    while(j <= i - 1):
        print('*', end = ' ')
        j = j + 1
    print()
    i = i - 1

# połówka 
# n = int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(i,n):
#         print("", end ="")  
#     for j in range(i+1):
#         print("*", end ="")   
#     print()

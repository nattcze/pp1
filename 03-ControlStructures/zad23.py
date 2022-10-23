# 23.	Write a program that creates the following pattern. Sample result:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999


n = int(input("Enter the number of rows: "))
for i in range(n+1):
    for j in range(i):
        print(i, end ="")
    print()

# # reduced triangle
# n = int(input("Enter the number of rows: "))
# for i in range(n):
#     for j in range(i,n):
#         print("*", end ="")
#     print()



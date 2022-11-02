# 28.	Write a program that displays the first fifty words of the Fibonacci sequence. 
# The sequence is defined as follows: the first term is equal to 0, 
# the second is equal to 1, 
# each subsequent term is the sum of the previous two. Sample result below. 
# https://en.wikipedia.org/wiki/Fibonacci_number
# 0 1 1 2 3 5 8 13 21 34 ...

a = 0
b = 1
print(a)
print(b)
for i in range(2,50):
    c = a + b 
    a = b
    b = c
    print(c)

# def fib(n):
#     //TODO mniejszze od zera
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n-1) + fib (n-2)

# for i in range(50):
#     print(fib(i))





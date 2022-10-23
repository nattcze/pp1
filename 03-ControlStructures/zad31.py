# 31.	Write a program that displays 20 integer random numbers in the range of 5 to 10.

from random import randrange

for i in range(1, 21):
  num = randrange(5, 11) #including 10
  print(f"{i}. {num}")
    
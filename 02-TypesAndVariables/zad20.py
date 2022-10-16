# 20.	Write a program that displays the results of three dice rolls and the sum of the dice rolled. Apply a random number generator
import random

n1 = random.randint(1,6)
n2 = random.randint(1,6)
n3 = random.randint(1,6)
n4 = n1 + n2 + n3

print(f"Sum of the 3 dice rolled is {n4} ")
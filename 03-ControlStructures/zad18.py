# 18.	There are coins of 1, 2 and 5 Polish Zlotys (PLN). Write a program showing any amount (natural number) read from the keyboard with as few coins as possible.
# Enter the amount in PLN: 18
# The amount of PLN 18 in coins:
# 5 zł – 3 
# 2 zł – 1 
# 1 zł – 1

x = int(input("Enter the amount in PLN: "))

print(f" The amount of coins of PLN {x} in coins is:")

fivePLN = x//5
print(f"5 zł - {fivePLN}")
twoPLN = (x -fivePLN*5)//2
print(f"2 zł - {twoPLN}")
onePLN = ((x - fivePLN*5)-twoPLN*2)//1
print(f"1 zł - {onePLN}")




# 22.	Write a program that displays numbers from 1 to 30. 
# If the number is divisible by 3 then the program displays the word 'THREE'. 
# Next, if the number is divisible by 5 then the program displays the word 'FIVE'. 
# Finally, if the number is divisible by both 3 and 5 then the program displays the word 'BINGO'. 
# Sample result:
# 1 2 THREE 4 FIVE THREE 7 ...
 
 #propozycja romy
for i in range(1,31):
    print(i, end = " , ")
import random
wynik = random.randint(1,30)
wynik_trzy = wynik - (wynik % 3)
wynik_pięć = wynik - (wynik % 5)
if wynik_trzy == 0 and (wynik_pięć < 0 or wynik_pięć > 0) :
    print("THREE!")
if wynik_pięć == 0 and (wynik_trzy < 0 or wynik_trzy > 0) :
    print("FIVE!")
if wynik_pięć == 0 and wynik_trzy == 0 :
    print("BINGO!")

# x=1
# for x in range(1,31):
#     print(x, end= " ")





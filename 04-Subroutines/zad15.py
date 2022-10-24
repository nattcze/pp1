# .	In the module mymath.py, create the following function definitions:
# a.	read_number() that reads from the keyboard and returns integer number
# b.	generate_number() that creates and returns random integer number in the range of <1,9>
# Then create a main program, in which, first import a module you created earlier. 
# The program is a simple guessing game. The user enters a one-digit number from the keyboard. 
# The computer then generates a random one-digit number. If the numbers match, the user wins the game. 



# def read_number():
#     x = int(input("Enter number: "))
#     return x 

# def generate_number():
#     y = random.randint(1, 10)

import random
import mymath

n1 = mymath.read_number()
n2 = mymath.generate_number()

def game():
    if n1 == n2:
        print("You won !")
        return True
    else:
        print("You lost D;")
        return False

status = game()

while status == False:
    status = game()




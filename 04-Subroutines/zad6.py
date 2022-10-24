# 6.	Define a function that displays numbers in the layout as below (like on a phone keypad). Apply an loop statement. 
# Then call the function.

def telefon():
    for i in range(1,10,3):
        print(" ")
        for j in range(0,3):
            # może być range(0) bo 0 jest default
            print(i+j, end= " ")

telefon()
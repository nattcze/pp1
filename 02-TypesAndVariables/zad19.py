#19.Write a program that calculates the Body Mass Index (BMI) based on your height in cm and weight in kg. The user enters the data from the keyboard. Find the formula on the Internet for calculating BMI. Then, using your program, check that you have the correct weight
a = int(input("Tell me how tall you are in cm "))
b = int(input("How much do you weight in kg "))
c = b / ((a/100)*2)
print(f"Your BMI is {round(c,2)}")
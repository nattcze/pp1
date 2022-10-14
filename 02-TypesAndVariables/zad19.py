# calculating BMI
a = int(input("Tell me how tall you are in cm "))
b = int(input("How much do you weight in kg "))
c = b / ((a/100)*2)
print(f"Your BMI is {round(c,2)}")
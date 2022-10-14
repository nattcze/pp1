#height in cm displayed in foot and inches
cm = int(input("Enter height in cm "))

#1 centimeter = 0.032808399 feet
#1 centimeter = 0.393700787 inches
#1 foot = 12 inches

feet = int(cm * 0.032808399)
inch = int(feet % 12)

# feet = int(cm * 0.032808399)
# inch = int(foot % 12)

print(f"I am {cm} tall, i.e. {round(feet,0)} feet and {round(inch,0)} inches ")
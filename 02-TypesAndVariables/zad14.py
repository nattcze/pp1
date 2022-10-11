# get input in Celsius degrees and convert to Farenheit and Kelvin
print("This program converts reads temperature in Celsius degrees and converts it to Kelwin and Farenheit.")
Celsius = int(input("Determine temperature in Celsius degrees "))

#calculating Celsius to Farenheit
n1 = (9/5)* Celsius+32

#calculating Celsius to Kelvin
n2 = Celsius + 273.15

#results
print(f"{Celsius} degrees Celsius is {n1} Farenheit degrees and {round(n2,2)} kelwin degrees")

  #temperature converter
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit of the temperature (C or F): ")

if unit == "C":
    temperature_in_F = (temperature * 9/5) + 32
    print("Temperature in F: " + str(temperature_in_F))
elif unit == "F":
    temperature_in_C = (temperature - 32) * 5/9
    print("Temperature in C: " + str(temperature_in_C))
else:
    print("Error: Invalid unit")
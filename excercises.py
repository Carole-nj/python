#python calculator
operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"
print("Result: " + str(result))

#weight converter
weight = float(input("Enter the weight : "))
unit = input("Enter the unit of the weight (kg or lbs): ")

if unit == "kg":
    weight_in_lbs = weight * 2.20462
    print("Weight in lbs: " + str(weight_in_lbs))
elif unit == "lbs":
    weight_in_kg = weight * 0.453592
    print("Weight in kg: " + str(weight_in_kg))
else:
    print("Error: Invalid unit")


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
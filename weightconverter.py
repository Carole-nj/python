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

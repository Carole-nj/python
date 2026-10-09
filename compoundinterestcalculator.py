principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principal amount (greater than 0): "))
    if principle <= 0:
        print("Please enter a valid principal amount.")

while rate <= 0:
    rate = float(input("Enter the interest rate (greater than 0): "))
    if rate <= 0:
        print("Please enter a valid interest rate.")

while time <= 0:
    time = float(input("Enter the time period (greater than 0): "))
    if time <= 0:
        print("Please enter a valid time period.")

compound_interest = principle * (1 + rate/100) ** time
print(f"Compound Interest: {compound_interest}")
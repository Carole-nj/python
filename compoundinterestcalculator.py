principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principal amount (greater than 0): "))
    if principle <= 0:
        print("Please enter a valid principal amount.")
    else:
        break
while True:
    rate = float(input("Enter the interest rate (greater than 0): "))
    if rate <= 0:
        print("Please enter a valid interest rate.")
    else:
        break

while True:
    time = float(input("Enter the time period (greater than 0): "))
    if time <= 0:
        print("Please enter a valid time period.")
    else:
        break

compound_interest = principle * (1 + rate/100) ** time
print(f"Compound Interest: {compound_interest}")
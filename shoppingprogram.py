foods = []
prices = []
total = 0

while True:
    food = input("Enter a food item (or 'done' to finish): ")
    if food.lower() == 'done':
        break
    price = float(input(f"Enter the price for {food}: "))
    foods.append(food)
    prices.append(price)
    total += price
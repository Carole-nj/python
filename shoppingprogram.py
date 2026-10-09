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

    print("^^^your cart^^^")
    for food in foods:
        print(food)

    for price in price:
        print(price)

    print(f"your total is: ${total:.2f}")
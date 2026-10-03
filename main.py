print("i love pizza")
print("it is really good")

#strings
first_name = "Carol"
food = "pizza"
email = "carol@example.com"
print(first_name)
print(food)
print(email)

#integers
age = 22
quantity = 3
num_of_students = 30

print(age)
print(quantity)
print(num_of_students)

#float
price = 3.99

print(price)

#boolean
is_hungry = True

print(is_hungry)

#typecasting
name = "Carol"
age = 22
gpa = 3.5
is_hungry = True

age_as_string = str(age)
print(age_as_string)

try:
	name_as_integer = int(name)
except ValueError:
	print("A name cannot be converted to an integer.")

#input
name = input("What is your name? ")
print("Hello, " + name + "!")

#Exercise rectangle area
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width

print("The area of the rectangle is: " + str(area))

#exercise 2 shopping cart program
item = input("Enter the name of the first item: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))
total = price * quantity
print("Item: " + item)
print("Price: $" + str(price))
print("Quantity: " + str(quantity))
print("Total: $" + str(total))

print("Thank you for shopping with us!")

#Madlibs game
#word game where you create a story by filling in the blanks with words of your choice
print("Welcome to the Madlibs game!")
print("Please provide the following words:")
adjective = input("Adjective: ")
noun = input("Noun: ")
verb = input("Verb: ")

print(f"The {adjective} {noun} {verb} quickly.")

#arithmetic operations
friends = 5
friends += 2 
friends -= 1
friends *= 3
friends /= 2

print(friends)
remaining_friends = friends % 2
print(remaining_friends)

#math functions


x = 3.14
y = 4
z = 5

result = round(x)
#result = abs(y)
#result = pow(y, 3)
#result = max(x, y, z)
#result = min(x, y, z)

print(result)

import math
print(math.pi)
print(math.e)

#excercise 3 circle circumference calculator
import math
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print("The circumference of the circle is: " + str(circumference))

#exercise 4 circle area calculator
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2)
print("The area of the circle is: " + str(area))





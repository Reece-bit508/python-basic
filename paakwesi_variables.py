# Exercise 1: Basic Variables
name = " Paa Kwesi Afful Donkor"
age = 21
favorite_language = "Python"
completed_today_class = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favorite Programming Language: {favorite_language}")
print(f"Completed Today's Class: {completed_today_class}")
print()

# Exercise 2: Variable Operations
num1 = 15
num2 = 4

sum= num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print(f"Sum: {sum}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")
print()

# Exercise 3: String Manipulation
first_name = "Paa Kwesi Afful"
last_name = "Donkor"

full_name = first_name + " " + last_name
uppercase_name = full_name.upper()
introduction = f"Hello, my name is {full_name}"

print(f"Full Name: {full_name}")
print(f"Uppercase Name: {uppercase_name}")
print(f"Introduction: {introduction}")
print()

# Exercise 4: User Input
print("Exercise 4:")
favorite_food = input("What is your favorite food? ")
times_per_week = input("How many times do you eat it per week? ")

print(f"You eat {favorite_food} {times_per_week} times per week!")
print()

# Exercise 5: Type Conversion
print("Exercise 5:")
age = "25"
height = 5.8

# Fixed code with proper type conversion
print("I am " + age + " years old and " + str(height) + " feet tall")
print()

# Exercise 6: Simple Calculator
celsius = 25
fahrenheit = (celsius * 9/5) + 32

print(f"Temperature in Celsius: {celsius}°C")
print(f"Temperature in Fahrenheit: {fahrenheit}°F")

"""A simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform calculation and display numbers."""

# For Addition purpose
def add(x, y):
    return x + y
# For subtraction purpose
def subtract(x, y):
    return x - y
# For multiplication purpose
def multiply(x, y):
    return x * y
#For division purpose
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

# Perform the calculation based on the chosen operation
if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = subtract(num1, num2)
elif operation == "*":
    result = multiply(num1, num2)
elif operation == "/":
    result = divide(num1, num2)
else:
    result = "Invalid operation. Please choose +, -, *, or /."

print(f"Result: {result}")

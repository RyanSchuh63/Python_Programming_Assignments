def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y
# Functions for the 4 main operations

num1 = float(input('Enter your first number: '))
num2 = float(input('Enter your second number: '))
Func = input('Please enter +(add), -(subtract), *(multiply), /(divide): ')
# User inputs for operation and numbers used

if Func == "+":
    print("The total is: ", add(num1, num2))
elif Func == "-":
    print("The difference is: ", subtract(num1, num2))
elif Func == "*":
    print("The product is: ", multiply(num1, num2))
elif Func == "/":
    print("the quotient is: ", divide(num1, num2))
#Calls correct function and prints outcome

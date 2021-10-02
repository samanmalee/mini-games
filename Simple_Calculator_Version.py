# Python program for simple calculator 
   
def addition(x, y):
    "Function to add two numbers "
    return x + y 
    
def subtraction(x, y):
    "Function to subtract two numbers" 
    return x - y 
   
def multiplication(x, y):
    "Function to multiply two numbers" 
    return x * y 
   
def division(x, y):
    "Function to divide two numbers" 
    return x / y 

def raisePower(x, y):
    "Function to raise to the power"
    return x ** y

# --------------------------------------- Starting main body --------------------------------------------

# Taking user input
print("Operation to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Raising a power to number")

choice = input("Enter choice: ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Deciding operation
if choice == '1':
   print(num1, "+" ,num2, "=", addition(num1, num2))

elif choice == '2':
   print(num1, "-", num2, "=", subtraction(num1, num2))

elif choice == '3':
   print(num1, "*", num2, "=", multiplication(num1, num2))

elif choice == '4':
   print(num1, "/", num2, "=", division(num1, num2))

elif choice == '5':
   print(num1, "**", num2, "=", raisePower(num1, num2))

else:
   print("Please select a valid input.")
print("Welcome to the Calculator")

# input the first number
num1 = float(input("Enter the first number: "))

# input the second number
num2 = float(input("Enter the second number: "))

# choosing an operation from the list
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

operation = input("Enter the number corresponding to your chosen operation: ")

# Performing the operation
if operation == '1':
    result = num1 + num2
    print(f"The addition of {num1} + {num2} is: {result}")
elif operation == '2':
    result = num1 - num2
    print(f"The subtraction of {num1} - {num2} is: {result}")
elif operation == '3':
    result = num1 * num2
    print(f"The Product of {num1} * {num2} is: {result}")
elif operation == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"The Division of {num1} / {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice\nPlease try again.")

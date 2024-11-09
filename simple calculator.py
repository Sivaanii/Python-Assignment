try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit()

print("Select an option:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

operation = input("Enter your choice (1/2/3/4 or +, -, *, /): "
                  
operations = {
    '1': num1 + num2,
    '+': num1 + num2,
    '2': num1 - num2,
    '-': num1 - num2,
    '3': num1 * num2,
    '*': num1 * num2,
    '4': "Error: Division by zero is undefined." if num2 == 0 else num1 / num2,
    '/': "Error: Division by zero is undefined." if num2 == 0 else num1 / num2
}
result = operations.get(operation, "Invalid operation. Please select a valid option.")
print(f"The result is: {result}")

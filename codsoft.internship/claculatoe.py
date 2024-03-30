a = float(input("Enter num1: "))
b = float(input("Enter num2: "))

print("Calculator")

operation = input("Choose operation (+, -, *, /): ")

if operation == '+':
    result = a + b
    print(f"Addition sum: {result}")
elif operation == '-':
    result = a - b
    print(f"Subtraction difference: {result}")
elif operation == '*':
    result = a * b
    print(f"Multiplication product: {result}")
elif operation == '/':
    if b != 0:
        result = a / b
        print(f"Division quotient: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose from +, -, *, /.")


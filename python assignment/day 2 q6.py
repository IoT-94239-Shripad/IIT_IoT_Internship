
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number (divider): "))
if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    result = num1 / num2
    print("Division result =", result)

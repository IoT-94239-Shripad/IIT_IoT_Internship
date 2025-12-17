import calculator

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        sum_result = calculator.add(num1, num2)
        diff_result = calculator.subtract(num1, num2)
        prod_result = calculator.multiply(num1, num2)
        div_result = calculator.divide(num1, num2)

        print("\nResults:")
        print(f"{num1} + {num2} = {sum_result}")
        print(f"{num1} - {num2} = {diff_result}")
        print(f"{num1} * {num2} = {prod_result}")
        print(f"{num1} / {num2} = {div_result}")

    except ValueError:
        print("\nInvalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()

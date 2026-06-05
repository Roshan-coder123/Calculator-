def calculator():
    print("=======")
    print("Calculator")
    print("=======")
    print(" + =  Addition")
    print(" - =  Subtraction")
    print(" * =  Multiplication")
    print(" / =  Division")
    print(" % =  Modulo")
    print(" ^ =  Exponentiation")
    print("=======")

    while True:
        try:
            num1 = float(input("\nEnter the first number: "))
            operator = input("Enter the operator (+, -, *, /, %, ^): ")
            num2 = float(input("Enter the second number: "))

            if operator == '+':
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif operator == '-':
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif operator == '*':
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
                else:
                    print("Error: Division by zero is not allowed.")
            elif operator == '%':
                result = num1 % num2
                print(f"{num1} % {num2} = {result}")
            elif operator == '^':
                result = num1 ** num2
                print(f"{num1} ^ {num2} = {result}")
            else:
                print("Invalid operator. Please try again.")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

        again = input("\nCalculate again? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye! 👋")
            break

if __name__ == "__main__":
    calculator()
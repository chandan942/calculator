def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /, %): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero"
        result = num1 / num2
    elif operator == '%':
        if num2 == 0:
            return "Error: Module by zero"
        result = num1 % num2
    else:
        return "Error: Invalid operator"

    return result

again = "y"

while again.lower() == "y":
    print("Result:", calculator())
    again = input("Do you want to calculate again? (y/n): ")
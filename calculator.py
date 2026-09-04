# adding the logic so that program remembers the history:
def calculate(num1, operator, num2):
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
            return "Error: Modulo by zero"
        result = num1 % num2
    else:
        return "Error: Invalid operator"

    return result


def calculator(history):
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /, %): ").strip()
    num2 = float(input("Enter second number: "))

    result = calculate(num1, operator, num2)

    if isinstance(result, str):
        return result

    calculation = f"{num1} {operator} {num2} = {result}"
    history.append(calculation)

    return result

def calculator(history):
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /, %): ").strip()
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
            return "Error: Modulo by zero"
        result = num1 % num2
    else:
        return "Error: Invalid operator"

    calculation = f"{num1} {operator} {num2} = {result}"
    history.append(calculation)

    return result


def show_history(history):
    if not history:
        print("\nNo calculation history available.")
        return 
        print("\nCalculation History:")
        for number, calculation in enumerate(history, start=1):
            print(f"{number}. {calculation}")

if __name__ == "__main__":
 
  history = []
  again = "y"

  while again.lower() == "y":
    print("\nResult:", calculator(history))

    choice = input(
        "\nEnter 'h' to view history, or press Enter to continue: "
    )

    if choice.lower() == "h":
        show_history(history)

    again = input("\nDo you want to calculate again? (y/n): ")
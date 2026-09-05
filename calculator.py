# adding the logic so that program remembers the history:
import json
def save_history(history):
  with open("history.json","w") as file:
    json.dump(history,file)

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
  num1 = get_valid_number("Enter first number: ")
  operator = get_valid_operator("Enter operator (+, -, *, /, %): ")
  num2 = get_valid_number("Enter second number: ")

  result = calculate(num1, operator, num2)
  if isinstance(result, str):
      return result

  calculation = f"{num1} {operator} {num2} = {result}"
  history.append(calculation)
  save_history(history)

  return result

def show_history(history):
    if not history:
        print("\nNo calculation history available.")
        return

    print("\nCalculation History:")
    for number, calculation in enumerate(history, start=1):
        print(f"{number}. {calculation}")

def get_valid_number(prompt):
    """Keeps asking until the user enters a valid number."""
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Error: Please enter a valid number.")

def get_valid_operator(prompt):
    """Keeps asking until the user enters a valid operator."""
    valid_ops = ('+', '-', '*', '/', '%')
    while True:
        op = input(prompt).strip()
        if op in valid_ops:
            return op
        print(f"Error: Please enter one of {valid_ops}.")

if __name__ == "__main__":
 
  history = []
  if __name__ == "__main__":
    history = []

  while True:
    print("================================")
    print("          CALCULATOR")
    print("================================")
    print()
    print("1. Calculate")
    print("2. View History")
    print("3. Clear History")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("\nResult:", calculator(history))

    elif choice == "2":
        show_history(history)

    elif choice == "3":
        history.clear()
        print("\nHistory cleared.")

    elif choice == "4":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice. Please select 1-4.")
# adding the logic so that program remembers the history:
import os
import json
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def save_history(history,file_path="history.json"):
  with open(file_path,"w") as file:
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

def format_result(result):
    if isinstance(result, float) and result.is_integer():
        return int(result)
    return result

def calculator(history):
  num1 = get_valid_number("Enter first number: ")
  operator = get_valid_operator("Enter operator (+, -, *, /, %): ")
  num2 = get_valid_number("Enter second number: ")

  result = calculate(num1, operator, num2)
  if isinstance(result, str):
      return result

  result = format_result(result)

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

def load_history(file_path="history.json"):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        return []

def delete_history(history):
    if not history:
        print("\nNo calculation history available.")
        return

    show_history(history)

    choice = input("\nEnter history number to delete: ")

    try:
        number = int(choice)
    except ValueError:
        print("\nInvalid number.")
        return

    index = number - 1

    if index < 0 or index >= len(history):
        print("\nHistory number doesn't exist.")
        return

    deleted = history.pop(index)
    save_history(history)

    print(f"\nDeleted: {deleted}")

if __name__ == "__main__":
    history = load_history()

while True:
    clear_screen()

    print("================================")
    print("          CALCULATOR")
    print("================================")
    print()
    print("1. Calculate")
    print("2. View History")
    print("3. Delete History Item")
    print("4. Clear History")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("\nResult:", calculator(history))
        input("\nPress Enter to continue...")

    elif choice == "2":
        show_history(history)
        input("\nPress Enter to continue...")

    elif choice == "3":
        delete_history(history)
        input("\nPress Enter to continue...")

    elif choice == "4":
        history.clear()
        save_history(history)
        print("\nHistory cleared.")
        input("\nPress Enter to continue...")

    elif choice == "5":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice. Please select 1-5.")
        input("\nPress Enter to continue...")
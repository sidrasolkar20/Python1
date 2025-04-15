"""Aim:write an interactive calculator! User input is assumed to be a formula that consist of a number,
an operator (at least + and-), and another number, separated by white space(e.g. 1 +1).
Split user input using str.split(), and check whether the resulting list is valid:"""
# Exp05(01)
# Name: Sidra Solkar
# UIN: 231P087   Roll No: 43
class FormulaError(Exception):
    pass

def calculate():
    while True:
        user_input = input("Enter a formula (e.g., 1 + 1) or 'quit' to exit: ").strip()

        if user_input.lower() == 'quit':
            print("\nName: Sidra Solkar UIN: 231P087 Roll No: 43")
            break

        parts = user_input.split()
        
        if len(parts) != 3:
            print("Error: Formula must have two numbers and an operator.")
            continue
        
        try:
            num1 = float(parts[0])
            num2 = float(parts[2])
        except ValueError:
            print("Error: Invalid number input.")
            continue
        
        if parts[1] not in ['+', '-']:
            print("Error: Invalid operator. Use '+' or '-'.")
            continue
        
        if parts[1] == '+':
            result = num1 + num2
        elif parts[1] == '-':
            result = num1 - num2
        
        print(f"Result: {result}")

# Start the calculator
calculate()

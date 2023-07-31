logo = """
 _____________________
|  _________________  |
| | Calculator   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero."

def floor_divide(a, b):
    if b != 0:
        return a // b
    else:
        return "Error: Cannot divide by zero."

def power(a, b):
    return a ** b

def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: Cannot divide by zero."

print(logo)
print("Welcome To the Calculator")
while True:
    
    operator = input('''
    +  Addition
    -  Substraction
    *  Multiplication
    /  Division
    // Floor division
    ** Raise to power
    %  Modulo or Remainder
    Please Input Your Operator (or 'q' to quit): ''')

    if operator == 'q':
        print("Calculator has been closed.")
        break

    operand1 = float(input("Enter Operand 1: "))
    operand2 = float(input("Enter Operand 2: "))

    if operator == '+':
        result = add(operand1, operand2)
    elif operator == '-':
        result = subtract(operand1, operand2)
    elif operator == '*':
        result = multiply(operand1, operand2)
    elif operator == '/':
        result = divide(operand1, operand2)
    elif operator == '//':
        result = floor_divide(operand1, operand2)
    elif operator == '**':
        result = power(operand1, operand2)
    elif operator == '%':
        result = modulo(operand1, operand2)
    else:
        result = "Error: Invalid operator"

    print(f"Result: {result}\n")


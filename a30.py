def add(a, b):    
    return a + b

def subtract(a, b):   
    return a - b

def multiply(a, b):   
    return a * b

def divide(a, b):   
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    operations = {
        '1': ('Addition', add),
        '2': ('Subtraction', subtract),
        '3': ('Multiplication', multiply),
        '4': ('Division', divide)
    }

    print("Calculatorgdffsf")
    print("Select an operation:")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")

    choice = input("Enter choice (1/2/3/4): ").strip()

    if choice not in operations:
        print("Invalid choice. Please restart and select a valid option.")
        return

    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    operation_name, operation_func = operations[choice]
    result = operation_func(num1, num2)

    print(f"\nResult of {operation_name} ({num1} and {num2}): {result}")


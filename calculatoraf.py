# Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Main Program
def calculator():
    print("Simple Calculator")
    
    try:
        # Taking user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice == '1':
            result = add(num1, num2)
            print(f"The result of addition is: {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"The result of subtraction is: {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"The result of multiplication is: {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"The result of division is: {result}")
        else:
            print("Invalid input! Please select a valid operation.")
    
    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the calculator
calculator()

# SUPER ADVANCED CALCULAATORR
history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

def square(a):
    return a * a

def cube(a):
    return a * a * a

def factorial(n):
    if n < 0:
        return "Error: Negative number"
    fact = 1
    for i in range(1, int(n) + 1):
        fact *= i
    return fact

def show_menu():
    print("\n========== CALCULATOR MENU ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square")
    print("8. Cube")
    print("9. Factorial")
    print("10. View History")
    print("11. Clear History")
    print("12. Exit")

# Main Program
while True:
    show_menu()
    choice = input("Enter your choice (1-12): ")

    if choice == "12":
        print("Calculator closed successfully.")
        break

    elif choice == "10":
        print("\n--- Calculation History ---")
        if not history:
            print("No history available.")
        else:
            for item in history:
                print(item)
        continue

    elif choice == "11":
        history.clear()
        print("History cleared.")
        continue

    try:
        if choice in ["1", "2", "3", "4", "5", "6"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
                expression = f"{num1} + {num2} = {result}"

            elif choice == "2":
                result = subtract(num1, num2)
                expression = f"{num1} - {num2} = {result}"

            elif choice == "3":
                result = multiply(num1, num2)
                expression = f"{num1} * {num2} = {result}"

            elif choice == "4":
                result = divide(num1, num2)
                expression = f"{num1} / {num2} = {result}"

            elif choice == "5":
                result = modulus(num1, num2)
                expression = f"{num1} % {num2} = {result}"

            elif choice == "6":
                result = power(num1, num2)
                expression = f"{num1} ^ {num2} = {result}"

        elif choice == "7":
            num = float(input("Enter number: "))
            result = square(num)
            expression = f"{num}² = {result}"

        elif choice == "8":
            num = float(input("Enter number: "))
            result = cube(num)
            expression = f"{num}³ = {result}"

        elif choice == "9":
            num = int(input("Enter number: "))
            result = factorial(num)
            expression = f"{num}! = {result}"

        else:
            print("Invalid choice. Try again.")
            continue

        print("Result:", result)
        history.append(expression)

    except ValueError:
        print("Invalid input! Please enter numeric values only.")

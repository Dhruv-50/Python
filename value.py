python
```
# 23.8 Modular Calculator

def sum_values(a, b):
    return a + b

def minus_values(a, b):
    return a - b

def product_values(a, b):
    return a * b

def quotient_values(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"

def power_values(a, b):
    return a ** b

def run_calculator():
    print("--- Simple Calculator ---")
    print("1. Addition | 2. Subtraction | 3. Multiplication")
    print("4. Division | 5. Power | 6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == '6':
        print("Calculator Closed.")
        return

    if choice not in ('1', '2', '3', '4', '5'):
        print("Invalid Option!")
        return

    num1 = float(input("Enter first value: "))
    num2 = float(input("Enter second value: "))

    if choice == '1':
        print(f"Answer: {sum_values(num1, num2)}")
    elif choice == '2':
        print(f"Answer: {minus_values(num1, num2)}")
    elif choice == '3':
        print(f"Answer: {product_values(num1, num2)}")
    elif choice == '4':
        print(f"Answer: {quotient_values(num1, num2)}")
    elif choice == '5':
        print(f"Answer: {power_values(num1, num2)}")

run_calculator()
```
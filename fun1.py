python
```
# 15.4 Function Basics

def greet(name):
    print(f"Hi, {name}! Welcome to Python.")

def square(value):
    return value ** 2

def cube(value):
    return value ** 3

print("--- Greeting Section ---")
greet("Alice")
greet("Bob")
greet("Charlie")

print("\n--- Square Results ---")
print(f"Square of 2: {square(2)}")
print(f"Square of 5: {square(5)}")
print(f"Square of 7: {square(7)}")

print("\n--- Cube Results ---")
print(f"Cube of 3: {cube(3)}")
print(f"Cube of 5: {cube(5)}")
print(f"Cube of 7: {cube(7)}")
```
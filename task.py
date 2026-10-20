python
```
# 34.5 Stack Simulator

class NumberStack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack Underflow"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is Empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(f"Stack (Top -> Bottom): {self.items[::-1]}")

# Simulation
stack_obj = NumberStack()

print("1. Adding 5 items: 10, 20, 30, 40, 50")
for value in [10, 20, 30, 40, 50]:
    stack_obj.push(value)

print(f"2. Top element: {stack_obj.peek()}")

print(f"3. Removed element: {stack_obj.pop()}")
print(f"   Removed element: {stack_obj.pop()}")

print("4. Current stack:")
stack_obj.display()
```
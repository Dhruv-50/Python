python
```
# 9.4 Percentage Calculator
a = float(input("Enter marks for Subject 1: "))
b = float(input("Enter marks for Subject 2: "))
c = float(input("Enter marks for Subject 3: "))
d = float(input("Enter marks for Subject 4: "))
e = float(input("Enter marks for Subject 5: "))

total = a + b + c + d + e
percentage = (total / 500) * 100
average = total / 5

print(f"\nGrand Total: {total:.2f}/500")
print(f"Final Percentage: {percentage:.2f}%")
print(f"Average Score: {average:.2f}")
```
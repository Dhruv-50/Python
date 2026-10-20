python
```
# 31.8 Set Operations Lab

groupA = {n for n in range(1, 21) if n % 2 == 0}  # Even numbers 1-20
groupB = {n for n in range(1, 21) if n % 4 == 0}  # Multiples of 4 up to 20

print(f"Set A (Evens 1-20)          : {groupA}")
print(f"Set B (Multiples of 4)      : {groupB}")
print("-" * 50)
print(f"Union (A | B)               : {groupA | groupB}")
print(f"Intersection (A & B)        : {groupA & groupB}")
print(f"Difference (A - B)          : {groupA - groupB}")
print(f"Difference (B - A)          : {groupB - groupA}")
print(f"Symmetric Difference (A ^ B): {groupA ^ groupB}")
```
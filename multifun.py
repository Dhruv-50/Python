python
```
# 24.7 Multi-Return Function

def calculate(a, b, c):
    summation = a + b + c
    mean = summation / 3
    smallest = min(a, b, c)
    largest = max(a, b, c)
    return summation, mean, smallest, largest

# Unpacking returned values
total, average, minimum, maximum = calculate(18, 42, 30)

print(f"Total: {total}")
print(f"Mean: {average:.2f}")
print(f"Smallest Value: {minimum}")
print(f"Largest Value: {maximum}")
```
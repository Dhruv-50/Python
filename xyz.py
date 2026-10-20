python
```
# 7.3 Swap Without Temp
p = int(input("Enter first value: "))
q = int(input("Enter second value: "))

print(f"\nBefore Swapping: p = {p}, q = {q}")

p, q = q, p
print(f"After Tuple Swapping: p = {p}, q = {q}")

p = p + q
q = p - q
p = p - q

print(f"After Arithmetic Swapping: p = {p}, q = {q}")
```
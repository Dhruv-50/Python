python
```
# 14.6 Factorial Function

def find_factorial(num):
    answer = 1
    for j in range(1, num + 1):
        answer *= j
    return answer

print(f"{'Value':<10} | {'Result':<15}")
print("-" * 28)

for k in range(1, 8):
    print(f"{k:<10} | {find_factorial(k):<15}")

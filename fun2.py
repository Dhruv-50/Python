python
```
# 16.2 Prime Number Checker

def check_prime(num):
    if num < 2:
        return False

    for j in range(2, num):
        if num % j == 0:
            return False

    return True

number = 15

if check_prime(number):
    print(f"{number} is a Prime Number")
else:
    print(f"{number} is Not a Prime Number")
```
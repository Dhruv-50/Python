python

# 6.3 Digit Extractor
num = int(input("Enter a 3-digit number: "))
a = num // 100
b = (num // 10) % 10
c = num % 10
d = a + b + c
e = a * b * c

print(f"Hundreds Digit: {a}")
print(f"Tens Digit: {b}")
print(f"Units Digit: {c}")
print(f"Sum of Digits: {d}")
print(f"Product of Digits: {e}")
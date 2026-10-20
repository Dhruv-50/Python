python
```
# 39.7 Exception Handling

try:
    value = int("world")
except ValueError as error:
    print(f"(a) ValueError caught: {error}")

try:
    answer = 50 / 0
except ZeroDivisionError as error:
    print(f"(b) ZeroDivisionError caught: {error}")

try:
    with
```
python
```
# 35.7 Tuple Operations

values = (82, 67, 91, 76, 85)

print(f"Original Tuple: {values}")
print(f"Indexing (First Element): {values[0]}")
print(f"Slicing (Middle 3)      : {values[1:4]}")
print(f"Length                  : {len(values)}")

# Demonstrating Immutability
print("\nTrying to change a tuple element:")
try:
    values[0] = 100
except TypeError as error:
    print(f"  TypeError caught successfully: {error}")

# Modify using list conversion
new_list = list(values)
new_list[0] = 100
values = tuple(new_list)

print(f"Tuple after list conversion: {values}")
```
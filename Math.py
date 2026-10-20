python
```
import math

# 10.6 Area and Perimeter
length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))

rect_area = length * width
rect_perimeter = 2 * (length + width)
circle_area = math.pi * (length ** 2)

print(f"Area of Rectangle: {rect_area:.2f}")
print(f"Perimeter of Rectangle: {rect_perimeter:.2f}")
print(f"Area of Circle (Radius = {length}): {circle_area:.2f}")
```
python
```
# 5.4 Unit Converter
value = float(input("Enter distance in kilometres: "))
metre = value * 1000
centi = value * 100000
mile = value * 0.621371
feet = value * 3280.84

print(f"Metres: {metre:.2f} m")
print(f"Centimetres: {centi:.2f} cm")
print(f"Miles: {mile:.4f} mi")
print(f"Feet: {feet:.2f} ft")

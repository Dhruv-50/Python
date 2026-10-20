python
```
# 1.05 BMI Calculator
a = float(input("Enter your weight: "))
b = float(input("Enter your height: "))
c = a / (b * b)

if c < 18.5:
    d = "Underweight"
elif c <= 24.9:
    d = "Normal"
elif c <= 29.9:
    d = "Overweight"
else:
    d = "Obese"

print("BMI:", round(c, 2))
print("Category:", d)
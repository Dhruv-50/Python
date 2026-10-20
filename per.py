python
```
# 11.3 Salary Calculator
salary = float(input("Enter basic salary: "))
hra = 0.20 * salary
da = 0.15 * salary
pf = 0.08 * salary

gross = salary + hra + da
net = gross - pf

print(f"HRA Amount: {hra:.2f}")
print(f"DA Amount: {da:.2f}")
print(f"PF Deduction: {pf:.2f}")
print(f"Gross Pay: {gross:.2f}")
print(f"Net Pay: {net:.2f}")
```
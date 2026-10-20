python
```
# 19.7 Report Card with f-strings

student_name = "Rahul Patel"
roll_number = 20261052
marks = [78, 85, 92, 69, 88]

total = sum(marks)
percentage = total / len(marks)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
else:
    grade = "C"

print("=" * 40)
print(f"{'STUDENT MARKSHEET':^40}")
print("=" * 40)
print(f"Name   : {student_name:<25}")
print(f"Roll No: {roll_number:<25}")
print("-" * 40)

for number, mark in enumerate(marks, start=1):
    print(f"Subject {number} Marks : {mark:>5}")

print("-" * 40)
print(f"Total Marks     : {total:>5} / 500")
print(f"Percentage      : {percentage:>5.2f}%")
print(f"Final Grade     : {grade:>5}")
print("=" * 40)
```
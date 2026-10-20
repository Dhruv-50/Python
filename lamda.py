python
```
# 17.5 Lambda Sort

students = [
    ("Amit", 75),
    ("Kiran", 45),
    ("Neha", 92),
    ("Priya", 58),
    ("Rohan", 84)
]

# Sort marks in descending order
sorted_students = sorted(students, key=lambda student: student[1], reverse=True)

print("Students sorted by marks (Highest to Lowest):")
for name, marks in sorted_students:
    print(f"  {name:<8}: {marks}")

# Filter students who scored 70 or more
passed_students = list(filter(lambda student: student[1] >= 70, sorted_students))

print("\nStudents scoring 70 or more:")
for name, marks in passed_students:
    print(f"  {name:<8}: {marks}")
```
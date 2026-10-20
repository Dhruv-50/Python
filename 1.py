python
```
# 36.8 File Handling

student_names = ["Karan", "Meera", "Jay"]

with open("students_data3.txt", "a") as file:
    for student in student_names:
        file.write(student + "\n")

# Read and display updated file
print("Updated Student Records:")

with open("students_data3.txt", "r") as file:
    records = file.readlines()
    for record in records:
        print(record.strip())

print(f"\nTotal Records: {len(records)}")
```
python
```
# 37.9 Student Marks Summary

student_data = [
    "Aarav 78\n",
    "Diya 92\n",
    "Krish 84\n",
    "Anaya 88\n",
    "Rohan 74\n"
]

# Write student data into a file
with open("student_marks3.txt", "w") as file:
    file.writelines(student_data)

total_score = 0
student_count = 0

# Read the file and calculate total marks
with open("student_marks3.txt", "r") as file:
    for record in file:
        details = record.strip().split()

        if len(details) == 2:
            student_name = details[0]
            student_marks = float(details[1])

            total_score += student_marks
            student_count += 1

# Calculate the average marks
average_score = total_score / student_count if student_count > 0 else 0

# Prepare the summary report
report = (
    f"Total Students: {student_count}\n"
    f"Total Marks: {total_score:.2f}\n"
    f"Class Average: {average_score:.2f}\n"
)

# Save the summary into another file
with open("student_summary3.txt", "w") as file:
    file.write(report)

# Display the summary results
print("=" * 35)
print(f"{'STUDENT MARKS SUMMARY':^35}")
print("=" * 35)
print(report)
print("Summary saved successfully.")
print("=" * 35)
```
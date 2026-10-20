python
```
# 28.5 Student Gradebook

marks_data = {
    "Aarav": [82, 76, 90],
    "Diya": [91, 94, 88],
    "Krish": [65, 73, 70],
    "Anaya": [86, 89, 92]
}

# Calculate average marks
averages = {
    name: sum(scores) / len(scores)
    for name, scores in marks_data.items()
}

# Sort by average marks in descending order
rankings = sorted(
    averages.items(),
    key=lambda item: item[1],
    reverse=True
)

print(f"{'Name':<15} | {'Average Score':<12}")
print("-" * 32)

for name, average in rankings:
    print(f"{name:<15} | {average:<12.2f}")

topper = rankings[0]

print("-" * 32)
print(f"Class Topper: {topper[0]} with Average: {topper[1]:.2f}")
```
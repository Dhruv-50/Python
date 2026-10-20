python
```
# 30.5 2D Matrix (Nested List)

grid = [
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
]

# (a) Display matrix in table format
print("3x3 Matrix:")
for line in grid:
    print(" ".join(f"{value:3d}" for value in line))

# (b) Calculate sum of each row
print("\nSum of Each Row:")
for number, line in enumerate(grid, start=1):
    print(f"  Row {number} Total: {sum(line)}")

# (c) Calculate main diagonal sum
diagonal_total = sum(grid[i][i] for i in range(len(grid)))
print(f"\nDiagonal Total: {diagonal_total}")
```
# Grid Pattern — Dynamic Programming

## What Is the Grid Pattern?

The **Grid Pattern** is a family of DP problems where you solve a 2D problem by filling in a table (grid) cell by cell.

The core idea:

> Each cell's answer depends only on its **neighbors** (usually the cell above and the cell to the left).

You fill the grid from top-left to bottom-right, and by the time you reach the bottom-right corner — you have your answer.

---

## The Mental Model

Think of each cell in the grid as asking:

> "How many ways / what's the best value I can achieve if I'm only allowed to look at the rows and columns up to me?"

You answer the easy cells first (borders), then use those answers to fill the harder cells.

---

## The Template

Almost every grid pattern problem follows this skeleton:

```python
# 1. Create a 2D grid (often with +1 padding for empty base cases)
grid = [[0] * (n + 1) for _ in range(m + 1)]

# 2. Fill base cases (first row and/or first column)
for i in range(m):
    grid[i][0] = base_case
for j in range(n):
    grid[0][j] = base_case

# 3. Fill the rest
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if condition:
            grid[i][j] = some_formula(grid[i-1][j-1])
        else:
            grid[i][j] = another_formula(grid[i-1][j], grid[i][j-1])

# 4. Answer is in the bottom-right corner
return grid[m][n]
```

### Space Optimization

Many grid problems can be reduced from **O(m × n)** space to **O(n)** by keeping only **one row** (or column) at a time, since each row only depends on the row directly above it.

```python
row = [initial_values] * n

for i in range(1, m):
    for j in range(1, n):
        row[j] = formula(row[j], row[j-1])  # row[j] = "above", row[j-1] = "left"

return row[-1]
```

---

## Problems in This Section

| Problem | Description | Solutions |
|---|---|---|
| [Unique Paths](unique_paths.md) | Count paths for a robot on a grid (right/down only) | Full Grid, Single Row |
| [Unique Paths with Obstacles](unique_paths_obstacles.md) | Same, but some cells are blocked | Single Array |
| [Longest Common Subsequence](longest_common_subsequence.md) | Find the longest matching subsequence of two strings | Full Grid, Space-Optimized |

---

## When to Use the Grid Pattern

Use this pattern when:
- You have **two sequences** and need to compare/combine them (LCS, Edit Distance, etc.)
- You have a **2D grid** and movement is restricted (Unique Paths, Min Path Sum)
- The answer to a cell depends on a **fixed set of neighbors** (usually above and/or left)

---

## Key Things to Remember

1. **Add +1 padding** for the empty string / empty row base case when comparing two sequences.
2. **First row and column** are always base cases — fill them first.
3. The grid approach trades **O(m × n) space** for clarity; the single-row trick trades clarity for **O(n) space**.
4. The answer is **always** in the last cell you fill (bottom-right corner, or last element of the row).

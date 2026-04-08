# Unique Paths

## The Problem

Imagine a robot is sitting in the **top-left corner** of a grid (like a chessboard). It wants to reach the **bottom-right corner**.

The robot can only move in **two directions**:
- **Right** →
- **Down** ↓

Given a grid of size `m` rows × `n` columns, **how many different paths** can the robot take to reach the bottom-right corner?

**Example:** A 3×7 grid has **28** unique paths.

```
S . . . . . .
. . . . . . .
. . . . . . E
```
`S` = Start (top-left), `E` = End (bottom-right)

---

## Why is This a DP Problem?

At every cell, the number of ways to reach it depends on the cells before it:
> "The number of ways to reach cell (i, j) = ways to reach (i-1, j) [from above] + ways to reach (i, j-1) [from the left]"

This is a **classic overlapping subproblem** — we reuse answers we've already computed.

---

## The Key Insight

- The **first row** only has one way to reach each cell — keep going right. So every cell in row 0 = **1**.
- The **first column** only has one way to reach each cell — keep going down. So every cell in column 0 = **1**.
- Every other cell = **above + left**.

---

## Solution 1: Full Grid (Brute Force DP)

### The Analogy

Think of the grid as a city map. Each intersection shows you: "How many different routes can you take from the starting corner to get here?"

You fill the map intersection by intersection — top-to-bottom, left-to-right.

### Step 1: Set up the grid

```python
grid = [[0] * n for _ in range(m)]
```

This creates an `m × n` grid filled with zeros. We'll fill it in one cell at a time.

### Step 2: Fill the first row — all 1s

The robot can only come from the **left** in the first row (it can't come from above). So there's exactly **1 way** to reach each cell in row 0.

```python
for i in range(n):
    grid[0][i] = 1  # First row: only 1 path to each cell
```

```
[ 1  1  1  1  1  1  1 ]
[ 0  0  0  0  0  0  0 ]
[ 0  0  0  0  0  0  0 ]
```

### Step 3: Fill the first column — all 1s

Similarly, the robot can only come from **above** in the first column. So exactly **1 way** to each cell in column 0.

```python
for i in range(m):
    grid[i][0] = 1  # First column: only 1 path to each cell
```

```
[ 1  1  1  1  1  1  1 ]
[ 1  0  0  0  0  0  0 ]
[ 1  0  0  0  0  0  0 ]
```

### Step 4: Fill the rest of the grid

For every other cell: `paths = from_above + from_left`

```python
for i in range(1, m):
    for j in range(1, n):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]
```

Fully filled for a 3×7 grid:

```
[  1   1   1   1   1   1   1 ]
[  1   2   3   4   5   6   7 ]
[  1   3   6  10  15  21  28 ]
```

The answer is the **bottom-right cell**: `grid[-1][-1]` = **28**.

### Step 5: Return the answer

```python
return grid[-1][-1]
```

### Full Code

```python
def unique_paths_brute_force(self, m: int, n: int) -> int:
    grid = [[0] * n for _ in range(m)]

    for i in range(n):
        grid[0][i] = 1  # First row can only be reached from the left

    for i in range(m):
        grid[i][0] = 1  # First column can only be reached from above

    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]  # from above + from left

    return grid[-1][-1]
```

### Complexity

| Type | Value |
|---|---|
| Time | O(m × n) — visit every cell once |
| Space | O(m × n) — store the entire grid |

---

## Solution 2: Single Row (Space Optimized)

### The Insight

Look at the grid-filling formula again:

```
grid[i][j] = grid[i-1][j] + grid[i][j-1]
```

When we're filling row `i`, we only ever look at:
- `grid[i-1][j]` → the cell **directly above** (the previous row)
- `grid[i][j-1]` → the cell **to the left** (already updated this row)

We never need rows older than the one above. So instead of storing the whole grid, we can get away with **a single row** and update it in place!

### The Analogy

Imagine you're painting the city map row by row, but you only have one strip of paper. After finishing each row, you repaint that same strip with the next row's values — reusing the paper.

### Step 1: Initialize the row with all 1s

This represents the first row of our grid — every cell in row 0 has exactly 1 path.

```python
row = [1] * n
```

### Step 2: Update the row for each subsequent row

For row `i` (starting from row 1), we update each cell left-to-right:
- `row[j]` currently holds the value from the **row above** (exactly what we need!)
- We add `row[j-1]` which now holds the **updated left neighbor** of the current row

```python
for i in range(1, m):
    for j in range(1, n):
        row[j] = row[j] + row[j-1]
```

Let's trace for m=3, n=7:

```
Start:  [1, 1, 1, 1, 1, 1, 1]   ← row 0
After row 1: [1, 2, 3, 4, 5, 6, 7]
After row 2: [1, 3, 6, 10, 15, 21, 28]  ← answer is row[-1] = 28
```

### Step 3: Return the last element

```python
return row[-1]
```

### Full Code

```python
def unique_paths_single_row(self, m: int, n: int) -> int:
    row = [1] * n  # Initialize first row with 1s

    for i in range(1, m):
        for j in range(1, n):
            row[j] = row[j] + row[j-1]  # above + left (in-place update)

    return row[-1]
```

### Complexity

| Type | Value |
|---|---|
| Time | O(m × n) — still visit every cell once |
| Space | O(n) — only one row stored at a time |

---

## Comparison of Both Solutions

| | Solution 1 (Full Grid) | Solution 2 (Single Row) |
|---|---|---|
| Time | O(m × n) | O(m × n) |
| Space | O(m × n) | **O(n)** |
| Easier to understand? | Yes | Once you get the trick |
| Use when... | Learning / visualizing | Space is a concern |

---

## Test Cases

```python
sol = Solution()
print(sol.unique_paths_brute_force(3, 7))   # 28
print(sol.unique_paths_brute_force(3, 2))   # 3
print(sol.unique_paths_single_row(3, 7))    # 28
print(sol.unique_paths_single_row(3, 2))    # 3
```

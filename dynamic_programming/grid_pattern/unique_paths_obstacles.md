# Unique Paths with Obstacles

## The Problem

Same robot, same grid — but now there are **rocks (obstacles)** scattered on the path! The robot cannot pass through a rock.

Given a grid where:
- `0` = open cell (robot can walk here)
- `1` = obstacle (robot cannot walk here)

How many unique paths exist from the **top-left** to the **bottom-right**?

**Example:**

```
0  0  0
0  1  0    ← obstacle in the middle
0  0  0
```

Answer: **2** (the robot must go around the rock)

---

## How Is This Different From Regular Unique Paths?

In the original problem, we initialized the first row and column to all 1s. But now — if there's a rock anywhere in the first row or column, every cell **after** that rock becomes unreachable (0 paths).

Also, any cell that has an obstacle itself must be set to 0 paths — the robot can never land there.

---

## The Approach: Space-Optimized Single Array

Just like the space-optimized solution in Unique Paths, we use a **single 1D array** that gets updated row by row. This avoids storing the whole grid.

### The Analogy

Imagine the grid is a city again, but now some streets are blocked by fallen trees. You're updating a running count of "how many ways can I reach this intersection?" As you sweep row by row, whenever you hit a blocked cell, you erase the count for that intersection (set it to 0).

---

## Step-by-Step Walkthrough

### Step 1: Check the starting cell

If the very first cell `(0, 0)` has an obstacle, the robot is trapped from the start. Return 0 immediately.

```python
if obstacles_grid[0][0] == 1:
    return 0
```

### Step 2: Initialize the array

We start with `array[0] = 1` (1 way to reach the starting cell). All other cells start at 0.

```python
rows, cols = len(obstacles_grid), len(obstacles_grid[0])
array = [0] * cols
array[0] = 1
```

```
array = [1, 0, 0]   ← for a 3-column grid
```

### Step 3: Sweep row by row, column by column

For each cell `(i, j)`:

**If there's an obstacle:** Set `array[j] = 0` — this cell is blocked, zero paths lead here.

**Otherwise:** Add the paths coming from the **left** (`array[j-1]`) to the current value of `array[j]` (which already holds the count from **above**).

```python
for i in range(rows):
    for j in range(cols):
        if obstacles_grid[i][j] == 1:
            array[j] = 0           # blocked: erase any paths to this cell
        elif j > 0:
            array[j] += array[j-1] # paths from above (already in array[j]) + from left
```

> Note: When `j == 0` (first column), we skip the `+= array[j-1]` step because there's nothing to the left. The value already in `array[0]` represents paths from above.

---

## Tracing Through the Example

Grid:
```
0  0  0
0  1  0
0  0  0
```

**Start:** `array = [1, 0, 0]`

**Row 0 (no obstacles):**
- j=0: skip (first column)
- j=1: `array[1] += array[0]` → `array[1] = 0 + 1 = 1`
- j=2: `array[2] += array[1]` → `array[2] = 0 + 1 = 1`
- `array = [1, 1, 1]`

**Row 1 (obstacle at j=1):**
- j=0: skip
- j=1: obstacle! `array[1] = 0`
- j=2: `array[2] += array[1]` → `array[2] = 1 + 0 = 1`
- `array = [1, 0, 1]`

**Row 2 (no obstacles):**
- j=0: skip
- j=1: `array[1] += array[0]` → `array[1] = 0 + 1 = 1`
- j=2: `array[2] += array[1]` → `array[2] = 1 + 1 = 2`
- `array = [1, 1, 2]`

**Answer:** `array[cols-1]` = `array[2]` = **2** ✓

---

## Why Does This Work?

At any point, `array[j]` holds:
- The number of paths to reach cell `(current_row, j)`
- Before we process the left neighbors in the current row, it still holds the value from the row above — which is exactly what we need for the "from above" contribution

When we do `array[j] += array[j-1]`, we're combining:
- `array[j]` = paths from above (inherited from previous row)
- `array[j-1]` = paths from the left (already updated this row)

---

## Full Code

```python
class Solution:
    def unique_paths_obstacles(self, obstacles_grid: list[list[int]]) -> int:
        if obstacles_grid[0][0] == 1:
            return 0

        rows, cols = len(obstacles_grid), len(obstacles_grid[0])

        array = [0] * cols
        array[0] = 1  # 1 way to reach the starting cell

        for i in range(rows):
            for j in range(cols):
                if obstacles_grid[i][j] == 1:
                    array[j] = 0            # obstacle: 0 paths here
                elif j > 0:
                    array[j] += array[j-1]  # above + left

        return array[cols - 1]
```

---

## More Examples

```python
sol = Solution()

# Obstacle in middle
print(sol.unique_paths_obstacles([[0,0,0],[0,1,0],[0,0,0]]))  # 2

# Obstacle blocks top row
print(sol.unique_paths_obstacles([[0,1],[0,0]]))               # 1

# Obstacle at start
print(sol.unique_paths_obstacles([[1,0],[0,0]]))               # 0

# Obstacle blocks left column
print(sol.unique_paths_obstacles([[0,0],[1,0]]))               # 0
```

---

## Complexity

| Type | Value | Why |
|---|---|---|
| Time | O(m × n) | Every cell visited exactly once |
| Space | O(n) | Only one row (1D array) stored |

Where `m` = number of rows, `n` = number of columns.

---

## Key Difference from Unique Paths (No Obstacles)

| | No Obstacles | With Obstacles |
|---|---|---|
| First row init | All 1s | 1 until first obstacle, then 0 |
| Obstacle cells | Don't exist | Set to 0 immediately |
| Logic change | Minimal | Add an `if obstacle → 0` check |

---

## Where to Practice

| Platform | Problem | Difficulty |
|---|---|---|
| [LeetCode #63](https://leetcode.com/problems/unique-paths-ii/) | Unique Paths II | Medium |

> This problem is part of the **NeetCode 150** interview prep list.

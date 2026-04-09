# Interval Pattern — Dynamic Programming

## What Is the Interval Pattern?

The **Interval Pattern** is a family of DP problems where you solve a problem on a **contiguous segment** (interval) of a string or array, and build larger solutions by combining smaller ones.

Every problem in this family asks:

> "What is the best answer for the substring (or subarray) from index `i` to index `j`?"

The key difference from other DP patterns:

| Pattern | What `dp[i][j]` means | Fill direction |
|---|---|---|
| **Grid Pattern** | Best answer using first `i` chars of one string and first `j` chars of another | Top-left → bottom-right |
| **Interval Pattern** | Best answer for the substring `s[i..j]` of **one string** | Short intervals first → long intervals last |

---

## The Mental Model: Building from the Inside Out

Imagine you're **decorating a string of beads** to be perfectly symmetric (a palindrome). You start with single beads (trivially symmetric), then you check whether you can wrap a matching pair around the outside to extend it.

This is the core idea of interval DP:

1. **Start with the smallest intervals** — single characters (length 1). These are trivially solved.
2. **Expand outward** — for each longer interval, use the answers from its inner, shorter sub-intervals.
3. **The answer to the whole problem** is the answer for the interval spanning the entire input `[0, n-1]`.

```
Length 1: [a] [b] [c] [d] [e]   ← trivially solved
Length 2: [a,b] [b,c] [c,d] [d,e]
Length 3: [a,b,c] [b,c,d] [c,d,e]
...
Length n: [a,b,c,d,e]           ← the full problem
```

---

## The Grid Visualization

For a string of length `n`, the DP grid is `n × n`. Each cell `dp[i][j]` represents the answer for the substring `s[i..j]`.

```
      j=0  j=1  j=2  j=3  j=4
i=0  [ 1    ?    ?    ?    ?  ]  ← substrings starting at 0
i=1  [ ×    1    ?    ?    ?  ]  ← substrings starting at 1
i=2  [ ×    ×    1    ?    ?  ]  ← substrings starting at 2
i=3  [ ×    ×    ×    1    ?  ]  ← substrings starting at 3
i=4  [ ×    ×    ×    ×    1  ]  ← single character at 4
```

- **Main diagonal** (`i == j`): Base cases — single characters. Always filled first.
- **Upper triangle** (`j > i`): The cells we fill, from the diagonal outward.
- **Lower triangle** (`j < i`): Invalid — a substring can't end before it starts. Leave as 0.
- **Top-right corner** (`dp[0][n-1]`): The answer to the full problem.

We fill **diagonal by diagonal**, moving from the main diagonal toward the top-right corner.

---

## Why Not Just Fill Top-Left to Bottom-Right?

In the Grid Pattern (e.g., LCS), `dp[i][j]` only depends on cells to the **above-left** — so top-left-to-bottom-right works perfectly.

In the Interval Pattern, `dp[i][j]` depends on **cells inside the same grid that represent shorter intervals**:
- `dp[i+1][j-1]` — one step inward from both ends
- `dp[i+1][j]` — shorter interval, excluding the left end
- `dp[i][j-1]` — shorter interval, excluding the right end

All three of these represent **shorter** intervals, which are on **earlier diagonals**. So we must fill shorter intervals before longer ones.

---

## The Template

```python
n = len(s)

# 1. Create the full n×n grid
dp = [[0] * n for _ in range(n)]

# 2. Base case: every single character
for i in range(n):
    dp[i][i] = base_value  # e.g., 1 for palindrome problems

# 3. Fill by interval length, from 2 up to n
for length in range(2, n + 1):     # length of current interval
    for i in range(n - length + 1):  # starting index
        j = i + length - 1           # ending index

        if condition(s[i], s[j]):
            dp[i][j] = formula_using(dp[i + 1][j - 1])
        else:
            dp[i][j] = formula_using(dp[i + 1][j], dp[i][j - 1])

# 4. Answer is in the top-right corner
return dp[0][n - 1]
```

### Why `j = i + length - 1`?

If the interval starts at `i` and has `length` characters, the last index is:

```
j = i + (length - 1)
  = i + length - 1
```

Example: `i=2`, `length=3` → `j = 4` → interval covers indices `[2, 3, 4]`.

### Why `i` runs up to `n - length`?

The interval `[i, i+length-1]` must fit within the string. The last valid starting index is:

```
i + length - 1 ≤ n - 1
i ≤ n - length
→ range(n - length + 1)
```

---

## Space Optimization

For problems where `dp[i][j]` depends only on the row below (`dp[i+1][...]`) and the current row to the left (`dp[i][j-1]`), we can reduce space from O(n²) to O(n) using two 1D arrays.

Instead of filling by **diagonal**, we fill by **row** from the **bottom up**:

```python
prev_row = [0] * n
curr_row = [0] * n

for i in range(n - 1, -1, -1):    # bottom to top
    curr_row[i] = base_value       # base case on the diagonal
    for j in range(i + 1, n):      # left to right, upper triangle
        if condition(s[i], s[j]):
            curr_row[j] = formula_using(prev_row[j - 1])
        else:
            curr_row[j] = formula_using(prev_row[j], curr_row[j - 1])

    prev_row, curr_row = curr_row, prev_row  # move completed row to prev
    curr_row = [0] * n                       # reset for next row

return prev_row[n - 1]  # the last swap moved the answer into prev_row
```

**How the mapping works:**
- `prev_row[j]` = `dp[i+1][j]` (the row below in the 2D grid)
- `prev_row[j-1]` = `dp[i+1][j-1]` (diagonal below-left in the 2D grid)
- `curr_row[j-1]` = `dp[i][j-1]` (the cell to the left in the current row)

---

## Problems in This Section

| Problem | Description | Solutions |
|---|---|---|
| [Longest Palindromic Subsequence](longest_palindrome_subsequence.md) | Longest subsequence of a string that is a palindrome | Full Grid, Space-Optimized |
| [Palindromic Substrings](palindromic_substrings.md) | Count all contiguous substrings that are palindromes | Memoized Recursion, Interval DP, Expand Around Center |

---

## When to Use the Interval Pattern

Ask yourself:
- Is the problem about a **single string or array** (not two strings)?
- Does the answer for a **range** `[i, j]` depend on answers for **smaller ranges** inside it?
- Does **symmetry** matter — does the problem look at both ends and work inward?

If yes to any of these → Interval DP is likely the right pattern.

**Classic problems that use this pattern:**
- Longest Palindromic Subsequence
- Palindrome Partitioning
- Burst Balloons
- Matrix Chain Multiplication
- Minimum Cost to Merge Stones

---

## Key Things to Remember

1. **Fill order is by length**, not by row or column. Shorter intervals must be solved first.
2. **Only the upper triangle is valid.** `dp[i][j]` is meaningless when `j < i`.
3. **The answer is in the top-right corner**: `dp[0][n-1]`.
4. For the **space-optimized version**, fill bottom-to-top by row (instead of diagonal-by-diagonal).
5. After the final swap in the optimized version, **the answer is in `prev_row[n-1]`**, not `curr_row[n-1]`.

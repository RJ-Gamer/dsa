# Longest Common Subsequence

## The Problem

Imagine you and your friend both have a **sticker album**. Each sticker has a letter on it, and they are arranged in a line.

- Your album:     `a - b - c - d - e`
- Friend's album: `a - c - e`

You want to find the **longest matching sequence of stickers** that appears in **both albums**, in the **same order** — but you're allowed to **skip stickers** in between!

In this case, both albums share `a`, `c`, and `e` (in that order). So the answer is **3**.

> **Subsequence** = you can skip letters, but you can't rearrange them.

---

## The Analogy: The Treasure Map Grid

Think of solving this like filling in a **treasure map grid**.

- Rows = stickers in **your** album
- Columns = stickers in your **friend's** album
- Each cell on the map answers the question:
  > "If I only looked at the stickers up to this point in both albums, what's the longest matching chain I can find?"

We fill this map cell by cell, left-to-right, top-to-bottom. By the time we reach the **bottom-right corner**, we have our answer!

---

## Step-by-Step Walkthrough

### Step 1: Set Up the Grid

We create a grid with one **extra row and column** filled with zeros. Why? Because if either album is empty, there are zero matching stickers — easy!

```python
m = len(text1)  # number of stickers in your album
n = len(text2)  # number of stickers in your friend's album

grid = [[0] * (n + 1) for _ in range(m + 1)]
```

For `"abcde"` vs `"ace"`, the initial grid looks like this (6 rows x 4 columns):

```
     ""  a   c   e
""  [ 0   0   0   0 ]
a   [ 0   _   _   _ ]
b   [ 0   _   _   _ ]
c   [ 0   _   _   _ ]
d   [ 0   _   _   _ ]
e   [ 0   _   _   _ ]
```

The `_` cells are what we'll fill in next.

---

### Step 2: Fill the Border with Zeros

The first row and first column are already 0 (from our grid initialization). This represents:

- **First row:** Your friend's stickers vs an empty album = 0 matches
- **First column:** Your stickers vs an empty album = 0 matches

```python
for j in range(1, n):
    grid[0][j] = 0  # empty album vs friend's album = no matches

for i in range(1, m):
    grid[i][0] = 0  # your album vs empty album = no matches
```

> These are already 0 by default — this step just makes the logic explicit.

---

### Step 3: Fill the Grid — The Heart of the Solution

Now we go through every sticker in your album (row by row) and every sticker in your friend's album (column by column).

```python
for i in range(1, m + 1):
    for j in range(1, n + 1):
```

At each cell `(i, j)`, we compare sticker `text1[i-1]` (yours) and sticker `text2[j-1]` (your friend's).

---

#### Case A: The Stickers Match! 🎉

If the two stickers are the same letter, we found a new match! We take the number of matches found **before this sticker** (the diagonal cell) and add **1**.

```python
if text1[i - 1] == text2[j - 1]:
    grid[i][j] = 1 + grid[i - 1][j - 1]
```

Think of the diagonal cell as: *"What was the best chain I had before I considered either of these two stickers?"* Now I can extend that chain by 1.

```
     ""  a   c   e
""  [ 0   0   0   0 ]
a   [ 0   1   _   _ ]   ← 'a' == 'a', so diagonal (0) + 1 = 1
```

---

#### Case B: The Stickers Don't Match 😔

If the stickers are different, we can't extend any chain. Instead, we **borrow the best answer** we've seen so far by looking at either:
- The cell **above** `grid[i-1][j]` → best chain if we skip your current sticker
- The cell **to the left** `grid[i][j-1]` → best chain if we skip your friend's current sticker

We take whichever is **bigger**.

```python
else:
    grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])
```

---

### Step 4: Read the Answer

After filling every cell, the **bottom-right corner** of the grid holds the answer — the length of the longest common subsequence of both full strings.

```python
return grid[m][n]
```

---

## Fully Filled Grid Example

For `"abcde"` vs `"ace"`:

```
     ""  a   c   e
""  [ 0   0   0   0 ]
a   [ 0   1   1   1 ]
b   [ 0   1   1   1 ]
c   [ 0   1   2   2 ]
d   [ 0   1   2   2 ]
e   [ 0   1   2   3 ]  ← answer is 3
```

The bottom-right cell is **3**, which matches `a-c-e`.

---

## Solution 1: Full Grid (O(m × n) Space)

```python
class Solution:
    def longest_common_subsequence_mxn(self, text1: str, text2: str) -> int:
        """
        Time: O(m × n)
        Space: O(m × n)
        """
        m = len(text1)
        n = len(text2)

        # Create a grid of zeros with an extra row and column
        grid = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the grid
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Letters match! Extend the chain from diagonal
                    grid[i][j] = 1 + grid[i - 1][j - 1]
                else:
                    # No match — borrow the best from above or left
                    grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])

        # Bottom-right corner has our answer
        return grid[m][n]


sol = Solution()
print(sol.longest_common_subsequence_mxn("abcde", "ace"))           # Output: 3
print(sol.longest_common_subsequence_mxn("september", "december"))  # Output: 6
```

---

## Solution 2: Space-Optimized (O(n) Space)

### The Key Insight

Look at the recurrence again:

```
if match:     grid[i][j] = 1 + grid[i-1][j-1]   ← needs the row above, one column left
else:         grid[i][j] = max(grid[i-1][j], grid[i][j-1])  ← needs the row above, same column
```

When we're filling row `i`, we only ever look at **row `i-1`** (the previous row) and the **current row so far**. We never go further back. So we don't need to keep the entire grid — just **two rows**: `prev` (the row above) and `curr` (the row we're filling right now).

Think of it like updating a **two-line scoreboard**. Once you've used a line to compute the next one, you can erase it and reuse it.

### How It Works

```
prev  →  [row we just finished]
curr  →  [row we're building now]

After each row: swap prev ↔ curr, then reset curr to all zeros.
```

For `"abcde"` vs `"ace"`, after processing row `a` (i=1):

```
prev = [0, 1, 1, 1]   ← result of row 'a'
curr = [0, 0, 0, 0]   ← ready for row 'b'
```

After row `b` (i=2):

```
prev = [0, 1, 1, 1]   ← result of row 'b' (same as 'a' — no new matches)
curr = [0, 0, 0, 0]   ← ready for row 'c'
```

After row `c` (i=3):

```
prev = [0, 1, 2, 2]   ← 'c' matched! diagonal extended to 2
```

...and so on until `prev = [0, 1, 2, 3]` after row `e`. The answer is `prev[n]` = **3**.

### The Code

```python
class Solution:
    def longest_common_subsequence_optimal(self, first: str, second: str) -> int:
        """
        Time: O(m × n)
        Space: O(n)  — only two rows instead of the full grid
        """
        m = len(first)
        n = len(second)

        prev = [0] * (n + 1)
        curr = [0] * (n + 1)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if first[i - 1] == second[j - 1]:
                    curr[j] = 1 + prev[j - 1]  # extend chain from diagonal
                else:
                    curr[j] = max(prev[j], curr[j - 1])  # borrow best from above or left

            prev, curr = curr, prev   # finished this row — promote it to "prev"
            curr = [0] * (n + 1)      # reset curr for the next row

        return prev[n]   # prev holds the last completed row


sol = Solution()
print(sol.longest_common_subsequence_optimal("abcde", "ace"))           # Output: 3
print(sol.longest_common_subsequence_optimal("september", "december"))  # Output: 6
```

> **Why `prev[n]` and not `curr[n]`?**
> After the last iteration, we do `prev, curr = curr, prev` — which moves the finished row into `prev`. So the answer lives in `prev[n]`, not `curr[n]`.

---

## Quick Summary

| Situation | What we do |
|---|---|
| Letters match | Diagonal value + 1 |
| Letters don't match | Max of above or left |
| Either string is empty | 0 (no match possible) |
| Final answer (full grid) | Bottom-right cell: `grid[m][n]` |
| Final answer (optimized) | Last element of prev row: `prev[n]` |

---

## Complexity

| Solution | Time | Space |
|---|---|---|
| Full Grid | O(m × n) | O(m × n) — stores every cell |
| Space-Optimized | O(m × n) | O(n) — only two rows at a time |

Where `m` = length of `text1` / `first`, `n` = length of `text2` / `second`.

---

## Where to Practice

| Platform | Problem | Difficulty |
|---|---|---|
| [LeetCode #1143](https://leetcode.com/problems/longest-common-subsequence/) | Longest Common Subsequence | Medium |

> This problem is part of the **Blind 75** and **NeetCode 150** interview prep lists.

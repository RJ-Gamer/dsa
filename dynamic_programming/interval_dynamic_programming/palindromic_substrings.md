# Palindromic Substrings

## The Problem

A **palindrome** is a string that reads the same forwards and backwards. `"racecar"`, `"aba"`, `"madam"` are all palindromes.

A **substring** is a contiguous slice of a string — every character between two positions, with nothing skipped.

The **Palindromic Substrings** problem asks: *how many substrings of a given string are palindromes?*

Every single character counts as a palindrome by itself. So even `"abc"` has at least 3 palindromic substrings: `"a"`, `"b"`, `"c"`.

### Example

```
word = "aaa"
```

All substrings:
- Length 1: `"a"` (index 0), `"a"` (index 1), `"a"` (index 2) → all palindromes ✓
- Length 2: `"aa"` (index 0–1), `"aa"` (index 1–2) → both palindromes ✓
- Length 3: `"aaa"` → palindrome ✓

Total: **6 palindromic substrings.**

---

## The Analogy: The Mirror Window Test

Imagine a row of letter tiles on a table:

```
m  —  a  —  d  —  a  —  m
```

You have a transparent window you can slide along the tiles and stretch to any width. Each time you place the window over some tiles, you look at the letters inside and hold them up to a mirror. If the mirror image matches the original — it's a palindrome. Count it.

Your job: try every possible window position and size, and count all the palindromes you find.

The smart question is: *can you check faster than re-reading every window from scratch?*

The key insight: **a substring is a palindrome if its outer characters match AND the inner substring is also a palindrome.**

---

## Substrings vs. Subsequences

This problem is closely related to [Longest Palindromic Subsequence](longest_palindrome_subsequence.md), but with a crucial difference:

| | Palindromic Substrings | Longest Palindromic Subsequence |
|---|---|---|
| **Characters** | Must be contiguous — no skipping | Can skip characters |
| **Question** | *Count* how many substrings are palindromes | *Longest length* that is a palindrome |
| `"abc"` | 3 palindromic substrings | LPS = 1 |
| `"aba"` | 4 palindromic substrings | LPS = 3 |

---

## Why This Is Interval DP

`is_palindrome(i, j)` breaks down like this:

- **Base:** If `i >= j` → always a palindrome (single character or empty string).
- **Outer characters match** (`word[i] == word[j]`): `word[i..j]` is a palindrome **if and only if** `word[i+1..j-1]` is also a palindrome.
- **Outer characters don't match**: `word[i..j]` is **not** a palindrome. No need to look inside.

This is interval DP: the answer for `[i, j]` depends on the inner interval `[i+1, j-1]`.

The recurrence:

```
is_palindrome(i, j) = (word[i] == word[j])  AND  is_palindrome(i+1, j-1)
```

Unlike Longest Palindromic Subsequence — which had a `max(skip-left, skip-right)` fallback — here there is no "try both." If the outer characters don't match, the whole substring fails immediately.

---

## Setting Up the Grid

For a string of length `n`, create an `n × n` boolean grid:

```python
size = len(word)
dp = [[False] * size for _ in range(size)]
```

**What `dp[i][j]` means:** `True` if `word[i..j]` is a palindrome, `False` otherwise.

For `word = "madam"` (size=5):

```
      m    a    d    a    m
  m  [i=0  ?    ?    ?    ?  ]
  a  [ ×  i=1   ?    ?    ?  ]
  d  [ ×   ×   i=2   ?    ?  ]
  a  [ ×   ×    ×   i=3   ?  ]
  m  [ ×   ×    ×    ×   i=4 ]
```

- `×` = lower triangle (`j < i`) — invalid, a substring can't end before it starts
- `i=k` on the diagonal = single-character substrings (always `True`)
- Final answer = count all `True` cells in the upper triangle + diagonal

---

## Step 1: Base Cases — Single Characters

Every single character is a palindrome of length 1.

```python
for i in range(size):
    dp[i][i] = True
    count += 1
```

After base cases for `"madam"`:

```
      m    a    d    a    m
  m  [ T    F    F    F    F ]
  a  [ ×    T    F    F    F ]
  d  [ ×    ×    T    F    F ]
  a  [ ×    ×    ×    T    F ]
  m  [ ×    ×    ×    ×    T ]
```

Count so far: **5** (one per character).

---

## Step 2: Fill by Interval Length

Fill diagonal by diagonal, length 2 up to length `n`.

```python
for length in range(2, size + 1):
    for i in range(size - length + 1):
        j = i + length - 1
```

---

### Length 2: Adjacent Pairs

`dp[i][i+1]` is `True` if and only if `word[i] == word[i+1]`.

> Note: For length 2, `dp[i+1][j-1]` = `dp[i+1][i]` — that cell is in the lower triangle (invalid). So we handle length 2 as a special case: no inner substring, just check whether the two characters match.

| (i, j) | word[i] | word[j] | Match? | dp[i][j] |
|---|---|---|---|---|
| (0, 1) | m | a | ✗ | False |
| (1, 2) | a | d | ✗ | False |
| (2, 3) | d | a | ✗ | False |
| (3, 4) | a | m | ✗ | False |

No new palindromes. Count still: **5**.

---

### Length 3

`dp[i][j]` = `True` if `word[i] == word[j]` AND `dp[i+1][j-1]` is `True`.

| (i, j) | word[i] | word[j] | Match? | Inner dp[i+1][j-1] | dp[i][j] |
|---|---|---|---|---|---|
| (0, 2) | m | d | ✗ | — | False |
| (1, 3) | a | a | ✓ | dp[2][2] = True | **True** ✓ → `"ada"` |
| (2, 4) | d | m | ✗ | — | False |

Count: **6** (`"ada"` added).

---

### Length 4

| (i, j) | word[i] | word[j] | Match? | Inner dp[i+1][j-1] | dp[i][j] |
|---|---|---|---|---|---|
| (0, 3) | m | a | ✗ | — | False |
| (1, 4) | a | m | ✗ | — | False |

Count still: **6**.

---

### Length 5: The Full String

| (i, j) | word[i] | word[j] | Match? | Inner dp[i+1][j-1] | dp[i][j] |
|---|---|---|---|---|---|
| (0, 4) | m | m | ✓ | dp[1][3] = True (`"ada"`) | **True** ✓ → `"madam"` |

Count: **7**.

---

**Final grid for `"madam"`:**

```
      m    a    d    a    m
  m  [ T    F    F    F    T ]   ← "madam" is a palindrome
  a  [ ×    T    F    T    F ]   ← "ada" is a palindrome
  d  [ ×    ×    T    F    F ]
  a  [ ×    ×    ×    T    F ]
  m  [ ×    ×    ×    ×    T ]
```

Count all `True` cells: 5 (diagonal) + 1 (`"ada"`) + 1 (`"madam"`) = **7**. ✓

---

## Solution 1: Memoized Recursion (Top-Down)

The most direct approach: write `is_palindrome` as a recursive function and let memoization avoid recomputing the same `(i, j)` pair twice.

```python
from functools import lru_cache

class Solution:
    def palindromic_substrings(self, word: str) -> int:
        """
        Time: O(n^2) — each (i, j) pair computed once
        Space: O(n^2) — cache stores all (i, j) results + recursion stack
        """
        size = len(word)
        count = 0

        for i in range(size):
            for j in range(i, size):
                if self.is_palindrome(word, i, j):
                    count += 1

        return count

    @lru_cache(maxsize=None)
    def is_palindrome(self, word: str, left: int, right: int) -> bool:
        if left >= right:
            return True
        if word[left] != word[right]:
            return False
        return self.is_palindrome(word, left + 1, right - 1)
```

**Why it works:** `is_palindrome(word, i, j)` peels one layer at a time — checks the outer characters, then asks the same question for `word[i+1..j-1]`. The `@lru_cache` ensures each `(word, i, j)` trio is only computed once.

---

## Solution 2: Interval DP — Boolean Table (Bottom-Up)

Instead of recursing top-down, fill the `dp` table from shorter intervals to longer ones.

```python
class Solution:
    def palindromic_substrings_dp(self, word: str) -> int:
        """
        Time: O(n^2) — fill every cell in the upper triangle
        Space: O(n^2) — the full n×n boolean grid
        """
        size = len(word)
        dp = [[False] * size for _ in range(size)]
        count = 0

        # Base case: single characters
        for i in range(size):
            dp[i][i] = True
            count += 1

        # Length 2: handled separately (inner interval would be invalid)
        for i in range(size - 1):
            if word[i] == word[i + 1]:
                dp[i][i + 1] = True
                count += 1

        # Length 3 and above
        for length in range(3, size + 1):
            for i in range(size - length + 1):
                j = i + length - 1
                if word[i] == word[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1

        return count
```

**Why length 2 is handled separately:** For `length = 2`, `j = i + 1`, so `dp[i+1][j-1]` = `dp[i+1][i]`. That cell is in the lower triangle — it's invalid and stays `False`. But two identical adjacent characters *do* form a palindrome. Separating length 2 avoids reading an invalid cell and keeps the main loop clean.

---

## Solution 3: Expand Around Center (Space-Optimized)

Every palindrome has a **center**:
- Odd-length palindromes (`"aba"`, `"madam"`) have a single center character.
- Even-length palindromes (`"aa"`, `"abba"`) have a center *gap* between two characters.

Instead of checking intervals from outside in, we go the other direction: **start at every possible center and expand outward** as long as the characters match.

For a string of length `n`, there are `2n - 1` possible centers:
- `n` single-character centers (for odd-length palindromes)
- `n - 1` gap centers (for even-length palindromes)

```python
class Solution:
    def palindromic_substrings_center(self, word: str) -> int:
        """
        Time: O(n^2) — n centers × up to n expansions each
        Space: O(1) — no grid needed
        """
        size = len(word)
        count = 0

        for center in range(size):
            # Odd-length: single character at center
            left, right = center, center
            while left >= 0 and right < size and word[left] == word[right]:
                count += 1
                left -= 1
                right += 1

            # Even-length: gap between center and center+1
            left, right = center, center + 1
            while left >= 0 and right < size and word[left] == word[right]:
                count += 1
                left -= 1
                right += 1

        return count
```

### Trace for `"madam"`

| Center | Type | Expansions | Palindromes found |
|---|---|---|---|
| 0 (`m`) | Odd | `"m"` only — `word[-1]` out of bounds | `"m"` |
| 0–1 (`m`/`a`) | Even | `m ≠ a` — stop immediately | — |
| 1 (`a`) | Odd | `"a"`, then `word[0]='m' ≠ word[2]='d'` — stop | `"a"` |
| 1–2 (`a`/`d`) | Even | `a ≠ d` — stop | — |
| 2 (`d`) | Odd | `"d"`, `"ada"` (k=1), `"madam"` (k=2), then out of bounds | `"d"`, `"ada"`, `"madam"` |
| 2–3 (`d`/`a`) | Even | `d ≠ a` — stop | — |
| 3 (`a`) | Odd | `"a"`, then `word[2]='d' ≠ word[4]='m'` — stop | `"a"` |
| 3–4 (`a`/`m`) | Even | `a ≠ m` — stop | — |
| 4 (`m`) | Odd | `"m"` only — `word[5]` out of bounds | `"m"` |

Total: `"m"`, `"a"`, `"d"`, `"a"`, `"m"`, `"ada"`, `"madam"` = **7** ✓

---

## Quick Summary

| Situation | What we do |
|---|---|
| `word[i] == word[j]` AND inner is palindrome | `dp[i][j] = True`, increment count |
| `word[i] != word[j]` | `dp[i][j] = False` — no need to check inside |
| Length 1 (`i == j`) | Always `True` — base case |
| Length 2 (`j == i + 1`) | `True` iff `word[i] == word[j]` |
| Fill order (tabulated) | By interval length: short → long |
| Final answer | Count of all `True` cells |

---

## Complexity

| Solution | Time | Space |
|---|---|---|
| Memoized Recursion | O(n²) | O(n²) — cache for all (i, j) pairs |
| Interval DP (table) | O(n²) | O(n²) — full n×n boolean grid |
| Expand Around Center | O(n²) | **O(1)** — no grid needed |

Where `n` = length of `word`.

> Time is O(n²) for all three: each (i, j) pair is visited at most once. Space improves from O(n²) to O(1) with the center-expansion approach.

---

## Where to Practice

| Platform | Problem | Difficulty |
|---|---|---|
| [LeetCode #647](https://leetcode.com/problems/palindromic-substrings/) | Palindromic Substrings | Medium |

> This problem is part of the **NeetCode 150** interview prep list.

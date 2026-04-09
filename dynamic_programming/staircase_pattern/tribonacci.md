# Tribonacci

## The Problem

You may know the **Fibonacci sequence** — where each number is the sum of the previous two:

```
0, 1, 1, 2, 3, 5, 8, 13, ...
```

**Tribonacci** is the same idea, but each number is the sum of the **previous three**:

```
T(0) = 0
T(1) = 1
T(2) = 1
T(n) = T(n-1) + T(n-2) + T(n-3)
```

So the sequence goes:

```
0, 1, 1, 2, 4, 7, 13, 24, 44, ...
```

Given `n`, return `T(n)`.

**Example:** `T(5)` = `0 + 1 + 1 + 2 + 4 + 7` → `T(5) = 7`

---

## Why DP?

If you compute `T(n)` naively with recursion (no memoization), you recalculate the same values over and over. For example, computing `T(10)` would re-compute `T(7)` multiple times.

DP avoids this by only computing each value **once**, keeping track of just the last three.

---

## The Solution: Space-Optimized (Three Variables)

### The Analogy

Imagine you're counting scores in a ball game where each round's score equals the sum of the **last three rounds**. You don't need a history book — you only need to remember the last three scores written on a tiny whiteboard.

After each new round, you erase the oldest score and write the new one.

### Code

```python
def tribonacci(self, n: int) -> int:
    if n == 0:
        return 0
    if n <= 2:
        return 1

    t0, t1, t2 = 0, 1, 1  # T(0), T(1), T(2)

    for _ in range(3, n + 1):
        t0, t1, t2 = t1, t2, t0 + t1 + t2

    return t2
```

### What Do the Variables Mean?

At any point in the loop:

| Variable | Meaning |
|---|---|
| `t0` | T(i-2) — three steps back at start, slides forward |
| `t1` | T(i-1) |
| `t2` | T(i)   — the current value we just computed |

After each iteration, the window slides one step forward:
- Old `t1` becomes new `t0`
- Old `t2` becomes new `t1`
- New `t2` = old `t0 + t1 + t2`

Python's simultaneous assignment handles this cleanly — the right side is evaluated with the **old values** before any assignment happens.

### Tracing for n = 5

```
Start:  t0=0, t1=1, t2=1

i=3:  t0=1, t1=1, t2=0+1+1=2     → [1, 1, 2]
i=4:  t0=1, t1=2, t2=1+1+2=4     → [1, 2, 4]
i=5:  t0=2, t1=4, t2=1+2+4=7     → [2, 4, 7]

Answer: t2 = 7
```

Verify: `T(5) = T(4) + T(3) + T(2) = 4 + 2 + 1 = 7` ✓

### Complexity

| Type | Value | Why |
|---|---|---|
| Time | O(n) | Loop runs n-2 times |
| Space | **O(1)** | Only three variables |

---

## Comparing Fibonacci vs Tribonacci

| | Fibonacci | Tribonacci |
|---|---|---|
| Depends on | Last 2 values | Last 3 values |
| Variables needed | 2 (`t1`, `t2`) | 3 (`t0`, `t1`, `t2`) |
| Base cases | `f(1)=1, f(2)=1` | `T(0)=0, T(1)=1, T(2)=1` |
| Pattern | `t1, t2 = t2, t1+t2` | `t0,t1,t2 = t1,t2,t0+t1+t2` |

The pattern is the same — you just extend the sliding window by one more variable.

---

## Test Output

```python
sol = Solution()
print(sol.tribonacci(0))   # 0
print(sol.tribonacci(1))   # 1
print(sol.tribonacci(4))   # 4
print(sol.tribonacci(5))   # 7
print(sol.tribonacci(25))  # 1389537
```

---

## Where to Practice

| Platform | Problem | Difficulty |
|---|---|---|
| [LeetCode #1137](https://leetcode.com/problems/n-th-tribonacci-number/) | N-th Tribonacci Number | Easy |

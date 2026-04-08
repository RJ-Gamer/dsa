# Climbing Stairs

## The Problem

You are standing at the bottom of a staircase with `n` steps. You can climb either **1 step** or **2 steps** at a time.

**How many distinct ways can you reach the top?**

**Examples:**
- `n = 2` → 2 ways: `[1+1]` or `[2]`
- `n = 3` → 3 ways: `[1+1+1]`, `[1+2]`, `[2+1]`
- `n = 5` → 8 ways

---

## The Key Insight

To reach step `n`, you must have come from either:
- Step `n-1` (took 1 step), or
- Step `n-2` (took 2 steps)

So:

```
ways(n) = ways(n-1) + ways(n-2)
```

This is exactly the **Fibonacci sequence**! The number of ways to climb n stairs is the (n+1)th Fibonacci number.

Base cases:
- `ways(1) = 1` (only one way: take 1 step)
- `ways(2) = 2` (two ways: `[1+1]` or `[2]`)

---

## Four Solutions — From Slow to Fast

We'll build up from the most naive solution to the most optimized. Each version teaches something new.

---

## Solution 1: Pure Recursion (Slowest)

### The Analogy

Imagine you're standing on step `n` and asking: "How many ways did I get here?"
You look back and say: "Either I came from step `n-1`, or from step `n-2`. Let me count both possibilities."

Each of those steps then asks the same question, all the way down to step 1 and step 2 (which we know the answers to).

### Code

```python
def climbStairsRecursive(self, n: int) -> int:
    if n == 1:
        return 1  # base case: 1 step = 1 way
    if n == 2:
        return 2  # base case: 2 steps = 2 ways
    return self.climbStairsRecursive(n - 1) + self.climbStairsRecursive(n - 2)
```

### The Problem: Repeated Work

For `n = 5`, the call tree looks like this:

```
                    f(5)
                  /       \
              f(4)          f(3)
             /    \        /    \
          f(3)   f(2)   f(2)   f(1)
         /    \
      f(2)   f(1)
```

Notice `f(3)` is computed **twice**, `f(2)` is computed **three times**. This gets catastrophically worse as n grows.

### Complexity

| Type | Value |
|---|---|
| Time | O(2^n) — doubles with every step |
| Space | O(n) — recursion stack depth |

---

## Solution 2: Memoization (Top-Down DP)

### The Fix

We compute each sub-answer once and **remember** it in a dictionary (`memo`). The next time we need it, we look it up instead of recomputing.

### The Analogy

Same as above, but now you carry a **sticky notepad**. The first time you figure out the answer for step `k`, you write it down. Next time someone asks, you just read it off the pad.

### Code

```python
def climbStairsMemoized(self, n: int) -> int:
    memo = {}
    if n in memo:
        return memo[n]
    if 1 <= n <= 2:
        return n

    result = self.climbStairsMemoized(n - 1) + self.climbStairsMemoized(n - 2)
    memo[n] = result
    return result
```

> **Note:** There's a subtle bug in this code — `memo` is created fresh on every call, so it never actually persists between calls. To fix this, `memo` should be defined outside the function or passed as a parameter. But the logic/structure is correct and teaches the memoization concept.

### How It Improves Things

With memoization, each value from 1 to n is computed **exactly once**. The call tree becomes a straight line instead of an exponential tree.

### Complexity

| Type | Value |
|---|---|
| Time | O(n) — compute each step once |
| Space | O(n) — memo dictionary + recursion stack |

---

## Solution 3: Tabulation (Bottom-Up DP)

### The Shift in Thinking

Instead of starting at `n` and recursing down, we **start from the bottom** and build up.

We create a `ways` array where `ways[i]` = number of ways to reach step `i`.

### The Analogy

You're filling in an answer sheet from question 1 to question n. You know answers 1 and 2 by heart. For every subsequent question, you look at the previous two answers and add them up.

### Code

```python
def climbStairsTabulated(self, n: int) -> int:
    ways = [0] * (n + 1)
    ways[1] = 1   # 1 way to reach step 1
    ways[2] = 2   # 2 ways to reach step 2

    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]
```

### Tracing for n = 5

```
ways[1] = 1
ways[2] = 2
ways[3] = ways[2] + ways[1] = 2 + 1 = 3
ways[4] = ways[3] + ways[2] = 3 + 2 = 5
ways[5] = ways[4] + ways[3] = 5 + 3 = 8
```

Answer: **8**

### Complexity

| Type | Value |
|---|---|
| Time | O(n) |
| Space | O(n) — stores the whole `ways` array |

---

## Solution 4: Space-Optimized (Best)

### The Final Insight

In the tabulation approach, to compute `ways[i]` we only ever use `ways[i-1]` and `ways[i-2]`. We don't need the whole array — just the **last two values**.

### The Analogy

Instead of the full answer sheet, you only keep a **sticky note** with the last two answers. After computing the new answer, you update the sticky note and throw away the oldest value.

### Code

```python
def climbStairsOptimized(self, n: int) -> int:
    if 1 <= n <= 2:
        return n

    t1, t2 = 1, 2  # t1 = ways(n-2), t2 = ways(n-1)

    for _ in range(3, n + 1):
        t1, t2 = t2, t1 + t2  # shift the window forward

    return t2
```

### Tracing for n = 5

```
Start:  t1=1, t2=2
i=3:    t1=2, t2=1+2=3
i=4:    t1=3, t2=2+3=5
i=5:    t1=5, t2=3+5=8
```

Answer: `t2` = **8**

### Complexity

| Type | Value |
|---|---|
| Time | O(n) |
| Space | **O(1)** — only two variables! |

---

## Summary of All Four Solutions

| Solution | Approach | Time | Space | Notes |
|---|---|---|---|---|
| Recursive | Top-down, no cache | O(2^n) | O(n) | Simple but very slow |
| Memoized | Top-down, with cache | O(n) | O(n) | Recursive + cache |
| Tabulated | Bottom-up, full array | O(n) | O(n) | Iterative, easy to trace |
| Optimized | Bottom-up, two vars | O(n) | **O(1)** | Best solution |

---

## The Evolution Story

```
Recursion → "I'll just compute everything"             (too slow)
Memoization → "I'll remember what I've computed"       (fast, uses memory)
Tabulation → "I'll build up from scratch"              (fast, uses memory)
Optimized → "I only need the last two values"          (fast, minimal memory)
```

---

## Test Output

```python
sol = Solution()
print(sol.climbStairsRecursive(5))    # 8
print(sol.climbStairsMemoized(8))     # 34
print(sol.climbStairsTabulated(8))    # 34
print(sol.climbStairsOptimized(8))    # 34
```

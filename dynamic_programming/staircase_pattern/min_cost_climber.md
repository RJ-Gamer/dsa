# Min Cost Climbing Stairs

## The Problem

You have a staircase. Each step has a **cost** to step on it (like a toll). Once you pay the cost of a step, you can jump **1 or 2 steps** forward.

You can start from **step 0** or **step 1** (your choice). You want to reach the **top** (past the last step) with the **minimum total cost**.

**Example:**

```
costs = [10, 15, 20]
```

- Path 1: Step 0 (pay 10) → Step 2 (pay 20) → Top = 30
- Path 2: Step 1 (pay 15) → Top = 15
- Path 3: Step 0 (pay 10) → Step 1 (pay 15) → Top = 25

Minimum cost = **15** ✓

---

## The Key Insight

At each step `i`, the cheapest cost to step on it is:

```
cost[i] + min(cheapest way to get to i-1, cheapest way to get to i-2)
```

The total cost to reach step `i` = the step's own toll + the cheaper of the two paths leading to it.

The answer is:
```
min(cheapest to reach last step, cheapest to reach second-to-last step)
```
Because from either of these, you can jump straight to the top.

---

## Solution 1: Tabulation (Full Array)

### The Analogy

Imagine you have a receipt for each step, showing "the cheapest total price to arrive here." You fill out each receipt by looking at the two previous receipts and picking the cheaper one.

### Code

```python
def min_cost_climber_tabulated(self, costs: list[int]) -> int:
    if not costs:
        return 0
    if len(costs) <= 2:
        return min(costs)

    dp = [0] * len(costs)
    dp[0], dp[1] = costs[0], costs[1]  # base cases: cost to stand on step 0 or 1

    for i in range(2, len(costs)):
        dp[i] = costs[i] + min(dp[i - 1], dp[i - 2])

    return min(dp[-1], dp[-2])
```

### Tracing for `costs = [10, 15, 20, 4, 6, 8]`

```
dp[0] = 10   (cost to be on step 0)
dp[1] = 15   (cost to be on step 1)
dp[2] = 20 + min(15, 10) = 20 + 10 = 30
dp[3] =  4 + min(30, 15) = 4  + 15 = 19
dp[4] =  6 + min(19, 30) = 6  + 19 = 25
dp[5] =  8 + min(25, 19) = 8  + 19 = 27
```

Answer: `min(dp[-1], dp[-2])` = `min(27, 25)` = **25**

Wait — let me double-check: can you skip step 5 entirely?
- From step 3 (cost 19), jump 2 steps → step 5 (cost 8+19 = 27), then jump to top
- From step 4 (cost 25), jump 1 step → top

Actually `min(dp[-1], dp[-2]) = min(27, 25) = 25` is correct.

### Complexity

| Type | Value |
|---|---|
| Time | O(n) |
| Space | O(n) — stores full `dp` array |

---

## Solution 2: Space-Optimized (Two Variables)

### The Insight

Same as Climbing Stairs — we only ever look at the **last two values** in `dp`. So we can replace the whole array with just two variables.

### The Analogy

Instead of writing every receipt, you only keep the **last two receipts** in your hand. After computing the new one, you slide your hand forward and drop the oldest.

### Code

```python
def min_cost_climber(self, costs: list[int]) -> int:
    if not costs:
        return 0
    if len(costs) <= 2:
        return min(costs)

    t0, t1 = costs[0], costs[1]  # t0 = dp[i-2], t1 = dp[i-1]

    for i in range(2, len(costs)):
        t0, t1 = t1, costs[i] + min(t0, t1)

    return min(t0, t1)
```

### Tracing for `costs = [10, 15, 20, 4, 6, 8]`

```
Start:  t0=10, t1=15

i=2: new t1 = 20 + min(10, 15) = 30,  t0=15, t1=30
i=3: new t1 =  4 + min(15, 30) = 19,  t0=30, t1=19
i=4: new t1 =  6 + min(30, 19) = 25,  t0=19, t1=25
i=5: new t1 =  8 + min(19, 25) = 27,  t0=25, t1=27

Answer: min(t0, t1) = min(25, 27) = 25
```

### Why `t0, t1 = t1, costs[i] + min(t0, t1)`?

Python evaluates the **right side first**, so `min(t0, t1)` uses the old values before the assignment happens. This is the Python simultaneous assignment trick — no need for a temp variable.

### Complexity

| Type | Value |
|---|---|
| Time | O(n) |
| Space | **O(1)** — only two variables |

---

## Comparison

| | Tabulated | Optimized |
|---|---|---|
| Time | O(n) | O(n) |
| Space | O(n) | **O(1)** |
| Easier to debug? | Yes (full array visible) | Harder to trace |

---

## Edge Cases

```python
# Empty staircase
min_cost_climber([])            # 0

# One or two steps: just pick the cheaper one
min_cost_climber([10])          # 10
min_cost_climber([10, 15])      # 10
```

---

## Full Test Output

```python
sol = Solution()
print(sol.min_cost_climber([10, 15, 20, 4, 6, 8]))           # 25
print(sol.min_cost_climber_tabulated([10, 15, 20, 4, 6, 8])) # 25
```

---

## Where to Practice

| Platform | Problem | Difficulty |
|---|---|---|
| [LeetCode #746](https://leetcode.com/problems/min-cost-climbing-stairs/) | Min Cost Climbing Stairs | Easy |

> This problem is part of the **NeetCode 150** interview prep list.

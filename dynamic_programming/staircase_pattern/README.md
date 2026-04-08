# Staircase Pattern — Dynamic Programming

## What Is the Staircase Pattern?

The **Staircase Pattern** is a family of DP problems where:

- You move **forward one step at a time** through a sequence (array or just a number)
- At each step, your best outcome depends on a **small number of previous steps** (usually 2 or 3)
- You build up the answer from the bottom, step by step

The name comes from the classic "Climbing Stairs" problem, but the same pattern shows up in problems about money, games, sequences, and more.

---

## The Mental Model

At each position `i`, ask:

> "What's the best I can do at position `i`, given the best outcomes I already know for positions `i-1`, `i-2`, (and maybe `i-3`)?"

You start from the **beginning** (bottom of the stairs), compute small answers, and build up to the final answer at the end.

---

## The Template

### Step 1: Identify the recurrence

Figure out how `dp[i]` depends on previous values. It almost always looks like:

```python
dp[i] = f(dp[i-1], dp[i-2])          # depends on 2 previous
dp[i] = f(dp[i-1], dp[i-2], dp[i-3]) # depends on 3 previous
```

### Step 2: Identify base cases

What are the smallest inputs you can answer directly without the formula?

```python
dp[0] = ...
dp[1] = ...
```

### Step 3: Fill the table

```python
dp = [0] * (n + 1)
dp[0] = base_case_0
dp[1] = base_case_1

for i in range(2, n + 1):
    dp[i] = recurrence formula
```

### Step 4: Optimize space (if needed)

If you only need 2 (or 3) previous values, replace the array with variables:

```python
# 2-step lookback
prev1, prev2 = base_0, base_1
for i in range(2, n + 1):
    prev1, prev2 = prev2, f(prev1, prev2)

# 3-step lookback
t0, t1, t2 = base_0, base_1, base_2
for i in range(3, n + 1):
    t0, t1, t2 = t1, t2, f(t0, t1, t2)
```

---

## Problems in This Section

| Problem | Description | Solutions | Space |
|---|---|---|---|
| [Climb Stairs](climb_stairs.md) | How many ways to reach the top (1 or 2 steps at a time)? | Recursive, Memoized, Tabulated, Optimized | O(1) best |
| [Min Cost Climber](min_cost_climber.md) | Reach the top with minimum total toll cost | Tabulated, Optimized | O(1) best |
| [House Robber](robber.md) | Rob non-adjacent houses for maximum money | Tabulated, Optimized | O(1) best |
| [Tribonacci](tribonacci.md) | Each number = sum of previous three | Optimized | O(1) |

---

## How the Problems Are Connected

All four problems share the same **skeleton**. What changes is what the recurrence formula computes:

| Problem | Recurrence |
|---|---|
| Climb Stairs | `dp[i] = dp[i-1] + dp[i-2]` |
| Tribonacci | `dp[i] = dp[i-1] + dp[i-2] + dp[i-3]` |
| Min Cost Climber | `dp[i] = cost[i] + min(dp[i-1], dp[i-2])` |
| House Robber | `dp[i] = max(dp[i-1], dp[i-2] + nums[i])` |

Learning one gives you a massive head start on all the others.

---

## The Evolution of Solutions

Every problem in this section follows the same optimization journey:

```
1. Recursive (no cache)    → Simple but exponentially slow
2. Memoized (top-down DP)  → Fast but uses extra space for the call stack
3. Tabulated (bottom-up)   → Fast, easy to trace, uses O(n) space
4. Space-optimized         → Fast, uses O(1) space — the gold standard
```

You don't always need to go through all four. But understanding each step is key to understanding **why** DP works.

---

## When to Use the Staircase Pattern

Use this pattern when:
- You move **linearly** through a sequence (left to right, step by step)
- The value at each position depends on a **fixed small window** of previous positions
- You're asked for a **count**, **max**, **min**, or **optimal value** at the end
- There are clear **base cases** at positions 0 and 1

---

## Key Things to Remember

1. Always write out the recurrence before coding.
2. Always handle edge cases (`n=0`, `n=1`, `n=2`) before the loop.
3. The space optimization only works when the lookback window is fixed and small.
4. Python's simultaneous assignment (`a, b = b, a + b`) is your friend — it evaluates the right side with old values before assigning.

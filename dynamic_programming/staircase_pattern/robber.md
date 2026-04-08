# House Robber

## The Problem

You are a robber planning to rob houses along a street. Each house has some amount of money in it.

**The catch:** You cannot rob **two houses that are next to each other** — the security systems will alert the police if two adjacent houses are broken into on the same night.

Given an array `nums` where `nums[i]` is the money in house `i`, find the **maximum amount you can rob** tonight.

**Example:**

```
nums = [2, 7, 9, 3, 1]
```

- Rob houses 0, 2, 4: `2 + 9 + 1 = 12`
- Rob houses 1, 3:    `7 + 3 = 10`
- Rob houses 0, 2:    `2 + 9 = 11`

Maximum = **12** ✓

---

## The Key Insight

At each house `i`, you make a choice:
- **Rob it:** Earn `nums[i]`, but you cannot rob house `i-1`. Best you could have gotten before = `best up to i-2` + `nums[i]`.
- **Skip it:** Don't earn anything from house `i`, but keep the best you had through `i-1`.

So:
```
max_rob[i] = max(max_rob[i-1],  max_rob[i-2] + nums[i])
             ↑ skip house i      ↑ rob house i
```

Base cases:
- `max_rob[0] = nums[0]` — only one house, rob it
- `max_rob[1] = max(nums[0], nums[1])` — two houses, pick the richer one

---

## Solution 1: Tabulation (Full Array)

### The Analogy

Imagine a scoreboard. Each slot `i` on the board answers: "What's the maximum I can earn if I only consider houses 0 through i?"

You fill the scoreboard left-to-right. To fill slot `i`, you compare:
- The score at slot `i-1` (skip this house)
- The score at slot `i-2` plus the money in house `i` (rob this house)

```python
def robber_tabulated(self, nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)

    max_robbed = [0] * len(nums)
    max_robbed[0] = nums[0]
    max_robbed[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        max_robbed[i] = max(max_robbed[i-1], max_robbed[i-2] + nums[i])

    return max_robbed[-1]
```

### Tracing for `nums = [2, 7, 9, 3, 1]`

```
max_robbed[0] = 2
max_robbed[1] = max(2, 7) = 7

i=2: max(7,  2+9) = max(7,  11) = 11
i=3: max(11, 7+3) = max(11, 10) = 11
i=4: max(11, 11+1)= max(11, 12) = 12
```

Answer: `max_robbed[-1]` = **12** ✓

### Complexity

| Type | Value |
|---|---|
| Time | O(n) |
| Space | O(n) — full `max_robbed` array |

---

## Solution 2: Space-Optimized (Two Variables)

### The Insight

Again, we only ever look at the **last two values**. We can replace the whole array with `prev1` (two steps back) and `prev2` (one step back).

### The Analogy

You only remember: "What was the best I had two houses ago?" and "What was the best I had one house ago?" Everything older can be forgotten.

```python
def robber_optimized(self, nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)

    prev1, prev2 = nums[0], max(nums[0], nums[1])

    for i in range(2, len(nums)):
        current = max(prev1 + nums[i], prev2)
        prev1, prev2 = prev2, current

    return prev2
```

### Variable Meaning

| Variable | Meaning |
|---|---|
| `prev1` | Best amount achievable up to 2 houses ago (`max_robbed[i-2]`) |
| `prev2` | Best amount achievable up to 1 house ago (`max_robbed[i-1]`) |
| `current` | Best amount achievable up to current house |

### Tracing for `nums = [2, 7, 9, 3, 1]`

```
Start: prev1=2, prev2=7

i=2: current = max(2+9, 7) = max(11, 7) = 11
     prev1=7, prev2=11

i=3: current = max(7+3, 11) = max(10, 11) = 11
     prev1=11, prev2=11

i=4: current = max(11+1, 11) = max(12, 11) = 12
     prev1=11, prev2=12

Answer: prev2 = 12
```

### Complexity

| Type | Value |
|---|---|
| Time | O(n) |
| Space | **O(1)** |

---

## Why `max(prev1 + nums[i], prev2)` and Not `max(prev2 + nums[i], prev1)`?

This trips people up. Let's be precise:

- `prev2` = best earnings up through house `i-1` (the house right before)
- Since you can't rob adjacent houses, you **cannot** add `nums[i]` to `prev2`
- `prev1` = best earnings up through house `i-2` (two houses back — safe to combine with house `i`)

So the formula is:
```
rob house i:   prev1 + nums[i]   ← two houses ago + current
skip house i:  prev2             ← just carry forward the best so far
```

---

## Comparison

| | Tabulated | Optimized |
|---|---|---|
| Time | O(n) | O(n) |
| Space | O(n) | **O(1)** |
| Easier to debug? | Yes | Harder to trace |

---

## Test Output

```python
sol = Solution()
print(sol.robber_tabulated([1, 2, 3, 1]))   # 4
print(sol.robber_tabulated([2, 7, 9, 3, 1]))  # 12
print(sol.robber_optimized([1, 2, 3, 1]))   # 4
print(sol.robber_optimized([2, 7, 9, 3, 1])) # 12
```

---

## Connection to Climbing Stairs

The House Robber and Climbing Stairs problems share the same recurrence structure:

```
result[i] = f(result[i-1], result[i-2])
```

The difference is just **what** that function `f` does:
- Climbing Stairs: `f = +` (add the two previous counts)
- House Robber: `f = max(prev2, prev1 + nums[i])` (pick the better option)

Both reduce to O(1) space with the same two-variable sliding window trick.

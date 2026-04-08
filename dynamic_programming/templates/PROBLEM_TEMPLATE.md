# [Problem Title]

<!-- One sentence: what does this problem ask you to do? -->

## The Problem

<!-- Describe the problem in plain English. No LeetCode jargon.
     Imagine you're explaining it to someone who has never coded.
     Use a concrete, relatable scenario if possible. -->

**Example:**

```
input  = ...
output = ...   (explain why)
```

---

## The Key Insight

<!-- Before any code — explain the recurrence in words.
     What does dp[i] represent? How does it depend on dp[i-1], dp[i-2]?
     Write out the formula. State the base cases. -->

```
dp[i] = ...

Base cases:
  dp[0] = ...
  dp[1] = ...
```

---

## Solution 1: [Name — e.g. Tabulation]

### The Analogy

<!-- Give a real-world analogy that makes the approach intuitive.
     Examples: receipt pad, scoreboard, treasure map, sticky note. -->

### Step 1: [First meaningful step]

<!-- Describe what you're doing and why. -->

```python
# code snippet
```

### Step 2: [Next step]

```python
# code snippet
```

<!-- Add as many steps as needed. Each step = one logical action. -->

### Tracing Through the Example

<!-- Show the array / grid being filled in, value by value.
     Make it visual. This is the most important part. -->

```
Input: ...

Step-by-step:
dp[0] = ...
dp[1] = ...
dp[2] = ...

Answer: dp[n] = ...
```

### Full Code

```python
def solution_name(self, ...) -> ...:
    # base cases
    ...

    # main loop
    for i in range(...):
        dp[i] = ...

    return ...
```

### Complexity

| Type | Value | Why |
|---|---|---|
| Time | O(?) | ... |
| Space | O(?) | ... |

---

## Solution 2: [Name — e.g. Space-Optimized]

<!-- If there's a better version, explain it here.
     Always explain *why* it's possible to optimize — what insight allows it? -->

### The Insight

<!-- Why can we do better? What did we notice about the previous solution? -->

### Code

```python
def solution_optimized(self, ...) -> ...:
    ...
```

### Tracing Through the Example

```
Input: ...

var1 = ..., var2 = ...
i=2: ...
i=3: ...
Answer: ...
```

### Complexity

| Type | Value | Why |
|---|---|---|
| Time | O(?) | ... |
| Space | O(?) | ... |

---

## Comparison of Solutions

| | Solution 1 | Solution 2 |
|---|---|---|
| Time | O(?) | O(?) |
| Space | O(?) | O(?) |
| Easier to understand? | Yes / No | Yes / No |
| Use when... | ... | ... |

---

## Test Cases

```python
sol = Solution()
print(sol.solution_name(...))    # Expected: ...
print(sol.solution_name(...))    # Expected: ...
```

---

<!-- Delete this comment block before submitting.
     Checklist:
     [ ] Plain-English problem statement
     [ ] Real-world analogy included
     [ ] Recurrence written out before code
     [ ] Base cases stated explicitly
     [ ] At least one traced example showing values
     [ ] All solution variants included
     [ ] Complexity table for each solution
     [ ] Working test cases with expected output
-->

# Contributing to Dynamic Programming Patterns

First off — thank you for taking the time to contribute. This guide exists to make DP approachable, and every improvement matters.

---

## Table of Contents

- [What You Can Contribute](#what-you-can-contribute)
- [Before You Start](#before-you-start)
- [Adding a New Problem](#adding-a-new-problem)
- [Adding a New Pattern](#adding-a-new-pattern)
- [Writing Style Guide](#writing-style-guide)
- [File Naming Conventions](#file-naming-conventions)
- [PR Checklist](#pr-checklist)

---

## What You Can Contribute

| Type | Examples |
|---|---|
| **New problem** | Add a problem to an existing pattern (e.g. Jump Game to Staircase) |
| **New pattern** | Knapsack, Interval DP, Tree DP, Matrix Chain, etc. |
| **Better explanation** | Improve an analogy, add a clearer trace, fix a confusing step |
| **Bug fix** | Incorrect code, wrong complexity analysis, broken link |
| **New solution variant** | Add a missing approach (e.g. recursive solution was missing) |

---

## Before You Start

1. **Check open issues and PRs** to avoid duplicating work.
2. **Open an issue first** if you're adding a new pattern — discuss the scope before writing.
3. For small fixes (typos, broken links), go ahead and open a PR directly.

---

## Adding a New Problem

### Step 1: Copy the template

Copy [`templates/PROBLEM_TEMPLATE.md`](templates/PROBLEM_TEMPLATE.md) and rename it to match your problem:

```
cp templates/PROBLEM_TEMPLATE.md dynamic_programming/staircase_pattern/jump_game.md
```

### Step 2: Fill in the template

Every problem explanation must include:

- [ ] Problem statement in plain English (no LeetCode jargon)
- [ ] A real-world analogy
- [ ] The key insight / recurrence written out before any code
- [ ] Base cases explicitly stated
- [ ] At least one traced example (show the array/grid being filled step by step)
- [ ] All solution variants (at minimum: tabulated + space-optimized)
- [ ] Complexity table for each solution
- [ ] Working test cases with expected output

### Step 3: Add the Python file

Create a matching `.py` file with the same name:

```
dynamic_programming/staircase_pattern/jump_game.py
```

Requirements for the Python file:
- Clean, readable code — no debug `print` statements in the final version
- Each solution as a method on a `Solution` class
- Test cases at the bottom using `print()` with expected output in comments
- Docstring on each method with Time and Space complexity

### Step 4: Update the pattern README

Add your problem to the table in the relevant pattern's `README.md`:

```markdown
| [Jump Game](jump_game.md) | `dp[i] = any(dp[j] and j + nums[j] >= i)` | Medium |
```

### Step 5: Update the top-level README

Add your problem to the [Problem Index](README.md#problem-index) table.

---

## Adding a New Pattern

Adding a new pattern is a bigger contribution. Please open an issue first.

A complete pattern submission includes:

1. A folder named `pattern_name/` (snake_case, ends in `_pattern`)
2. A `README.md` inside the folder following this structure:
   - What is this pattern? (1–2 paragraphs)
   - The mental model
   - The code template (skeleton showing the recurrence shape)
   - Space optimization technique for this pattern
   - Table of all problems in the pattern
   - When to use this pattern
   - Key things to remember
3. At least **2 problems** to start the pattern
4. An entry in the top-level `README.md` under the Patterns section

---

## Writing Style Guide

This guide is written so that **a beginner can understand it**. Please follow these principles:

### Be simple, not smart

- Avoid jargon without explanation
- If a term appears for the first time, define it
- Write like you're explaining to a friend, not documenting for a compiler

### Use analogies

Every problem should have at least one real-world analogy. Good analogies we've used:
- Sticker album (LCS)
- Robot on a city map (Unique Paths)
- Toll roads (Min Cost Climber)
- Sticky notepad (Memoization)

### Show the trace

Don't just say "fill the table" — show the actual values being filled in. A traced example is worth 10 paragraphs.

### Tell the story of optimization

Don't just show the best solution. Walk through why the naive approach fails, how memoization fixes it, and why the space-optimized version works. The journey is the lesson.

### Tone

- Direct and clear
- No filler words ("In this section, we will explore...")
- No condescending ("Obviously...", "Simply...")
- Short sentences over long ones

---

## File Naming Conventions

| Thing | Convention | Example |
|---|---|---|
| Problem markdown | `snake_case.md` | `house_robber.md` |
| Problem Python | `snake_case.py` | `house_robber.py` |
| Pattern folder | `snake_case_pattern/` | `knapsack_pattern/` |
| Pattern README | `README.md` (always) | `knapsack_pattern/README.md` |

---

## PR Checklist

Before submitting a pull request, confirm:

- [ ] My `.md` file follows the [problem template](templates/PROBLEM_TEMPLATE.md)
- [ ] The explanation includes a real-world analogy
- [ ] At least one traced example is shown
- [ ] All code is tested and outputs match the expected values in comments
- [ ] No debug `print` statements left in `.py` files
- [ ] Complexity (time + space) is stated for every solution
- [ ] The pattern `README.md` is updated with the new problem
- [ ] The top-level `README.md` Problem Index is updated
- [ ] File names follow the naming convention

---

## Questions?

Open an issue with the `question` label and we'll get back to you.

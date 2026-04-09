<div align="center">

# Dynamic Programming Patterns

**Stop memorizing solutions. Start recognizing patterns.**

A structured, beginner-friendly guide to Dynamic Programming — explained with analogies, traced examples, and every optimization step shown from brute force to O(1) space.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Problems](https://img.shields.io/badge/Problems-10-orange)](./)
[![Patterns](https://img.shields.io/badge/Patterns-3-blueviolet)](./)
[![Stars](https://img.shields.io/github/stars/RJ-Gamer/dsa?style=social)](https://github.com/RJ-Gamer/dsa)
[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub-ff69b4?logo=github&style=social)](https://github.com/sponsors/RJ-Gamer)

</div>

---

## Why This Exists

Most DP resources throw solutions at you. You memorize them, forget them, and panic in interviews.

This guide takes a different approach:

- Every problem is explained with a **real-world analogy** anyone can understand
- Every solution shows the **full journey**: naive recursion → memoization → tabulation → space optimization
- Problems are grouped by **pattern**, not by difficulty — because once you see the pattern, every problem in that family becomes easy

> If you can explain it to a 5-year-old, you actually understand it.

---

## Table of Contents

- [How to Use This Guide](#how-to-use-this-guide)
- [The DP Mindset](#the-dp-mindset)
- [Patterns](#patterns)
  - [Staircase Pattern](#-staircase-pattern)
  - [Grid Pattern](#-grid-pattern)
  - [Interval Pattern](#-interval-pattern)
- [Problem Index](#problem-index)
- [The Optimization Journey](#the-optimization-journey)
- [How to Approach Any DP Problem](#how-to-approach-any-dp-problem)
- [Complexity Cheat Sheet](#complexity-cheat-sheet)
- [Contributing](#contributing)
- [License](#license)

---

## How to Use This Guide

**If you're new to DP:**
1. Read [The DP Mindset](#the-dp-mindset) below
2. Start with the [Staircase Pattern](dynamic_programming/staircase_pattern/README.md) — it's the simplest
3. Work through problems in order within each pattern
4. Read every solution variant, not just the optimal one — the journey matters

**If you're preparing for interviews:**
1. Go to the [Problem Index](#problem-index) and pick a pattern
2. Try solving the problem yourself first
3. Then read the explanation to fill gaps
4. Compare your approach to all solution variants

**If you're reviewing a specific problem:**
- Jump directly from the [Problem Index](#problem-index)

---

## The DP Mindset

Dynamic Programming solves hard problems by answering this question:

> "Can I break this into smaller problems, and have I already solved any of them before?"

Two things must be true for DP to work:

| Property | What it means | Example |
|---|---|---|
| **Overlapping Subproblems** | The same smaller problem appears multiple times | `F(10)` needs `F(8)` — so does `F(9)` |
| **Optimal Substructure** | The best answer to a big problem is built from best answers to sub-problems | Cheapest path A→C = cheapest A→B + cheapest B→C |

If both are true → DP will work.

---

## Patterns

### 🪜 Staircase Pattern

**The idea:** Move through a sequence one step at a time. Each cell's answer depends on a small, fixed number of previous cells (usually 2–3).

```
dp[i] = f(dp[i-1], dp[i-2])
```

The pattern shows up whenever you're moving linearly through an array and making a local decision at each step.

| Problem | Core Recurrence | Difficulty |
|---|---|---|
| [Climb Stairs](dynamic_programming/staircase_pattern/climb_stairs.md) | `dp[i] = dp[i-1] + dp[i-2]` | Easy |
| [Tribonacci](dynamic_programming/staircase_pattern/tribonacci.md) | `dp[i] = dp[i-1] + dp[i-2] + dp[i-3]` | Easy |
| [Min Cost Climbing Stairs](dynamic_programming/staircase_pattern/min_cost_climber.md) | `dp[i] = cost[i] + min(dp[i-1], dp[i-2])` | Easy |
| [House Robber](dynamic_programming/staircase_pattern/robber.md) | `dp[i] = max(dp[i-1], dp[i-2] + nums[i])` | Medium |

[Explore the Staircase Pattern →](dynamic_programming/staircase_pattern/README.md)

---

### 🗺️ Grid Pattern

**The idea:** Fill a 2D table. Each cell's answer depends on the cell directly above it and the cell to its left.

```
grid[i][j] = f(grid[i-1][j], grid[i][j-1])
```

The pattern shows up in path counting, string comparison, and any problem where you compare two sequences.

| Problem | Core Recurrence | Difficulty |
|---|---|---|
| [Unique Paths](dynamic_programming/grid_pattern/unique_paths.md) | `grid[i][j] = above + left` | Easy |
| [Unique Paths with Obstacles](dynamic_programming/grid_pattern/unique_paths_obstacles.md) | Same, but blocked cells = 0 | Easy |
| [Longest Common Subsequence](dynamic_programming/grid_pattern/longest_common_subsequence.md) | Match → diagonal+1, else max(above, left) | Medium |
| [Edit Distance](dynamic_programming/grid_pattern/min_distance.md) | Match → diagonal, else 1+min(diagonal, above, left) | Medium |

[Explore the Grid Pattern →](dynamic_programming/grid_pattern/README.md)

---

### 🔁 Interval Pattern

**The idea:** Solve a problem on a single string by expanding from smaller substrings to larger ones. Each cell `dp[i][j]` is the answer for the substring `s[i..j]`.

```
dp[i][j] = f(dp[i+1][j-1], dp[i+1][j], dp[i][j-1])
```

The pattern shows up whenever a problem involves symmetry, ranges that shrink from both ends, or combining answers from subintervals.

| Problem | Core Recurrence | Difficulty |
|---|---|---|
| [Longest Palindromic Subsequence](dynamic_programming/interval_dynamic_programming/longest_palindrome_subsequence.md) | Match → inner+2, else max(skip-left, skip-right) | Medium |
| [Palindromic Substrings](dynamic_programming/interval_dynamic_programming/palindromic_substrings.md) | `dp[i][j] = word[i]==word[j] and dp[i+1][j-1]` | Medium |

[Explore the Interval Pattern →](dynamic_programming/interval_dynamic_programming/README.md)

---

## Problem Index

| # | Problem | Pattern | Solutions | Code |
|---|---|---|---|---|
| 1 | [Climb Stairs](dynamic_programming/staircase_pattern/climb_stairs.md) | Staircase | Recursive, Memoized, Tabulated, Optimized | [.py](dynamic_programming/staircase_pattern/climb_stairs.py) |
| 2 | [Tribonacci](dynamic_programming/staircase_pattern/tribonacci.md) | Staircase | Space-Optimized | [.py](dynamic_programming/staircase_pattern/tribonacci.py) |
| 3 | [Min Cost Climbing Stairs](dynamic_programming/staircase_pattern/min_cost_climber.md) | Staircase | Tabulated, Space-Optimized | [.py](dynamic_programming/staircase_pattern/min_cost_climber.py) |
| 4 | [House Robber](dynamic_programming/staircase_pattern/robber.md) | Staircase | Tabulated, Space-Optimized | [.py](dynamic_programming/staircase_pattern/robber.py) |
| 5 | [Unique Paths](dynamic_programming/grid_pattern/unique_paths.md) | Grid | Full Grid, Single Row | [.py](dynamic_programming/grid_pattern/unique_paths.py) |
| 6 | [Unique Paths with Obstacles](dynamic_programming/grid_pattern/unique_paths_obstacles.md) | Grid | Single Array | [.py](dynamic_programming/grid_pattern/unique_paths_obstacles.py) |
| 7 | [Longest Common Subsequence](dynamic_programming/grid_pattern/longest_common_subsequence.md) | Grid | Full Grid, Space-Optimized | [.py](dynamic_programming/grid_pattern/longest_common_subsequence.py) |
| 8 | [Edit Distance](dynamic_programming/grid_pattern/min_distance.md) | Grid | Full Grid | [.py](dynamic_programming/grid_pattern/min_distance.py) |
| 9 | [Longest Palindromic Subsequence](dynamic_programming/interval_dynamic_programming/longest_palindrome_subsequence.md) | Interval | Full Grid, Space-Optimized | [.py](dynamic_programming/interval_dynamic_programming/longest_palindrome_subsequence.py) |
| 10 | [Palindromic Substrings](dynamic_programming/interval_dynamic_programming/palindromic_substrings.md) | Interval | Memoized Recursion, Interval DP, Expand Around Center | [.py](dynamic_programming/interval_dynamic_programming/palindromic_substrings.py) |

---

## The Optimization Journey

Every problem in this guide walks through the same four steps. Understanding each step — not just the final answer — is what makes DP click.

```
Step 1: Recursion
        "I'll recompute everything from scratch."
        ✓ Correct   ✗ Exponentially slow (O(2^n))

        ↓

Step 2: Memoization  (Top-Down DP)
        "I'll cache results as I recurse."
        ✓ Fast   ✗ Still uses recursion stack

        ↓

Step 3: Tabulation  (Bottom-Up DP)
        "I'll build the answer from the ground up."
        ✓ Fast   ✓ No recursion   ✗ O(n) space

        ↓

Step 4: Space Optimization
        "I only need the last few values."
        ✓ Fast   ✓ O(1) space   ← The gold standard
```

Not every problem needs all four steps — but every problem *can* be explained through this lens.

---

## How to Approach Any DP Problem

Use this checklist every time you see a DP problem:

**1. Define `dp[i]` in plain English**
> Write the sentence: "`dp[i]` = the max/min/count of ... considering only the first `i` elements."
> If you can't write this sentence, you're not ready to code.

**2. Write the recurrence**
> How does `dp[i]` relate to `dp[i-1]`, `dp[i-2]`, etc.? Work through 2–3 small examples by hand.

**3. Write the base cases**
> What are `dp[0]`, `dp[1]`? What happens with an empty input?

**4. Decide traversal order**
> 1D → left to right. 2D → top-left to bottom-right.

**5. Code tabulation first**
> Get the full array version working and tested before optimizing.

**6. Optimize space**
> Does `dp[i]` only look back a fixed number of steps? If yes, replace the array with variables.

---

## Complexity Cheat Sheet

| Approach | Time | Space | When to use |
|---|---|---|---|
| Recursion (no cache) | O(2ⁿ) | O(n) stack | Never in production |
| Memoization | O(n) | O(n) | When recursion is clearest |
| Tabulation | O(n) | O(n) | Default starting point |
| Space-Optimized | O(n) | **O(1)** | When space matters |
| 2D Tabulation | O(m×n) | O(m×n) | Grid / two-sequence problems |
| 2D Space-Optimized | O(m×n) | **O(n)** | Grid problems, space matters |

---

## Repo Structure

```
.
├── README.md                          ← You are here
├── CONTRIBUTING.md                    ← How to add problems or patterns
├── CHANGELOG.md                       ← Version history
├── CREATING_A_SKILL.md                ← Guide to creating custom Claude skills
├── LICENSE                            ← MIT
├── .gitignore
├── templates/
│   └── PROBLEM_TEMPLATE.md            ← Scaffold for new problems
└── dynamic_programming/
    ├── staircase_pattern/
    │   ├── README.md                  ← Pattern overview + when to use
    │   ├── climb_stairs.md / .py
    │   ├── min_cost_climber.md / .py
    │   ├── robber.md / .py
    │   └── tribonacci.md / .py
    ├── grid_pattern/
    │   ├── README.md                  ← Pattern overview + when to use
    │   ├── unique_paths.md / .py
    │   ├── unique_paths_obstacles.md / .py
    │   ├── longest_common_subsequence.md / .py
    │   └── min_distance.md / .py
    └── interval_dynamic_programming/
        ├── README.md                  ← Pattern overview + when to use
        ├── longest_palindrome_subsequence.md / .py
        └── palindromic_substrings.md / .py
```

Each problem has two files:
- `.md` — the full explanation with analogy, step-by-step walkthrough, traced examples, and all solution variants
- `.py` — clean, runnable Python code with test cases

---

## Contributing

Want to add a problem, fix an explanation, or introduce a new pattern?

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines, naming conventions, and the problem template.

All contributions are welcome — especially:
- New problems within existing patterns
- New DP patterns (Knapsack, Interval, Tree DP, etc.)
- Improved analogies or clearer explanations

---

## License

[MIT](LICENSE) — free to use, share, and build on.

---

## Inspiration

This repo was inspired by [NeetCode's Dynamic Programming playlist](https://www.youtube.com/watch?v=66hDgWottdA&t=3472s). If you want a video walkthrough alongside these written explanations, that playlist is the best companion resource.

---

<div align="center">

If this helped you, consider giving it a star — it helps others find it.

</div>

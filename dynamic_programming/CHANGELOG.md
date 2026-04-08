# Changelog

All notable changes to this project will be documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- `longest_common_subsequence` — space-optimized O(n) solution using two-row (`prev`/`curr`) technique

---

## [1.0.0] — 2026-04-08

### Added

**Staircase Pattern**
- `climb_stairs` — 4 solutions: recursive, memoized, tabulated, space-optimized
- `tribonacci` — space-optimized O(1) solution
- `min_cost_climber` — tabulated and space-optimized solutions
- `robber` (House Robber) — tabulated and space-optimized solutions
- `staircase_pattern/README.md` — pattern overview, recurrence template, when-to-use guide

**Grid Pattern**
- `unique_paths` — 2 solutions: full grid (O(m×n) space) and single-row (O(n) space)
- `unique_paths_obstacles` — single-array space-optimized solution
- `longest_common_subsequence` — DP grid solution with full traced example
- `grid_pattern/README.md` — pattern overview, grid template, space optimization technique

**Repo structure**
- `README.md` — main landing page with badges, pattern map, problem index, optimization journey
- `CONTRIBUTING.md` — contribution guide with PR checklist, writing style guide, naming conventions
- `CHANGELOG.md` — this file
- `LICENSE` — MIT
- `.gitignore` — Python standard
- `templates/PROBLEM_TEMPLATE.md` — scaffold for new problem explanations

---

## Version History Summary

| Version | Date | Highlights |
|---|---|---|
| 1.0.0 | 2026-04-08 | Initial release — 7 problems across 2 patterns |

---

[Unreleased]: https://github.com/YOUR-USERNAME/YOUR-REPO/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/YOUR-USERNAME/YOUR-REPO/releases/tag/v1.0.0

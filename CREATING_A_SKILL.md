# How to Create a Custom Skill in Claude Code

A complete, step-by-step guide — from zero to a working `/slash-command`.

---

## What Is a Skill?

A skill is a reusable instruction set for Claude. Once created, you invoke it with a `/slash-command` and Claude follows the instructions inside it — reading files, writing code, running commands, whatever you tell it to do.

Think of it like writing a recipe card for Claude:
- The **recipe name** = your `/command`
- The **ingredients** = the context and arguments you pass
- The **instructions** = the Markdown body of your skill file

Skills follow the open [Agent Skills standard](https://agentskills.io) and are just Markdown files with a YAML header.

---

## Two Levels of Skills

| Level | Location | Who can use it |
|---|---|---|
| **User (personal)** | `~/.claude/skills/<skill-name>/SKILL.md` | You, across all projects |
| **Project** | `.claude/skills/<skill-name>/SKILL.md` | Everyone on the project |

Start with a **user skill** while building. Promote it to a project skill when the team needs it.

---

## Step 1: Pick a Location and Create the Folder

Every skill lives in its own folder. The folder name becomes the slash command.

**For a personal skill** (available in all your projects):
```bash
mkdir -p ~/.claude/skills/dp-guide
```

**For a project skill** (lives inside your repo, committed to git):
```bash
mkdir -p .claude/skills/dp-guide
```

> The folder name `dp-guide` will become the command `/dp-guide`.

---

## Step 2: Create `SKILL.md`

The file **must** be named exactly `SKILL.md` (uppercase). This is the only required file.

```bash
touch ~/.claude/skills/dp-guide/SKILL.md
```

Open it and add content. The structure is always:

```
---
YAML frontmatter (metadata)
---

Markdown body (instructions for Claude)
```

---

## Step 3: Write the Frontmatter

The frontmatter is a YAML block between `---` markers at the top of the file. It tells Claude when and how to use the skill.

### The Full Frontmatter Reference

```yaml
---
# The command name. Lowercase, hyphens only. Max 64 chars.
# Becomes /slash-command. Defaults to folder name if omitted.
name: dp-guide

# What this skill does. Claude reads this to decide when to use it automatically.
# Keep it under 250 chars. Front-load the key use case.
description: Explains dynamic programming patterns with analogies, visual traces, and step-by-step code breakdowns. Use when teaching DP or explaining a DP problem.

# Hint shown in autocomplete when user types /dp-guide
argument-hint: [problem-name or pattern]

# Set true to prevent Claude from using this automatically.
# Good for workflows with side effects (deploy, send email, etc.)
disable-model-invocation: false

# Set false to hide from the / menu. Only Claude can invoke it.
# Useful for background-knowledge skills users shouldn't call directly.
user-invocable: true

# Tools Claude can use without asking permission when this skill is active.
# Options: Read, Write, Edit, Bash, Grep, Glob, WebFetch, WebSearch, etc.
allowed-tools: Read Grep Glob

# Which model to use when this skill runs (optional override).
# model: claude-opus-4-6

# Effort level: low, medium, high, max (Opus 4.6 only)
# effort: medium

# Run in isolated subagent context.
# context: fork

# Which subagent to use with context: fork
# agent: Explore
---
```

> You don't need all of these. A minimal skill only needs `name` and `description`.

### Minimal Working Frontmatter

```yaml
---
name: dp-guide
description: Explains a dynamic programming problem with analogies, step-by-step traces, and complexity breakdowns.
argument-hint: [problem-name]
allowed-tools: Read Grep
---
```

---

## Step 4: Write the Instructions (The Skill Body)

The body is plain Markdown. Claude reads and follows it as instructions. Write it like you're briefing a smart colleague.

### Rules for Good Skill Bodies

1. **Be specific** — vague instructions produce vague results
2. **Use numbered steps** for sequential workflows
3. **Specify the output format** — tables, code blocks, analogies, etc.
4. **Use `$ARGUMENTS`** to reference what the user passed in

### Using Arguments

When a user types `/dp-guide staircase`, the word `staircase` is the argument.

| Placeholder | What it contains |
|---|---|
| `$ARGUMENTS` | Everything after the command, as one string |
| `$ARGUMENTS[0]` | First argument |
| `$ARGUMENTS[1]` | Second argument |
| `$1`, `$2` | Shorthand for `$ARGUMENTS[0]`, `$ARGUMENTS[1]` |

**Example:**
```
/dp-guide staircase
```
In the skill body, `$ARGUMENTS` = `staircase`, `$ARGUMENTS[0]` = `staircase`.

### Dynamic Shell Injection

Use `` !`command` `` to inject live terminal output into your skill **before** Claude sees it. The command runs at invocation time.

```yaml
---
name: pr-review
description: Review the current pull request
allowed-tools: Bash
---

## Current PR
!`gh pr view`

## Changed files
!`gh pr diff --name-only`

Review the PR above. Look for bugs, security issues, and style violations.
```

When you run `/pr-review`, the shell commands run first and their output is inserted inline — then Claude sees the fully assembled prompt.

---

## Step 5: A Complete Real Example

Here's a full skill that turns this DP guide repo into a `/dp-guide` command:

**`~/.claude/skills/dp-guide/SKILL.md`**

```yaml
---
name: dp-guide
description: Explains a dynamic programming problem or pattern using plain-English analogies, step-by-step traces, and complexity analysis. Use when teaching DP or walking through a DP solution.
argument-hint: [problem-name or pattern-name]
allowed-tools: Read Grep Glob
---

You are explaining a dynamic programming concept to someone who is smart but new to DP.
Your job is to explain: **$ARGUMENTS**

Follow this structure exactly:

## 1. The Problem
Restate the problem in one sentence. Then explain it using a real-world analogy (toys, houses, stairs, etc.).

## 2. The Key Insight
What is the one idea that unlocks the solution? State the recurrence relation in plain English first, then as a formula.

## 3. Step-by-Step Walkthrough
Walk through the solution line by line. For every non-obvious line of code, add a comment explaining *why* it's there (not just what it does).

## 4. Visual Trace
Pick a small example. Manually trace through it, showing the state of the dp array / grid at each step.

## 5. All Solutions (if multiple exist)
Show each solution from naive to optimized. For each one:
- Explain the key idea
- Show the code
- State time and space complexity

## 6. The Optimization Journey
Summarize the evolution:
Recursion → Memoization → Tabulation → Space Optimization

## 7. Test Cases
Show 2–3 inputs with expected outputs.

Use simple language throughout. If a 10-year-old couldn't follow it, simplify further.
```

**Invoke it:**
```
/dp-guide house robber
/dp-guide longest common subsequence
/dp-guide staircase pattern
```

---

## Step 6: Test Your Skill

1. Open Claude Code in any project
2. Type `/` — your skill should appear in the autocomplete list
3. Invoke it:
   ```
   /dp-guide climbing stairs
   ```
4. Claude will follow your SKILL.md instructions

**If the skill doesn't appear:**
- Check the folder is named correctly and `SKILL.md` is inside it
- Verify the path: `~/.claude/skills/dp-guide/SKILL.md`
- Restart Claude Code (skills are loaded at session start)

---

## Step 7: Advanced Patterns

### Run in an Isolated Subagent (Fork Mode)

When your skill does heavy research, run it in a forked subagent so it doesn't pollute your main conversation context:

```yaml
---
name: deep-dive
description: Deep research on a DP pattern or algorithm
context: fork
agent: Explore
allowed-tools: Read Grep Glob
---

Research everything about $ARGUMENTS in the codebase.
Return a summary with file references and code snippets.
```

The `Explore` agent is optimized for reading and searching. It completes its task and returns a single summary.

### Disable Automatic Invocation

For skills that have side effects (deploy, commit, send a message), you don't want Claude triggering them automatically:

```yaml
---
name: publish-guide
description: Publishes the DP guide to GitHub Pages
disable-model-invocation: true
---

1. Run `git add .`
2. Commit with message: "docs: update DP guide"
3. Push to origin main
4. Confirm deployment succeeded
```

With `disable-model-invocation: true`, this skill **only** runs when you explicitly type `/publish-guide`.

### Restrict Available Tools

Limit what Claude can do while a skill is active:

```yaml
---
name: read-only-explainer
description: Explains code without making any changes
allowed-tools: Read Grep Glob
---

Explain how $ARGUMENTS works. Read the relevant files.
Do not edit, write, or run any commands.
```

---

## Folder Structure Reference

```
~/.claude/
└── skills/
    └── dp-guide/
        ├── SKILL.md          ← Required. The skill definition.
        ├── examples/
        │   └── output.md     ← Optional. Show Claude what good output looks like.
        └── templates/
            └── problem.md    ← Optional. Templates Claude can reference.
```

For a **project skill** (lives in your repo):
```
your-project/
└── .claude/
    └── skills/
        └── dp-guide/
            └── SKILL.md
```

---

## Sharing Your Skill

To share a project skill with your team:
1. Put it in `.claude/skills/` inside your repo
2. Commit it to git — everyone who clones the repo gets the skill automatically

To share a personal skill:
1. Export your `~/.claude/skills/<skill-name>/` folder
2. Others drop it in their own `~/.claude/skills/`

---

## Quick Cheat Sheet

```
# Create a personal skill
mkdir -p ~/.claude/skills/my-skill && touch ~/.claude/skills/my-skill/SKILL.md

# Create a project skill
mkdir -p .claude/skills/my-skill && touch .claude/skills/my-skill/SKILL.md

# Invoke
/my-skill
/my-skill some argument here

# Access arguments inside SKILL.md
$ARGUMENTS       → all arguments as a string
$ARGUMENTS[0]    → first argument
$1               → shorthand for first argument

# Run shell command at invocation time (output injected inline)
!`git status`

# Disable auto-invocation (side-effect workflows)
disable-model-invocation: true

# Run in isolated subagent
context: fork
agent: Explore
```

---

## Frontmatter Quick Reference

| Field | Type | What it does |
|---|---|---|
| `name` | string | The `/command-name`. Defaults to folder name. |
| `description` | string | When Claude uses it automatically. Keep under 250 chars. |
| `argument-hint` | string | Autocomplete hint, e.g. `[issue-number]` |
| `allowed-tools` | string | Tools usable without permission prompts |
| `disable-model-invocation` | bool | Only run when explicitly invoked |
| `user-invocable` | bool | Show in `/` menu (default: true) |
| `context` | string | `fork` = run in isolated subagent |
| `agent` | string | Which agent for `context: fork` |
| `model` | string | Model override for this skill |
| `effort` | string | `low` / `medium` / `high` / `max` |
| `paths` | string | Glob pattern — only activate for matching files |
| `shell` | string | `bash` (default) or `powershell` |

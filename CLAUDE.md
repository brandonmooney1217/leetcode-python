# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Critical Rules

- **DO NOT implement solutions** — Brandon solves problems himself
- **ONLY provide problem description and empty function stub** when adding a new problem
- **Do NOT create test files** — solutions are validated directly on LeetCode

## Adding a New Problem

Create only `topic/problem_name.py` with this format:

```python
# LeetCode #XXX (Easy/Medium/Hard): https://leetcode.com/problems/problem-name/
from typing import List  # only if needed

class Solution:
    def solution_function(self, ...) -> ...:
        pass
```

## Syntax Verification

```bash
python3 -m py_compile topic/file.py
```

## Type Hints

- Use `from typing import List, Optional, Dict` etc. when using generic type annotations
- Python 3.9+ lowercase generics (`list[int]`) also work without imports

## Repository Layout

Solutions organized by LeetCode topic category: `arrays/`, `dynamic_programming/`, `trees/`, `graphs/`, etc. Each file is a standalone solution — no shared utilities or cross-file dependencies.

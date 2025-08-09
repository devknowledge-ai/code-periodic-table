# Getting Started: Help Build the Anvil Suite

*Join us in creating developer tools that solve real problems*

## Current Project Status

**Important: The Anvil Suite is in pre-development.** No working tools exist yet. We're looking for contributors to help write the very first lines of functional code.

See [PROJECT_STATUS.md](./PROJECT_STATUS.md) for complete transparency about what exists (very little) vs. what's planned (everything else).

## Where to Start

We have two parallel tracks that need initial implementation:

### Track 1: Anvil Context - Sticky Comments Component
**Goal**: Comments that stay attached to code through refactoring

**First tasks**:
1. Extract comments from Python files
2. Create basic AST fingerprints for code blocks
3. Track a comment through one simple refactoring

**Start here**: [projects/anvil-context/](./projects/anvil-context/)

### Track 2: Null Guard - Basic Pattern Detection
**Goal**: Detect obvious null/None reference bugs

**First tasks**:
1. Detect unchecked function returns that could be None
2. Find dictionary access without .get()
3. Identify chain access patterns (a.b.c where any could be None)

**Start here**: [projects/null-guard/PROTOTYPE.md](./projects/null-guard/PROTOTYPE.md)

## Setting Up Your Development Environment

```bash
# Clone the repository
git clone https://github.com/anvil-suite/code-periodic-table.git
cd code-periodic-table

# Set up Python environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install pytest black mypy
```

## Your First Contribution

Since we're starting from scratch, here are concrete first PRs we need:

### For Anvil Context (Sticky Comments)

**PR #1: Comment Extraction**
```python
# Create: projects/anvil-context/src/comment_extractor.py

import ast
from typing import List, Dict

def extract_comments(file_path: str) -> List[Dict]:
    """Extract all comments from a Python file with their line numbers."""
    # TODO: Implement comment extraction
    # Should return: [{"line": 10, "text": "# TODO: fix this", "type": "inline"}]
    pass
```

**PR #2: Basic Fingerprinting**
```python
# Create: projects/anvil-context/src/fingerprint.py

def create_fingerprint(code_block: str) -> str:
    """Create a simple fingerprint for a code block."""
    # TODO: Start with something basic like hash of normalized AST
    pass
```

### For Null Guard

**PR #1: Basic Pattern Detector**
```python
# Create: projects/null-guard/src/detector.py

import ast
from typing import List

def find_unchecked_returns(code: str) -> List[dict]:
    """Find function returns used without None checks."""
    # TODO: Parse AST, find patterns like:
    # user = get_user()
    # user.name  # <- potential bug
    pass
```

**PR #2: Test Cases**
```python
# Create: projects/null-guard/tests/test_patterns.py

def test_unchecked_return():
    code = """
    user = get_user(123)
    print(user.name)  # Should detect this
    """
    bugs = find_unchecked_returns(code)
    assert len(bugs) == 1
    assert bugs[0]['line'] == 2
```

## No Working Prototypes Yet

The following do NOT work yet (despite what other docs might suggest):

- ❌ `pip install nullguard` - package doesn't exist
- ❌ `nullguard check file.py` - no CLI exists
- ❌ `python prototype.py` - the git-memory prototype only does basic commit message analysis
- ❌ Web demos - no web interface exists
- ❌ IDE extensions - not built yet

## What Actually Exists

### Minimal Starting Points:
- `anvil-core/src/` - Basic structure, needs implementation
- `projects/git-memory/prototype.py` - Simple commit message analyzer (very basic)
- Documentation and plans (what you're reading)

### What Needs to Be Built:
- Everything else

## How to Contribute Right Now

1. **Pick a track** (Anvil Context or Null Guard)
2. **Choose a first task** from above
3. **Create an issue** describing what you'll implement
4. **Write the code** - even 20 lines is progress!
5. **Submit a PR** - we'll help you refine it

### Good First Issues

Look for issues labeled:
- `good-first-issue` - Beginner friendly
- `help-wanted` - We need help here
- `ground-floor` - Foundational code needed

## Getting Help

**Questions?** Open an issue with the `question` label
**Stuck?** Comment on your PR - we'll help
**Ideas?** Start a discussion in GitHub Discussions

## The Honest Truth

We're at the very beginning. The code you write will be foundational. You're not contributing to an existing project - you're helping create it from scratch.

This is an opportunity to:
- Shape the architecture from the ground up
- Get your code into the core of the project
- Be recognized as a founding contributor

## Next Steps

1. Read [PROJECT_STATUS.md](./PROJECT_STATUS.md) to understand what's real vs planned
2. Check [CURRENT_ROADMAP.md](./CURRENT_ROADMAP.md) for the development plan
3. Pick a small task and start coding
4. Submit even small PRs - every line of code moves us forward

---

*Ready to build something real? Let's start with just a few lines of code.*
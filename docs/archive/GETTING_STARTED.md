# [ARCHIVED] Getting Started with Anvil - FICTIONAL GUIDE

# ⚠️⚠️⚠️ CRITICAL WARNING ⚠️⚠️⚠️

## THIS ENTIRE GUIDE IS FICTIONAL

**THE FOLLOWING COMMANDS AND TOOLS DO NOT EXIST:**
- ❌ The prototype script `detect_repeated_fixes.py` DOES NOT EXIST
- ❌ The repository path shown IS NOT REAL
- ❌ The installation steps WILL NOT WORK
- ❌ The sample outputs are FICTIONAL EXAMPLES

**This document is preserved from before [The Great Simplification](../../THE_GREAT_SIMPLIFICATION.md) as a historical artifact showing our original (abandoned) approach.**

**For actual project status, see [PROJECT_STATUS.md](../../PROJECT_STATUS.md)**

---

*Original fictional content follows below...*

Welcome! This guide would have taken you from zero to your first contribution in about 10 minutes (if any of this existed).

## 1-Minute Understanding

**Anvil prevents your team from fixing the same bug twice.**

It watches your Git history, learns what went wrong before, and warns you when you're about to repeat a mistake. Think of it as institutional memory for your codebase.

## 5-Minute Setup

### Prerequisites
- Python 3.8+
- Git
- A repository with at least 6 months of history

### Quick Start

```bash
# Clone the repository
git clone https://github.com/devknowledge-ai/anvil
cd anvil

# Install dependencies
pip install -r requirements.txt

# Try the demo prototype (very basic proof-of-concept)
python prototype/detect_repeated_fixes.py /path/to/your/repo

# Note: This is a simple demo that only analyzes commit messages,
# not actual code patterns. It demonstrates the concept only.
```

### What You'll See

```
Analyzing repository: /path/to/your/repo
Found 1,234 commits, 89 bug fixes

PATTERN DETECTED: Null Reference on Optional Fields
- Fixed 4 times in the last year
- Pattern: Accessing user['field'] without checking existence
- Files affected: auth.py, payment.py, profile.py
- Suggestion: Add .get('field') or existence check

PATTERN DETECTED: Race Condition in Async Updates
- Fixed 3 times in the last 6 months
- Pattern: Concurrent updates without locking
- Files affected: cache.py, session.py
- Suggestion: Add mutex or use atomic operations

Summary: 7 repeated patterns found
Potential bugs prevented: 12-15 per year
```

## Your First Contribution

Choose based on your skills and interests:

### Option A: Improve Pattern Detection (Python)
**Task**: Add detection for resource leak patterns  
**Difficulty**: Medium  
**Mentor**: @adrian  

```python
# In anvil/patterns/resource_patterns.py
def detect_unclosed_resources(diff):
    """
    Detect when files/connections are opened but not closed
    Example: open() without close() or with statement
    """
    # Your code here
```

[Claim this task →](https://github.com/devknowledge-ai/anvil/issues/1)

### Option B: Create VS Code Warning UI (TypeScript)
**Task**: Design the warning popup when a pattern is detected  
**Difficulty**: Easy  
**Mentor**: @sarah  

Create a mockup for how warnings appear in VS Code:
- Non-intrusive but noticeable
- Shows pattern description and previous fix
- Has "Ignore" and "Learn More" buttons

[Claim this task →](https://github.com/devknowledge-ai/anvil/issues/2)

### Option C: Optimize Git Analysis (Any language)
**Task**: Speed up repository scanning  
**Difficulty**: Hard  
**Mentor**: @mike  

Current performance: 1000 commits/second  
Goal: 5000 commits/second  

[Claim this task →](https://github.com/devknowledge-ai/anvil/issues/3)

## Project Structure (What Matters Now)

```
anvil/
├── prototype/           # Demo concept code (not production)
│   ├── detect_repeated_fixes.py    # Simple demo script
│   └── patterns/        # Placeholder for future modules
├── tests/              # Test suite
├── mockups/            # UI/UX designs
└── docs/               # Documentation
```

Ignore everything else for now. The `/vision` and `/research` directories are for future phases.

## Development Workflow

1. **Pick an issue** labeled `good-first-issue`
2. **Comment** "I'll take this" on the issue
3. **Fork and clone** the repository
4. **Create a branch**: `git checkout -b feature/your-feature`
5. **Make changes** and write tests
6. **Push and PR** with clear description
7. **Get reviewed** - we'll help you succeed

## Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_pattern_detection.py

# Run with coverage
pytest --cov=anvil
```

## Getting Help

### Quick Questions
- Discord: [#help channel](https://discord.gg/anvil)
- GitHub: Comment on your issue

### Detailed Discussion
- Weekly office hours: Thursdays 3pm UTC
- Pair programming: Book time with a mentor

### Stuck?
Email adrian.belmans@gmail.com with subject "Anvil: Stuck on [issue]"

## Success Metrics

Your contribution succeeds when:
- ✅ Tests pass
- ✅ Code is readable
- ✅ Solves the stated problem
- ✅ Doesn't over-engineer

We optimize for clarity over cleverness.

## Real Example: Your First Pattern Detection

Here's a complete example of adding a new pattern detection:

```python
# anvil/patterns/security_patterns.py

def detect_hardcoded_secrets(diff):
    """
    Detect when secrets are hardcoded instead of using env variables
    """
    patterns = []
    
    # Look for common secret patterns
    secret_keywords = ['password', 'api_key', 'secret', 'token']
    
    for line in diff.added_lines:
        for keyword in secret_keywords:
            if keyword in line.lower() and '=' in line:
                # Check if it's a hardcoded string
                if '"' in line or "'" in line:
                    patterns.append({
                        'type': 'hardcoded_secret',
                        'line': line,
                        'suggestion': f'Use environment variable for {keyword}'
                    })
    
    return patterns
```

## Next Steps

1. **Join Discord** for real-time help
2. **Star the repo** to show support
3. **Pick an issue** and start coding
4. **Share feedback** on this guide

## FAQ

**Q: Do I need to understand the whole project?**  
A: No. Focus on your specific task. The architecture is modular.

**Q: What if I break something?**  
A: That's what tests and code review are for. We'll help fix it.

**Q: Can I propose new features?**  
A: Yes! Open an issue with your idea. We love fresh perspectives.

**Q: How long should my first contribution take?**  
A: Aim for something you can complete in 2-4 hours.

---

## The One Thing to Remember

**We want you to succeed.** This isn't a test. We'll provide mentorship, pair programming, and whatever help you need to make your first contribution.

Ready? [Pick your first issue →](https://github.com/devknowledge-ai/anvil/issues?q=is%3Aissue+is%3Aopen+label%3Agood-first-issue)

---

*P.S. - Still curious about the bigger vision? Check out [The Story Behind Anvil](./vision/). But honestly, just building the tool is contribution enough.*
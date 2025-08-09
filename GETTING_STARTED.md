# Getting Started: Build NullGuard in 30 Minutes

*Your first contribution to the Anvil Suite - our showcase demo*

## Why Start with NullGuard?

NullGuard is:
- **Simple to understand**: Everyone knows null bugs
- **Quick to test**: See results immediately  
- **High impact**: 70% of bugs with simple patterns
- **Our demo**: The showcase for the entire suite

## Quick Setup (5 minutes)

```bash
# Clone the repository
git clone https://github.com/anvil-suite/code-periodic-table.git
cd code-periodic-table

# Set up Python environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install NullGuard
cd projects/null-guard
pip install -e .

# Run tests to verify setup
pytest tests/
```

## Your First Contribution (25 minutes)

### Option 1: Add a Null Pattern (Easiest)
Find a null bug pattern and add it to our library:

```python
# Edit: projects/null-guard/src/patterns.py

# Add your pattern
MY_PATTERN = {
    "name": "empty_list_access",
    "description": "Accessing index on potentially empty list",
    "example": "items = get_items()\nfirst = items[0]  # Could be empty!",
    "fix": "items = get_items()\nif items:\n    first = items[0]",
    "confidence": 0.80
}

# Add to PATTERNS list
PATTERNS.append(MY_PATTERN)
```

Test your pattern:
```bash
pytest tests/test_patterns.py::test_my_pattern
```

### Option 2: Improve Detection (Medium)
Enhance the detection algorithm:

```python
# Edit: projects/null-guard/src/detector.py

def detect_your_bug_type(self, tree: ast.AST) -> List[Bug]:
    """Detect a new type of null bug"""
    bugs = []
    
    for node in ast.walk(tree):
        if self.is_your_bug_pattern(node):
            bugs.append(Bug(
                line=node.lineno,
                column=node.col_offset,
                message="Your bug description",
                confidence=0.75
            ))
    
    return bugs
```

### Option 3: Add a Test Case (Very Easy)
Add real-world null bugs to our test suite:

```python
# Edit: projects/null-guard/tests/test_cases.py

TEST_CASES.append({
    "name": "your_test_case",
    "code": """
        # Your code with a null bug
        user = get_user(invalid_id)
        print(user.name)  # Bug: user could be None
    """,
    "expected_bugs": 1,
    "bug_line": 3
})
```

## See Your Impact

Run the accuracy test to see how you improved NullGuard:

```bash
python -m nullguard.accuracy_test

# Output:
# Before your change: 73.2% accuracy
# After your change:  74.1% accuracy  ⬆️
# You improved accuracy by 0.9%! 🎉
```

## Try the Demo

Run the interactive demo:

```bash
# Start the web demo
python -m nullguard.demo.web

# Visit http://localhost:5000
# Paste code with null bugs
# See them detected in real-time!
```

Or use the CLI:

```bash
# Analyze a file
nullguard check myfile.py

# Analyze a project
nullguard check --recursive ./src
```

## Next Steps

### Completed the basics? Level up:

1. **Integrate with your editor**
   ```bash
   # VSCode extension
   cd extensions/vscode-nullguard
   npm install && npm run build
   ```

2. **Add context simulation**
   - Edit `mock_context.json`
   - Show how Adaptive Documentation will boost accuracy

3. **Improve the demo UI**
   - Make it beautiful
   - Add before/after comparisons
   - Show confidence scores

### Want to work on other tools?

Now that you understand the pattern:
- **Adaptive Documentation** - The critical foundation
- **Anvil Memory** - Make Git searchable
- **Anvil Comments** - Track moving comments
- **anvil-core** - Shared algorithms

## Getting Help

### Stuck? We're here to help:

**Quick questions**: Open a GitHub issue
**Real-time help**: Discord #nullguard channel
**Code review**: Submit a draft PR early
**Ideas**: Discussions → "NullGuard Ideas"

### Common Issues

**Import errors?**
```bash
pip install -e ../../anvil-core  # Install shared library
```

**Tests failing?**
```bash
pytest tests/ -v  # See which specific test fails
```

**Not sure what to work on?**
Check issues labeled `good-first-issue` and `nullguard`

## Your First PR

### Checklist:
- [ ] Code works locally
- [ ] Tests pass (`pytest`)
- [ ] Added/updated tests for your change
- [ ] Updated patterns.py or detector.py
- [ ] Ran accuracy test

### PR Template:
```markdown
## What I Changed
[Describe your change]

## Accuracy Impact
Before: X%
After: Y%

## Test Coverage
- [ ] Added new test case
- [ ] Existing tests still pass
```

## Celebrate! 🎉

You've just contributed to:
- A tool that will prevent thousands of bugs
- The showcase demo for the entire Anvil Suite
- Open source software used by developers worldwide

**Share your contribution**: Tag us on Twitter @AnvilSuite

---

## Why This Matters

Every null bug pattern you add:
1. **Prevents real bugs** in production code
2. **Saves debugging time** for developers
3. **Demonstrates** the power of pattern detection
4. **Attracts** more contributors to the project

You're not just fixing code - you're building the future of automated bug prevention.

---

*Ready to start? The code is waiting for you!*

**[Jump to NullGuard →](./projects/null-guard/)**
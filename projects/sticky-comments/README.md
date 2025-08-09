# Anvil Comments: Comments That Survive Refactoring

Part of the [Anvil Suite](../../README.md) - a simple tool solving a universal problem.

**Comments that stay attached to what they describe, not where they were written.**

*Born from The Great Simplification: No fancy AI, no complex theories. Just comments that stick to code like they should.*

## The Problem

You write a comment explaining complex logic. Two weeks later, someone refactors the code. The comment is now three functions away, describing code that no longer exists.

**Every team suffers from comment drift.**

## The Solution

StickyComments tracks comments semantically. When code moves, the comment moves with it. When code changes, you're notified if the comment needs updating.

```python
# STICKY: This validation prevents the "Tuesday bug" (issue #1234)
# Context: Payment processor fails on Tuesdays due to timezone mismatch
def validate_payment_date(date):
    if date.weekday() == 1:  # Tuesday
        date = adjust_timezone(date)
    return date
```

When this code moves to `utils/validators.py` or gets renamed to `check_date`, the comment follows.

## How It Works

1. **Parse** - Extract comments and their semantic context
2. **Fingerprint** - Create stable identifiers for code blocks
3. **Track** - Follow fingerprints through Git history
4. **Update** - Reattach comments to moved/modified code

## Quick Start

```bash
pip install sticky-comments
sticky init
sticky track  # Start tracking comments
```

## Use Cases

- **Architecture decisions** - "Why we use Redis here"
- **Bug explanations** - "This fixes the race condition from issue #456"
- **Performance notes** - "Don't optimize, we tried and it made things worse"
- **Business logic** - "Finance team requires this specific rounding"

## Project Status

🚧 **Early Development** - Seeking contributors

### What Works
- [ ] Comment extraction from Python files
- [ ] Basic AST fingerprinting
- [ ] Git history tracking

### Help Needed
- [ ] Multi-language support (JavaScript, Go, Java)
- [ ] IDE plugins (VS Code, IntelliJ)
- [ ] Refactoring detection algorithms
- [ ] Performance optimization

## Contributing

This is a focused project with a clear goal. We need:
- **Python developers** for core logic
- **IDE plugin developers** for integrations
- **Algorithm experts** for fingerprinting

## Technical Specs

- **Languages**: Python 3.8+
- **Dependencies**: GitPython, AST, SQLite
- **Performance**: Track 10,000 comments in <5 seconds
- **Accuracy**: 80% comment survival through refactoring

## Get Involved

1. Star this repo
2. Try the prototype
3. Report issues
4. Submit PRs

**No complex philosophy. No grand vision. Just solving comment drift.**

---

Contact: adrian.belmans@gmail.com | [Discord](https://discord.gg/sticky-comments)
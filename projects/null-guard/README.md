# Anvil Guard: Stop Null Bugs Before They Bite

Part of the [Anvil Suite](../../README.md) - born from The Great Simplification.

**One job: Prevent null reference exceptions. Done exceptionally well.**

*No complex theories. No overwhelming documentation. Aiming to build a tool that catches null bugs with 95% accuracy.*

📋 **[See the Prototype Plan](./PROTOTYPE.md)** - How we're building the demo that showcases everything

## Our Goal

**Target: 95% detection rate. Less than 5% false positives.**

We're building NullGuard to achieve high confidence in null reference detection.

## What It Catches

```python
# ❌ NullGuard warns: Potential null reference
user = database.get_user(user_id)
print(user['name'])  # What if get_user returns None?

# ✅ NullGuard approves: Null check present
user = database.get_user(user_id)
if user:
    print(user['name'])
```

## Why It's Different

Unlike general linters that flag everything:
- **Learns from YOUR codebase** - Knows which functions can return None
- **Context-aware** - Understands your null-checking patterns
- **Git-integrated** - Learns from previous null pointer fixes
- **Minimal noise** - Only warns when confident

## Installation

⚠️ **Note: NullGuard is in development. These commands show intended usage.**

```bash
# Clone the repository (package not yet published to PyPI)
git clone https://github.com/anvil-suite/code-periodic-table.git
cd code-periodic-table/projects/null-guard
pip install -e .

# Future usage (not yet implemented):
# anvil-guard init  # Will analyze your codebase
# anvil-guard check file.py  # Will check specific file
# anvil-guard watch  # Will provide real-time monitoring
```

**Current Status**: See [PROTOTYPE.md](./PROTOTYPE.md) for development progress.

## How It Works

1. **Analyzes your Git history** for previous null pointer fixes
2. **Learns your codebase patterns** - which functions return None
3. **Integrates with Adaptive Documentation** - understands WHY fixes were made
4. **Builds a model** specific to your code with rich context
5. **Provides targeted warnings** with high confidence

**The Vision**: When integrated with [Adaptive Documentation](../adaptive-documentation/), Anvil Guard could potentially understand not just that a null check was added, but WHY. This context ("getUser() returns null for inactive users") is what we believe will enable our target 95% accuracy.

## Performance

| Metric | Target | Status |
|--------|--------|---------| 
| Detection Rate | 95% | Not yet measured |
| False Positives | <5% | Not yet measured |
| Analysis Speed | <100ms | Not yet measured |
| Languages | Python, JS, Java | Planned: Python first |

## Example Output (Conceptual)

```
# This shows the intended output format once implemented:
nullguard check auth.py

⚠️ Line 45: Potential null reference
   user['email'] may fail if user is None
   
   Previous similar bugs:
   - Fixed in commit a3b2c1d (2024-01-15)
   - Fixed in commit f9e8d7c (2023-12-01)
   
   Suggested fix:
   if user and 'email' in user:
       send_email(user['email'])
```

## Scope Limitations (By Design)

NullGuard ONLY detects null reference bugs. It doesn't detect:
- ❌ SQL injection
- ❌ Race conditions  
- ❌ Memory leaks
- ❌ Type errors
- ✅ Null references (extremely well)

**One pattern. Exceptional accuracy.**

## Contributing

We need help with:
- [ ] JavaScript support
- [ ] Java support
- [ ] IDE integrations
- [ ] Performance optimization
- [ ] Training data from more codebases

## Vision for Success

> "We aim to build a tool that catches real null bugs without false alarms."  
> — Project Goal

> "Our target is to become the tool that doesn't cry wolf."  
> — Design Philosophy

## The Philosophy

Do one thing. Do it better than anyone else. Build trust through accuracy.

## Status

📋 **Pre-Development** - See [PROTOTYPE.md](./PROTOTYPE.md) for the development plan

---

**Not trying to detect everything. Just null references. Aiming for perfection.**

Contact: adrian.belmans@gmail.com
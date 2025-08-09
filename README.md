# Anvil: Never Fix the Same Bug Twice

Your team fixed this bug three months ago. And six months before that. And last year.  
But the developer who knew about it left, and now you're debugging it again.

**Anvil remembers what your team learned, so you don't lose it.**

```bash
# See it in action
pip install anvil-preview
anvil init
anvil check  # Warns you BEFORE you repeat a mistake
```

[**Get Started →**](./GETTING_STARTED.md) | [**See Demo →**](./DEMO.md) | [**View Mockups →**](./anvil/mockups/)

---

## What Anvil Does (30-second version)

- 🔍 **Watches** your Git history to learn what went wrong before
- ⚠️ **Warns** you in your IDE when you're about to repeat a mistake
- 💬 **Preserves** the "why" behind decisions through semantic comments
- 🔒 **Runs locally** - your code never leaves your machine

## The Problem We're Solving

Every team loses critical knowledge:
- "We tried this approach before, it doesn't work" *(but nobody remembers why)*
- "There's a subtle bug in this pattern" *(discovered after 3 incidents)*
- "Don't refactor this, it breaks X" *(the person who knew X left)*

**Current tools don't learn from YOUR team's specific history and mistakes.**

## Quick Demo

```python
# You write this code:
user_data = fetch_user(user_id)
process_payment(user_data['payment_info'])

# Anvil warns you:
⚠️ Similar code caused null pointer exception in commit 3fa2b1c (2024-01-15)
   Fix: Check if 'payment_info' exists before accessing
   Previous developer note: "Payment info is optional for guest users"
   
# You avoid a bug that already bit your team twice
```

## How to Contribute

We need builders, not philosophers. Here's how to help:

### 🔨 For Developers
- Build the Git analysis engine
- Create IDE integrations
- Improve pattern detection
- [See open issues →](https://github.com/devknowledge-ai/anvil/issues)

### 🎨 For Designers
- Design warning UI/UX
- Create feedback mechanisms
- Improve developer experience
- [View mockup needs →](./anvil/mockups/NEEDED.md)

### 🧪 For Early Adopters
- Test with your codebase
- Report false positives
- Share use cases
- [Join beta →](./BETA.md)

## Project Status

- ✅ Problem validated with 50+ developer interviews
- ✅ Core algorithm designed
- ✅ Architecture planned
- 🚧 Building prototype
- ⏳ Seeking contributors and early testers

## The Irony That Shaped This Project

*A brief human moment:*

While documenting this project, we wrote 50+ documents about preventing lost knowledge... then nearly lost track of our own knowledge in the documentation maze. A contributor pointed out we were exhibiting the exact problem we're trying to solve—critical information buried in overwhelming complexity.

That feedback became the most valuable contribution yet. We restructured everything, and ironically, the critique itself is exactly the kind of wisdom Anvil should preserve: *"Your project structure is sabotaging your goals, here's why..."*

**This is why Anvil matters.** Not for the grand vision of universal code classification, but for preserving these specific, crucial moments of clarity that make or break projects.

## Get Started in 5 Minutes

```bash
# Clone and try the prototype
git clone https://github.com/devknowledge-ai/anvil
cd anvil
python prototype/detect_repeated_fixes.py ./your-repo

# See what patterns your team repeats
```

[**Full Getting Started Guide →**](./GETTING_STARTED.md)

## FAQ

**Q: Is this just another linter?**  
A: No. Linters check against fixed rules. Anvil learns from YOUR team's specific history.

**Q: Does it require cloud services?**  
A: No. Runs 100% locally. Your code never leaves your machine.

**Q: What languages does it support?**  
A: Starting with Python, JavaScript, Go. The approach is language-agnostic.

**Q: How accurate is it?**  
A: Currently targeting 70% detection with <20% false positives. You control sensitivity.

## Contact

**Project Lead**: Adrian Belmans  
**Email**: adrian.belmans@gmail.com  
**Discord**: [Join our community](https://discord.gg/anvil)

---

### The Bigger Picture

*Curious about our long-term research vision? We're exploring how pattern recognition could transform programming. But that's tomorrow's dream. Today, we're building Anvil to solve a real problem.*

[Learn about our vision →](./vision/) *(Optional reading - Anvil stands on its own)*


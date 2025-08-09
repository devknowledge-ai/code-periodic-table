# Reality Check: The HCI Problem We Haven't Solved

## The Brutal Truth

This document acknowledges the critical flaw in Adaptive Documentation: **We've replaced one hard problem (pattern classification) with another equally hard problem (non-intrusive context capture).**

## The Two Paths and Their Fatal Flaws

### Path 1: LLM Context Capture (The "Access Problem")
**Promise**: Automatically extract documentation from LLM conversations (95% signal)  
**Reality**: We don't own the platforms

- **GitHub Copilot**: No API for chat history
- **Claude Code**: No programmatic access to conversations
- **ChatGPT**: Sessions are isolated, no IDE integration
- **Cursor/Codeium**: Proprietary, closed systems

**What we pretended**: `claude-code --enable-context-capture`  
**What exists**: Nothing. This is fictional.

### Path 2: Smart Prompting (The "Annoyance Problem")
**Promise**: Intelligently prompt developers at the perfect moment  
**Reality**: This is an unsolved AI-hard problem

The "Goldilocks Zone" is impossibly narrow:
- **Too frequent**: Tool gets uninstalled in rage
- **Too rare**: Miss critical context, no value
- **Wrong moment**: Break flow state, developer hatred

**What we need**: Near-perfect flow state detection  
**What we have**: Hand-waving about "natural pauses"

## The Cascade Failure

```
Adaptive Documentation fails
        ↓
No clean training data
        ↓
Anvil Guard can't achieve 95% accuracy
        ↓
GitMemory has only noise to index
        ↓
Entire Anvil suite becomes "just another linter"
```

## The Honest Research Questions

1. **Can we actually access LLM conversation data?**
   - Current answer: No
   - Required: Platform partnerships or reverse engineering

2. **Can we detect the perfect moment to prompt?**
   - Current answer: No proven approach
   - Required: Extensive HCI research, user studies

3. **Will developers tolerate ANY interruption?**
   - Current answer: Probably not
   - Required: Radically different approach

## What We Should Build First (The Honest MVP)

### Phase 0: Manual Proof of Value
**Stop pretending we have magic. Start with explicit user action.**

```python
# Version 0.1: Dead simple manual capture
class ManualDocumentationCapture:
    """
    No AI. No magic. Just a button.
    """
    def capture_on_demand(self):
        # User explicitly clicks "Document This"
        return {
            "trigger": "user_initiated",
            "friction": "high_but_honest",
            "value": "needs_validation"
        }
```

### Test These Hypotheses First:

1. **Value Test**: If developers manually attach LLM conversations to code, does it actually help?
2. **Friction Test**: What percentage will use a manual "Save Context" button?
3. **Access Test**: Can we even GET the LLM conversation data with user cooperation?

### Only After Proving Value:

4. **Timing Research**: Study actual developer workflows
5. **Prototype Triggers**: Git hooks first, not "flow detection"
6. **Platform Negotiations**: Talk to GitHub/Anthropic about APIs

## The Three Possible Outcomes

### 1. We Solve Platform Access
- Partner with GitHub/Anthropic for official APIs
- Build browser extensions for web-based tools
- Focus entirely on open-source LLMs we can instrument

### 2. We Solve the HCI Problem
- Discover developers will tolerate git commit hooks
- Find that batch processing (end of day) is acceptable
- Learn that opt-in manual capture is sufficient

### 3. We Pivot to Reality
- Abandon "adaptive" triggering
- Focus on extracting value from existing artifacts
- Accept lower signal quality, adjust accuracy promises

## The Real Research Priority

**Old framing**: "Adaptive Documentation is the foundation that enables everything"

**Honest framing**: "Adaptive Documentation is an unsolved research problem that everything depends on"

## Recommendation: Start Here

```bash
# Week 1-2: Build the dumbest possible version
adaptive-doc init --mode=manual
adaptive-doc capture --explicit-button-only

# Week 3-4: Measure if anyone uses it
adaptive-doc analytics --adoption-rate
adaptive-doc survey --why-not-used

# Week 5-6: Only if adoption > 10%
adaptive-doc experiment --git-hooks
adaptive-doc experiment --pr-comments
```

## The Critical Question

**Not**: "How do we build perfect adaptive triggering?"

**But**: "Will developers provide documentation under ANY circumstances that don't make them hate us?"

If the answer is no, the entire Anvil suite needs a different foundation.

---

*This document exists because intellectual honesty is more valuable than false confidence.*
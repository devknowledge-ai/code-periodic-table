# Adaptive Documentation: The Foundation of the Anvil Suite

**The #1 Priority** - This ambitious research project aims to capture the "why" behind code changes.

*Born from The Great Simplification: Our goal is to move from noisy Git history (10% signal) to capturing context at the source (potentially 95% signal).*

## What It Does

Adaptive Documentation intelligently prompts developers to document code changes at the optimal moment, learning from individual preferences and team patterns to minimize friction while maximizing documentation value.

```bash
# IDE integration that learns your patterns
adaptive-doc monitor --learn-mode
adaptive-doc capture --smart-timing
```

## Output

Rich, contextual documentation that travels with your code:

```json
{
  "change_id": "abc123",
  "timestamp": "2024-01-15T10:30:00Z",
  "code_fingerprint": "auth_null_check_v2",
  "documentation": {
    "why": "getUser() can return null for inactive users",
    "impact": "Prevents NPE in production when users are deactivated",
    "alternatives_considered": "Throwing exception, but would break existing flows"
  },
  "capture_method": "voice_note",
  "developer_state": "natural_pause",
  "confidence": 0.95
}
```

## Features

- **Adaptive Timing** - Never interrupts flow, always catches important changes
- **Learning System** - Adapts to individual developer preferences and patterns
- **Code Review Integration** - Learns from PR comments what needs documentation
- **Multi-Modal Capture** - Text, voice notes, diagrams, or links
- **Privacy-Preserving** - Federated learning keeps your code secure

## Core Innovation

The system learns THREE things simultaneously:
1. **WHEN to ask** - Based on change significance and developer state
2. **HOW to ask** - Matching each developer's style (minimalist to comprehensive)
3. **WHAT to ask** - Learning from code reviews what generates questions

## Installation (Planned)

**Note: No working implementation exists yet. These commands show intended usage.**

```bash
# Future VS Code Extension (not yet available)
code --install-extension adaptive-documentation

# Future CLI Tool (not yet available)
npm install -g adaptive-doc
```

## Usage

### IDE Integration
```typescript
// Automatic monitoring with smart prompts
// Extension learns your patterns and preferences
```

### CLI Mode
```bash
# Start monitoring
adaptive-doc start

# Configure preferences
adaptive-doc config --style minimalist --timing batch

# View statistics
adaptive-doc stats --show-learning-curve
```

## Smart Triggering Examples

### Minimalist Developer Flow
```
[Small change detected]
System: 🔔
Dev: *clicks*
System: "Performance fix?" [Y/N]
Dev: Y
System: "Benchmark?" 
Dev: "50ms → 10ms"
[Done - 5 seconds]
```

### Code Review Learning
```
[PR Comment]: "Why change from Promise.all to sequential?"
System: *learns this pattern needs documentation*

[Next similar change]
System: "Previous reviews asked about parallel→sequential. Explain?"
Dev: "Prevents rate limiting with external API"
[Future PRs pre-answered]
```

## Use Cases

- **Prevent Knowledge Loss** - Capture decisions before they're forgotten
- **Accelerate Code Reviews** - Pre-answer common questions
- **Onboard Faster** - New developers understand the "why"
- **Train AI Models** - Clean data for pattern learning
- **Build Team Memory** - Collective knowledge that grows over time

## Success Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Documentation rate | 70% of significant changes | In development |
| Developer engagement | >60% respond to prompts | Testing phase |
| Review questions reduced | 40% fewer "why?" comments | Measuring |
| Time to document | <30 seconds average | Optimizing |

## LLM-Assisted Development: The Game Changer

When developers use Claude Code, GitHub Copilot, or ChatGPT to write code, the documentation problem fundamentally transforms:

### Traditional vs. LLM-Assisted Development
- **Traditional**: Intent in developer's mind → Code written → Documentation extracted later (10% signal)
- **LLM-Assisted**: Intent explicitly stated → Discussion documented → Code generated WITH context (95% signal)

### Zero-Friction Documentation
The conversation between developer and LLM contains everything:
- Complete problem statement and requirements
- Design decisions and trade-offs discussed
- Implementation reasoning and alternatives
- Error corrections and refinements

```python
# Example: Automatic context extraction from Claude Code session
{
  "user_request": "Add rate limiting to prevent API abuse",
  "problem": "IPs making 1000+ requests/minute",
  "llm_suggestion": "Token bucket algorithm",
  "alternatives_discussed": ["Fixed window (burst issues)", "Sliding window (memory overhead)"],
  "decision": "Token bucket for smooth limiting",
  "code_generated": "link://session/12345#code-block-3"
}
```

### Integration Example
```bash
# Claude Code with automatic context capture
claude-code --enable-context-capture

# Git commits include full context
git commit -m "Add rate limiting" --llm-context=.claude-session.json
```

See [llm-integration.md](./llm-integration.md) for complete LLM integration details.

## Why This Is The Foundation (If Successful)

**This aims to solve the core data problem.** Every other tool in the Anvil suite could benefit from clean, structured data about why code changes - if we can capture it.

- **Without LLM assistance**: Raw Git history has ~10% signal, we would need to prompt developers to fill gaps
- **With LLM assistance**: Conversations could contain ~95% signal, if we can extract it

**Note**: Other tools can provide baseline functionality without this data:
- **Anvil Guard** - Can detect patterns from Git history alone (lower accuracy)
- **GitMemory** - Can search standard Git commits (less context)
- **Future ML Models** - Can train on existing data (noisier results)

The enhanced capabilities depend on successfully solving the context capture problem.

## Contributing

Critical areas needing help:
- [ ] Flow state detection algorithms
- [ ] Code review pattern analysis
- [ ] Federated learning implementation
- [ ] Voice transcription integration
- [ ] Multi-IDE support (IntelliJ, Sublime, etc.)

## Status

⚠️ **Critical Research Challenge** - This is an unsolved HCI problem that would significantly enhance the Anvil suite if solved

### The Honest State of Things

- **LLM Integration**: No APIs exist. Platform access is fictional.
- **Smart Prompting**: Flow state detection is AI-hard. We have no solution.
- **Developer Tolerance**: Unknown if developers will document under ANY circumstances.

### The Pragmatic Path Forward: Partnerships

**Instead of waiting for APIs that don't exist, we're partnering with open-source AI coding tools.**

See [partnerships.md](./partnerships.md) - Roo-code, Cline, Aider, and others already have the data we need.

See [integration-api-spec.md](./integration-api-spec.md) - Simple API that any AI tool can implement.

See [mvp-manual.md](./mvp-manual.md) - Start with a simple button. Prove value. Only then add "magic."

See [REALITY_CHECK.md](./REALITY_CHECK.md) - The brutal honesty about what we haven't solved.

---

**Capturing the "why" at the moment of change. The foundation of collective team memory.**

Contact: adrian.belmans@gmail.com
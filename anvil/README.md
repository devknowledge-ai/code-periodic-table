# Anvil: The Practical Tool

*Building a team's collective memory, one commit at a time*

---

## Overview

Anvil is the practical realization of our vision—a tool that learns from your team's unique history to prevent repeated mistakes and preserve institutional knowledge. While our long-term vision explores the "Digital Universe" of code, Anvil delivers immediate, tangible value to development teams today.

## Core Capabilities

### 🔍 Mistake Prevention
Analyzes your Git history to identify when you're about to repeat a past mistake. Like having a senior developer looking over your shoulder, warning you about pitfalls the team has encountered before.

### 💬 Semantic Comments
Links comments to the *meaning* of code, not just line numbers. When code moves or refactors, the context moves with it. The "why" behind decisions is never lost.

### 🧠 Pattern Learning
Learns your team's specific patterns, conventions, and decisions. Every team is unique—Anvil adapts to yours.

### 🔒 Privacy-First
Runs entirely locally. Your code never leaves your machine. No cloud dependencies, no privacy concerns.

## How Anvil Works

```mermaid
graph LR
    A[Git History] --> B[Pattern Analysis]
    B --> C[Team Knowledge Base]
    C --> D[Real-time Warnings]
    D --> E[Developer IDE]
    E --> F[Prevented Mistakes]
```

1. **Observes** - Continuously analyzes your Git history
2. **Learns** - Identifies patterns in bugs, fixes, and refactorings
3. **Remembers** - Builds a knowledge base specific to your team
4. **Warns** - Provides real-time guidance in your IDE
5. **Adapts** - Improves based on your feedback

## Architecture

Anvil follows a modular, extensible architecture aligned with our [Digital Universe principles](../vision/digital-universe-theory.md):

- **Local-First**: All processing happens on your machine
- **Incremental**: Learns progressively without disrupting workflow
- **Adaptive**: Evolves with your team's changing patterns
- **Respectful**: Never imposes, only suggests

[**→ Detailed Architecture Documentation**](./architecture/)

## Specifications

### MVP Features (Phase 1)
- Git history analysis
- Pattern detection 
- IDE warnings
- Basic semantic linking

### Enhanced Features (Phase 2)
- Cross-file pattern recognition
- Refactoring tracking
- Team dashboard
- Performance optimization

### Advanced Features (Phase 3)
- ML-powered predictions
- Cross-team learning (opt-in)
- Custom pattern definitions
- API for extensions

[**→ Full Feature Specifications**](./specifications/)

## Why Anvil Succeeds Where Others Failed

### 1. Team-Specific, Not Universal
We don't try to impose universal rules. Anvil learns YOUR team's patterns, YOUR conventions, YOUR history.

### 2. Immediate Value
No need to wait for a grand unified theory. Anvil provides value from day one by preventing your team's specific repeated mistakes.

### 3. Privacy by Design
Local-first architecture means your code never leaves your control. No trust required.

### 4. Progressive Enhancement
Starts simple, grows smarter. Each prevented mistake makes the system better.

## Implementation Status

### ✅ Completed
- Core concept validation
- Architecture design
- Pattern detection algorithms (theoretical)
- User workflow design

### 🚧 In Progress
- Prototype development
- Git analysis engine
- IDE extension framework

### 📋 Next Steps
- Build proof-of-concept
- Test with pilot teams
- Refine based on feedback
- Scale to production

## Get Involved

### For Developers
Help build the tool:
- Git analysis algorithms
- IDE integrations
- Pattern detection
- Performance optimization

### For Teams
Be an early adopter:
- Test prototypes
- Provide feedback
- Share use cases
- Shape the product

### For Researchers
Validate our approach:
- Review algorithms
- Suggest improvements
- Contribute research
- Analyze results

## The Connection to Our Vision

While Anvil stands alone as a valuable tool, it's also our laboratory for understanding the Digital Universe of code. Every pattern detected, every mistake prevented, contributes to our larger understanding of how code evolves and how knowledge can be preserved.

But you don't need to believe in the vision to benefit from Anvil. The tool's value is immediate and practical.

---

*Anvil: Because your team's history shouldn't be mystery.*

[← Back to Project Overview](../README.md) | [Specifications →](./specifications/) | [Architecture →](./architecture/)
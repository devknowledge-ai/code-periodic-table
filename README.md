# The Anvil Suite: Forging Your Team's Collective Memory

A suite of focused developer tools born from **The Great Simplification** - our pivot from an overly complex research project to practical, shippable tools that solve real problems.

📖 **Read our story**: [The Anvil Story - From Vision to Suite](./ANVIL_STORY.md) 

Each tool in the suite does one thing exceptionally well. Together, they transform how teams preserve institutional memory.

## 🎯 Priority #1: Adaptive Documentation
**The Foundation That Powers Everything**

[**Adaptive Documentation**](./projects/adaptive-documentation/) captures the "why" behind code changes - the context and reasoning that makes all our other tools intelligent. This is the most critical component of the Anvil Suite.

- **Problem**: 90% of valuable context is lost in Git history noise
- **Solution**: Capture context at the source, especially from AI coding assistants
- **Impact**: Transforms 10% signal (Git) into 95% signal (structured knowledge)
- **Status**: 🚨 **Critical Priority** - The entire suite depends on this

[**Start Contributing Here →**](./projects/adaptive-documentation/)

## 🛠️ The Anvil Tools

Each tool is independent but gains superpowers when powered by Adaptive Documentation:

### [Anvil Context](./projects/anvil-context/) 
**Living documentation for code, errors, and crashes**  
Status: 🚧 Early Development | Powered by: Fingerprinting + Integration
*Evolved from "Sticky Comments" into comprehensive context system*

### [Anvil Guard](./projects/null-guard/)
**Prevent null reference exceptions with 95% accuracy**  
Status: 🧪 Beta Testing | Powered by: Historical bug patterns + context

### [Anvil Memory](./projects/git-memory/)
**Your team's searchable knowledge base**  
Status: 🚧 Active Development | Powered by: Enriched commit context

### [Anvil Fingerprint](./projects/code-fingerprint/)
**Stable identity for code patterns**  
Status: 🔬 Research Phase | Powered by: Pattern evolution tracking

## Why The Anvil Suite?

Every developer knows the pain:
- Comments that drift away from the code they describe
- Null pointer bugs that keep coming back
- Git history that's write-only
- Similar code that's impossible to find
- **The "why" behind code changes lost forever**

We're building focused tools to solve these specific problems. Each tool does one thing exceptionally well.

## The Research Loop

The Anvil Suite operates on a continuous cycle: **Tools solve problems → Generate data → Validate research → Improve tools**

Read [**RESEARCH_LOOP.md**](./RESEARCH_LOOP.md) to understand how practical tool development drives scientific insights.

## How to Contribute

**Start with the problem that affects you most:**

| Project | Problem It Solves | Skills Needed | Difficulty |
|---------|------------------|---------------|------------|
| **[Adaptive Documentation](./projects/adaptive-documentation/)** 🎯 | Lost context and reasoning | Python, API integration | Medium |
| **[Anvil Guard](./projects/null-guard/)** | Null/None bugs | Pattern matching, AST | Medium |
| **[Anvil Memory](./projects/git-memory/)** | Unsearchable Git history | Git internals, search | Medium |
| **[Anvil Comments](./projects/sticky-comments/)** | Drifting comments | AST manipulation, diffs | Hard |
| **[Anvil Fingerprint](./projects/code-fingerprint/)** | Unstable code identity | Algorithms, compilers | Hard |
| **[anvil-core](./anvil-core/)** | Shared intelligence | Architecture, algorithms | Hard |

See [**CONTRIBUTING.md**](./CONTRIBUTING.md) for detailed contribution guidelines.

## Project Philosophy

- **Small scope** - Each tool solves one problem exceptionally well
- **High quality** - Better to do one thing perfectly than many things poorly
- **Independent value** - Each tool is useful standalone
- **Shared foundation** - Common functionality in [anvil-core](./anvil-core/)
- **Open source** - MIT licensed, community-driven
- **Data-driven** - Let real usage guide development

## Architecture: How It All Works Together

```
┌─────────────────────────────────────────────────────────┐
│                  Adaptive Documentation                  │
│         Captures the "why" from developers & AI          │
└────────────────────┬─────────────────────────────────────┘
                     │ High-signal context data
                     ▼
┌─────────────────────────────────────────────────────────┐
│                      anvil-core                          │
│    Shared algorithms, fingerprinting, pattern analysis   │
└──────┬──────────┬──────────┬──────────┬─────────────────┘
       │          │          │          │
       ▼          ▼          ▼          ▼
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
│  Guard   │ │  Memory  │ │ Comments │ │Fingerprint│
│          │ │          │ │          │ │           │
│ Prevents │ │ Searches │ │  Tracks  │ │Identifies │
│   bugs   │ │ history  │ │ comments │ │ patterns  │
└──────────┘ └──────────┘ └──────────┘ └──────────┘
```

**The Key Insight**: Adaptive Documentation transforms noisy Git history (10% signal) into structured knowledge (95% signal), especially when integrated with AI coding assistants. This clean data powers all other tools to achieve unprecedented accuracy.

## ⚠️ Current Status

**Important**: This project is in early planning stages. **No working code exists yet.**  
See [**PROJECT_STATUS.md**](./PROJECT_STATUS.md) for complete transparency about what's real vs. planned.

## 🚀 Quick Start

**New contributor?** → [**Get Started with NullGuard in 30 minutes**](./GETTING_STARTED.md) *(Building from scratch)*  
**Want to help with partnerships?** → [**Partnership Tracker**](./PARTNERSHIP_TRACKER.md)  
**Interested in performance?** → [**Performance Benchmarks**](./anvil-core/PERFORMANCE_BENCHMARKS.md)

## Learn More

- 📖 [**The Great Simplification**](./THE_GREAT_SIMPLIFICATION.md) - How we pivoted from complexity to focus
- 🎯 [**Vision and Research**](./VISION.md) - Where we're heading (concise overview)
- 🛠️ [**Contributing Guide**](./CONTRIBUTING.md) - Visual map of where to contribute
- 🔄 [**The Research Loop**](./RESEARCH_LOOP.md) - How tools generate insights (detailed)

## Contact

**Project Lead**: Adrian Belmans  
**Email**: adrian.belmans@gmail.com  
**GitHub**: [@anvil-tools](https://github.com/anvil-tools)

---

*The Anvil Suite: Simple tools. Real problems. Shipped code.*


# The Anvil Suite: Forging Your Team's Collective Memory

A suite of focused developer tools that capture, preserve, and leverage your team's collective knowledge. Each tool solves a specific problem, but together they transform how teams preserve institutional memory.

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

### [Anvil Comments](./projects/sticky-comments/) 
**Comments that survive refactoring**  
Status: 🚧 Early Development | Powered by: Code fingerprinting

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

## Contact

**Project Lead**: Adrian Belmans  
**Email**: adrian.belmans@gmail.com  
**GitHub**: [@anvil-tools](https://github.com/anvil-tools)

---

*Anvil: Forging better developer tools. One focused project at a time.*


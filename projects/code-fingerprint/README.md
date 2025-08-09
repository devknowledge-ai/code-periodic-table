# Anvil Fingerprint: Stable Identity for Code Patterns

Part of the [Anvil Suite](../../README.md) - solving the code identity problem.

**Generate stable fingerprints for code that survive syntax changes.**

*The Great Simplification in action: Forget complex pattern classification. Just give code a stable identity so we can track it.*

## The Problem

This is the same code:
```python
# Version A
result = [x * 2 for x in data if x > 0]

# Version B
result = []
for x in data:
    if x > 0:
        result.append(x * 2)
```

But traditional hashing sees them as completely different.

## The Solution

CodeFingerprint generates semantic hashes based on what code DOES, not how it LOOKS.

```python
from codefingerprint import fingerprint

code_a = "[x * 2 for x in data if x > 0]"
code_b = "for x in data:\n    if x > 0:\n        result.append(x * 2)"

print(fingerprint(code_a))  # "sf:map:filter:mul2:gt0:a7b3c"
print(fingerprint(code_b))  # "sf:map:filter:mul2:gt0:a7b3c"
# Same fingerprint!
```

## How It Works

1. **Parse** code into Abstract Syntax Tree (AST)
2. **Normalize** language-specific constructs
3. **Extract** semantic operations (map, filter, iterate)
4. **Hash** the normalized operations

## Use Cases

- **Clone Detection** - Find duplicate code across projects
- **Plagiarism Detection** - Identify copied homework/code
- **Refactoring Tracking** - Follow code through refactors
- **Pattern Matching** - Find similar code structures
- **Code Search** - "Find code that does X"

## Quick Start

```bash
pip install codefingerprint

# CLI usage
codefingerprint analyze script.py

# API usage
from codefingerprint import fingerprint
sig = fingerprint(your_code)
```

## Supported Languages

- ✅ Python - Full support
- 🚧 JavaScript - In development
- 📋 Java - Planned
- 📋 Go - Planned
- 📋 C++ - Planned

## Accuracy Metrics

| Test Case | Accuracy |
|-----------|----------|
| Syntax variations | 92% |
| Variable renaming | 98% |
| Whitespace/formatting | 100% |
| Logic reordering | 76% |
| Algorithm substitution | 45% |

## Contributing

This is a challenging computer science problem. We need:

- **Compiler experts** - AST normalization
- **Algorithm researchers** - Semantic equivalence
- **Language specialists** - Multi-language support
- **ML engineers** - Learning-based approaches

## Research Foundation

Based on established research:
- Jiang et al. "DECKARD: Scalable and Accurate Tree-Based Detection"
- Kamiya et al. "CCFinder: Multi-linguistic Token-based Code Clone Detection"
- Our approach: Simplified, practical implementation

## Current Limitations

- Cannot detect algorithmic equivalence (quicksort vs mergesort)
- Struggles with heavily optimized code
- Language-specific idioms need manual rules

## Status

🔬 **Research Phase** - Python prototype working, seeking contributors for other languages

---

**One hard problem, solved well.**

Contact: adrian.belmans@gmail.com
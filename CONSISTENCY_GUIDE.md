# Documentation Consistency Guide

## Purpose

This guide ensures all documentation in the Code Periodic Table project maintains consistent messaging about the project's status and nature.

## Core Truth Statement

**The Code Periodic Table project is a theoretical research exploration with ZERO implementation.** No code, tools, or working software exists.

## Key Messages to Maintain

### 1. Implementation Status
- **ALWAYS state**: "No implementation exists"
- **NEVER claim**: "Working tools", "Available now", "Production ready"
- **NEVER provide**: Setup instructions, installation guides, or usage examples

### 2. Performance Metrics
- **ALWAYS label as**: "Theoretical", "Hypothetical", "Speculative", "Imaginary"
- **NEVER present as**: Achieved, measured, tested, or proven
- **Example**: "Theoretical target: 70% accuracy (if built)" ✅
- **NOT**: "Achieves 70% accuracy" ❌

### 3. Development Status
- **Phase 1**: Conceptual only, 0% implemented
- **Phase 2**: Theoretical proposal, depends on non-existent Phase 1
- **Phase 3**: Pure research, highly speculative

### 4. Timeline Claims
- **ALWAYS state**: "No timeline", "May never be built", "Unknown if feasible"
- **NEVER promise**: Specific dates, "Coming soon", "In development"

## Required Disclaimers

### For Main Documents
Place at the top of README files:
```markdown
## ⚠️ IMPORTANT: This is a research project with NO working implementation

This repository contains theoretical concepts, research documentation, and proposed designs only. 
**No functional software, tools, or code exists.**
```

### For Technical Documents
```markdown
## ⚠️ DISCLAIMER

This document describes theoretical approaches for software that does not exist.
All technical details are speculative and have not been implemented or tested.
```

### For Contribution Documents
```markdown
## ⚠️ NOTE: There is NO CODE in this project

Contributions are welcome for research, documentation, and theoretical frameworks only.
There are no tools to test, no code to review, and no software to install.
```

## Consistency Checklist

Before committing any documentation changes, verify:

- [ ] No claims of working tools or implementations
- [ ] No specific performance metrics without "theoretical" qualifier
- [ ] No installation or setup instructions
- [ ] No timelines or promises of future availability
- [ ] Clear disclaimers about non-existence of code
- [ ] Consistent use of conditional language ("would", "could", "might")
- [ ] Reality check against IMPLEMENTATION_STATUS.md

## Language Guidelines

### Use These Terms
- "Conceptual", "Theoretical", "Proposed", "Hypothetical"
- "Research", "Exploration", "Investigation"
- "Would", "Could", "Might" (conditional)
- "If built", "If implemented", "If it existed"

### Avoid These Terms
- "Works", "Available", "Ready", "Functional"
- "Install", "Download", "Setup", "Use"
- "Is", "Does", "Provides" (when describing non-existent features)
- "Coming soon", "In development", "Under construction"

## Review Process

1. **Self-check**: Use this guide's checklist
2. **Cross-reference**: Verify against IMPLEMENTATION_STATUS.md
3. **Reality check**: Read reality-check/READ-THIS-FIRST.md
4. **Peer review**: Have someone verify consistency

## Common Pitfalls to Avoid

1. **Aspirational Writing**: Writing as if the future state exists
2. **Marketing Language**: Making the project sound more advanced than it is
3. **Implied Functionality**: Suggesting tools work through examples
4. **Buried Disclaimers**: Hiding non-existence warnings in small text

## Updating This Guide

As the project evolves (or doesn't), update this guide to reflect:
- New consistent messaging requirements
- Common errors found in reviews
- Clarifications needed based on user confusion

## The Golden Rule

**When in doubt, emphasize what DOESN'T exist over what might exist someday.**

---

Last Updated: 2025
Purpose: Maintain honest, consistent documentation across all project files
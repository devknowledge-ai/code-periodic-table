# State of Hypotheses: Current Evidence Dashboard

## Overview

This document tracks the current state of our major hypotheses, presenting evidence both for and against each claim. This is a living document that evolves as we gather more data.

**Last Updated**: 2025
**Overall Status**: Early research, most hypotheses unproven

---

## Core Hypotheses

### Hypothesis 1: Code Patterns Can Be Systematically Classified

**Claim**: It's possible to create a systematic classification system for code patterns, similar to the periodic table for chemical elements.

**Evidence FOR**:
- Local patterns within teams show repeatability
- Certain patterns (Singleton, Observer) are universally recognized
- AST analysis can identify structural patterns
- Git history shows pattern evolution over time

**Evidence AGAINST**:
- Current accuracy only 40-70%
- Cross-language patterns extremely difficult
- Combinatorial explosion of pattern variations
- Rice's Theorem suggests fundamental limits

**Current Verdict**: **PARTIALLY VALIDATED** for local patterns, **UNPROVEN** for universal classification

**Next Steps**: Focus on improving local pattern recognition before attempting universal classification

---

### Hypothesis 2: Teams Repeat ~40% of Their Mistakes

**Claim**: Development teams repeat approximately 40% of previously fixed bugs and mistakes.

**Evidence FOR**:
- Initial analysis of 5 repositories shows 35-45% repetition
- Anecdotal evidence from developers confirms this
- Similar bugs appear in different parts of codebase
- Copy-paste propagates mistakes

**Evidence AGAINST**:
- Sample size too small for statistical significance
- "Repetition" definition is fuzzy
- Some "repeated" mistakes are actually different
- Modern tooling already catches many repeats

**Current Verdict**: **PRELIMINARY SUPPORT**, needs larger study

**Next Steps**: Analyze 100+ repositories for statistical validation

---

### Hypothesis 3: We Can Achieve 80%+ Pattern Recognition Accuracy

**Claim**: Our approach can achieve 80% or higher accuracy in pattern recognition.

**Evidence FOR**:
- Current prototypes at 40-70% show improvement possible
- More training data consistently improves accuracy
- Some specific patterns achieve 85%+ accuracy
- Domain-specific models perform better

**Evidence AGAINST**:
- Plateau effect observed around 70%
- Performance degrades on real-world code
- False positive rate remains high
- Theoretical limits may prevent 80%+

**Current Verdict**: **UNPROVEN**, significant challenges remain

**Next Steps**: Experiment with different ML architectures, feature engineering

---

### Hypothesis 4: Learning from Git History Provides Valuable Signals

**Claim**: Git commit history contains valuable information for understanding pattern evolution and mistakes.

**Evidence FOR**:
- Refactoring commits show pattern improvements
- Bug fix commits identify problematic patterns
- Commit messages provide intent information
- Historical analysis reveals team practices

**Evidence AGAINST**:
- Signal-to-noise ratio very low
- Merge commits pollute analysis
- Commit quality varies wildly
- Rebasing destroys historical information

**Current Verdict**: **PARTIALLY VALIDATED**, but extraction is difficult

**Next Steps**: Develop better filtering algorithms for git noise

---

### Hypothesis 5: Local Learning Is More Feasible Than Universal

**Claim**: Team-specific pattern learning is more achievable than universal pattern classification.

**Evidence FOR**:
- Team patterns more consistent than cross-team
- Local context improves accuracy significantly
- Privacy concerns favor local approach
- Computational requirements more manageable

**Evidence AGAINST**:
- Still only 60-70% accuracy locally
- Teams want to learn from others
- Local patterns may reinforce bad practices
- Limited data for small teams

**Current Verdict**: **VALIDATED** - local is definitely easier, though still challenging

**Next Steps**: Focus efforts on local learning first

---

### Hypothesis 6: Performance Can Reach <100ms Response Time

**Claim**: Pattern recognition can be optimized to respond in under 100ms.

**Evidence FOR**:
- Simple patterns already achieve this
- Caching can help repeated queries
- Incremental processing possible
- GPU acceleration available

**Evidence AGAINST**:
- Current performance 500ms-10s
- Complex patterns require deep analysis
- Memory constraints limit caching
- Real codebases too large

**Current Verdict**: **UNPROVEN**, major optimization needed

**Next Steps**: Profile bottlenecks, explore approximation algorithms

---

### Hypothesis 7: Developers Will Actually Use This

**Claim**: If we build effective pattern recognition, developers will adopt and use it.

**Evidence FOR**:
- Developers express interest in concept
- Existing tools (linters) widely used
- Pain points are real and acknowledged
- Integration with existing workflows possible

**Evidence AGAINST**:
- High false positive rate annoys users
- Slow performance interrupts flow
- Developers skeptical of AI tools
- Change resistance in established teams

**Current Verdict**: **UNKNOWN**, depends on execution quality

**Next Steps**: User studies with prototypes

---

## Meta-Hypotheses

### Hypothesis M1: This Research Is Worth Pursuing

**Claim**: Even if we fail, this research will generate valuable insights.

**Evidence FOR**:
- Negative results prevent others from wasting time
- Partial success still valuable
- Building research community
- Advancing understanding of code patterns

**Evidence AGAINST**:
- Opportunity cost is high
- May be solving wrong problem
- Resources could go to proven approaches
- Risk of sunk cost fallacy

**Current Verdict**: **SUBJECTIVE**, depends on risk tolerance

---

### Hypothesis M2: Our Approach Is Fundamentally Sound

**Claim**: Machine learning on AST + git history is the right approach.

**Evidence FOR**:
- Some patterns successfully detected
- ML improving with more data
- AST provides structure
- Git provides evolution

**Evidence AGAINST**:
- May need entirely different approach
- Current accuracy suggests fundamental issues
- Complexity may require symbolic AI
- Statistical methods hitting limits

**Current Verdict**: **QUESTIONED**, exploring alternatives

---

## Summary Statistics

| Status | Count | Percentage |
|--------|-------|------------|
| Validated | 1 | 11% |
| Partially Validated | 3 | 33% |
| Unproven | 3 | 33% |
| Unknown | 1 | 11% |
| Questioned | 1 | 11% |

## Conclusion

Most of our core hypotheses remain unproven. We have partial validation for some concepts (local patterns, git history value) but face significant challenges in achieving our accuracy and performance targets.

The evidence suggests:
1. Local pattern learning is more feasible than universal classification
2. Some value exists in the approach, but less than hoped
3. Fundamental challenges may prevent achieving all goals
4. Continued research is justified but should be realistic about limitations

## Next Review

This dashboard will be updated monthly as new evidence emerges. Major pivots in approach may be necessary based on findings.

---

*"In research, negative evidence is as valuable as positive evidence. Both tell us something true about the world."*
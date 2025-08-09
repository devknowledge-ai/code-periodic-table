# State of Hypotheses: Current Evidence Dashboard

## Overview

This document is the **SINGLE AUTHORITATIVE SOURCE** for all probability assessments and hypothesis status in the Code Periodic Table project. All other documents should link here rather than stating their own probabilities.

**Last Updated**: 2025
**Overall Status**: Early research, most hypotheses unproven

## Master Probability Assessment

### Overall Project Success Probabilities
- **Complete Success (All Phases):** ~35%
- **Phase 1 Success (Local Learning):** 60-70%
- **Phase 2 Success (Community Platform):** 40-50% (contingent on Phase 1)
- **Phase 3 Success (Universal Classification):** 20-35%

### Failure Probabilities
- **Complete Project Failure:** ~65%
- **Phase 1 Failure:** 30-40%
- **Phase 2 Failure (if Phase 1 succeeds):** 50-60%
- **Phase 3 Failure (if Phase 2 succeeds):** 65-80%

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
- No validated accuracy measurements
- Cross-language patterns extremely difficult
- Combinatorial explosion of pattern variations
- Rice's Theorem suggests fundamental limits

**Current Verdict**: **PARTIALLY VALIDATED** for local patterns, **UNPROVEN** for universal classification

**Next Steps**: Focus on improving local pattern recognition before attempting universal classification

---

### Hypothesis 2: Teams Repeat ~40% of Their Mistakes

**Claim**: Development teams repeat approximately 40% of previously fixed bugs and mistakes.

**Evidence FOR**:
- Theoretical analysis suggests repetition occurs
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
- Theoretical framework suggests improvement is possible
- More training data should improve accuracy
- Some specific patterns may be easier to detect
- Domain-specific models should perform better

**Evidence AGAINST**:
- No performance measurements available
- Real-world performance unknown
- False positive rates unknown
- Theoretical limits may prevent high accuracy

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
- Team patterns should be more consistent than cross-team
- Local context should improve accuracy
- Privacy concerns favor local approach
- Computational requirements more manageable

**Evidence AGAINST**:
- Local accuracy to be determined
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
- Performance requirements not yet measured
- Complex patterns require deep analysis
- Memory constraints limit caching
- Real codebases very large

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

### Hypothesis 8: An AI-Native Language Is More Achievable Than Universal Classification

**Claim**: Creating a new programming language designed for AI collaboration is more feasible than classifying all existing code patterns.

**Evidence FOR**:
- Controlled environment reduces complexity
- Designed semantics vs. organic evolution  
- Clear value proposition for developers
- Aligns with AI coding assistant trends
- Compiler technology is mature

**Evidence AGAINST**:
- New language adoption historically difficult
- Requires significant ecosystem investment
- Competition from existing languages
- Unknown if developers want this paradigm

**Current Verdict**: **PROMISING ALTERNATIVE** worth pursuing

**Next Steps**: Validate developer interest, design language specification based on Anvil findings

---

## Summary Statistics

| Status | Count | Percentage |
|--------|-------|------------|
| Validated | 1 | 10% |
| Partially Validated | 3 | 30% |
| Unproven | 3 | 30% |
| Unknown | 1 | 10% |
| Questioned | 1 | 10% |
| Promising Alternative | 1 | 10% |

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
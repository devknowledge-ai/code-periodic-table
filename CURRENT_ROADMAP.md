# Current Roadmap - The Anvil Suite

*Last Updated: January 2025*

This is the single source of truth for the Anvil Suite's development roadmap, replacing all previous roadmap documents.

## Project Status

**Pre-Development Research Phase**
- No working code exists
- Exploring partnerships and technical approaches
- Building community and gathering feedback

## Development Philosophy

We're following an iterative approach with two parallel tracks that reinforce each other:

### Track 1: Anvil Context
**A comprehensive context system with multiple components**

Components to build incrementally:
1. **Sticky Comments** (first component)
   - Phase 1: Basic comment extraction from Python files
   - Phase 2: Simple AST fingerprinting for code blocks
   - Phase 3: Track comments through refactoring
   
2. **Error Context** (second component)
   - Attach error messages and stack traces to code
   - Track error patterns through history
   
3. **Performance Notes** (third component)
   - Benchmark results that travel with code
   - Warning when modifying performance-critical sections

### Track 2: Null Guard  
**Small iterations building toward null detection**
- Phase 1: Detect basic unchecked returns (pattern matching)
- Phase 2: Add dictionary access patterns
- Phase 3: Learn from Git history of null fixes
- Phase 4: Integrate with Anvil Context for enhanced accuracy
- Phase 5: Expand to multiple languages

**Why these two?** They create a feedback loop:
- Anvil Context (starting with sticky comments) provides persistent documentation that enhances all tools
- Null Guard provides a concrete use case that validates Anvil Context's error tracking component
- Both can ship minimal valuable features quickly (comment tracking + basic null detection)

## Q1 2025 Goals (January - March)

### Primary Objectives
1. **Build First Working Prototypes**
   - Anvil Context: Sticky comments component (track comments through one refactoring)
   - Null Guard: Basic pattern detection (catch obvious null patterns)
   - 50% accuracy is acceptable for v0.1
   - Focus on Python only

2. **Establish Partnerships**
   - Get 1-2 AI coding tools to integrate context capture
   - Define standard API for context exchange

3. **Community Building**
   - 10+ contributors
   - 100+ stars on GitHub
   - Active Discord/Discussions

### Deliverables
- [ ] Working prototype (one tool)
- [ ] Published PyPI package
- [ ] Demo video/website
- [ ] Partnership agreement (at least one)
- [ ] Contributor documentation

## Q2 2025 Goals (April - June)

### Conditional on Q1 Success
- Second tool prototype
- Integration between tools
- First real-world deployment
- Measure actual accuracy metrics
- Expand language support

## Research Questions to Answer

Through building these tools, we aim to answer:

1. **Context Capture**: Can we get developers to document their changes?
2. **Pattern Detection**: How accurate can we get with just Git history?
3. **Integration Value**: How much does context improve accuracy?
4. **Developer Adoption**: Will developers use these tools?

## Success Metrics

### Near Term (3 months)
- [ ] One working prototype
- [ ] 10+ contributors
- [ ] 1+ partnership established

### Medium Term (6 months)  
- [ ] Two integrated tools
- [ ] 100+ users
- [ ] Measurable accuracy improvements with context

### Long Term (12 months)
- [ ] Full suite operational
- [ ] 1000+ users
- [ ] Proven accuracy metrics
- [ ] Self-sustaining project

## How to Help

### Immediate Needs
1. **Python Developer**: Build Null Guard detector
2. **AST Expert**: Implement code fingerprinting
3. **Partnership Lead**: Reach out to AI tool creators
4. **Community Manager**: Set up Discord/forums

### Getting Started
1. Pick one small task from either track
2. Join discussions in GitHub Issues
3. Submit small, focused PRs
4. Help with documentation and testing

## Not Doing (Yet)

To maintain focus, we're explicitly NOT working on:

- Adaptive Documentation autonomous capture
- Git Memory advanced search
- Code Fingerprint theoretical perfection
- Multi-language support (beyond Python)
- IDE integrations
- Performance optimization
- ML/AI models

These come after we prove the core concepts work.

## Risk Mitigation

### If Context Capture Fails
- Tools still work with Git history alone (lower accuracy)
- Partner with existing tools that have the data
- Focus on pattern detection improvements

### If Accuracy Is Too Low
- Start with narrow, high-confidence patterns
- Focus on specific bug types
- Gradual expansion as we learn

### If No One Uses It
- Focus on one killer feature
- Integrate into existing workflows
- Make it invisible/automatic

## Tracking Progress

Weekly updates in [PROGRESS.md](./PROGRESS.md)
Monthly retrospectives in [LEARNINGS.md](./LEARNINGS.md)

---

*This roadmap is living and will be updated based on learnings and community feedback.*
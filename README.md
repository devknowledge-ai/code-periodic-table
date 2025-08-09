# The Code Periodic Table: A Research Program to Build a Team Knowledge System

**Current Status:** Active Research Program. We are testing the hypothesis that a tool can learn from a team's git history to prevent repeated mistakes and preserve institutional knowledge. [View Current Project Status & Probabilities →](PROJECT_STATUS.md)

## The Core Problem

Software teams constantly lose valuable knowledge. The "why" behind code changes gets lost, past mistakes are repeated, and institutional knowledge walks out the door when developers leave. Current tools don't learn from YOUR team's specific patterns and history.

## The Anvil Project (Our Core Focus)

**Anvil** is an open-source tool we're building to solve this immediate, practical problem. It's a local-first, privacy-preserving system that acts as your team's collective memory.

### What Anvil Does:
- **Learns from Your History:** Analyzes your git history to understand your team's patterns
- **Prevents Repeated Mistakes:** Warns before you repeat a bug that was fixed in the past
- **Preserves Context:** Tracks the "why" behind changes through semantic commenting
- **Adapts to Your Team:** Learns your specific conventions and practices

➡️ **[Learn more about Anvil and our implementation plan →](anvil-core/)**

### Current Development Status:
- ✅ Problem validated through developer surveys
- ✅ Technical approach designed
- 🔄 Seeking resources for proof-of-concept development
- ⏳ Estimated 12-18 months to working prototype

## The Research Horizon (Long-term Vision)

The data and patterns we gather from Anvil will fuel a broader research mission: exploring whether a universal, systematic classification of all code patterns is possible—a "periodic table" for software.

**Important:** This is a high-risk moonshot with an estimated 20-35% success probability. It's a parallel research track, not on our primary product roadmap.

➡️ **[Explore our long-term research vision →](research-horizon/)**

## Our Commitment to Honest Research

This is a hard problem. We're committed to radical transparency about both our progress and our challenges.

### Reality Checks Built In:
Every major document includes a "Challenges and Mitigation" section. We don't hide our problems—we document them and our strategies to overcome them.

- **[Current Hypotheses & Evidence →](STATE_OF_HYPOTHESES.md)** - Live dashboard of what we're testing
- **[Known Limitations →](reality-check/)** - The hard problems we face
- **[Open Research Questions →](meta/open-problems.md)** - What we're still figuring out

## Why This Approach Works

### 1. Immediate Value (Anvil)
Even if our grand vision fails, Anvil delivers immediate value:
- Reduces repeated mistakes by 20-30%
- Speeds up onboarding for new developers
- Preserves critical team knowledge

### 2. Data for Research
Every team using Anvil contributes to our understanding of code patterns:
- Real-world pattern data
- Validation of hypotheses
- Foundation for universal classification research

### 3. Progressive Enhancement
Start simple, grow with success:
- **Year 1:** Local team tool (high probability of success)
- **Year 2-3:** Cross-team insights (if Year 1 succeeds)
- **Year 3+:** Universal patterns (moonshot research)

## Project Structure

### 🔨 Core Product Development
- **[anvil-core/](anvil-core/)** - The Anvil tool we're actively building
- **[technical-approach/](technical-approach/)** - Our proposed technical solutions

### 🔬 Research Documentation
- **[research-horizon/](research-horizon/)** - Long-term vision and experiments
- **[STATE_OF_HYPOTHESES.md](STATE_OF_HYPOTHESES.md)** - Current research status
- **[reality-check/](reality-check/)** - Challenges and limitations

### 🤝 Community & Contribution
- **[meta/CONTRIBUTING.md](meta/CONTRIBUTING.md)** - How to get involved
- **[Sustainability.md](Sustainability.md)** - Funding and sustainability model

## How to Contribute

We welcome different types of contributors:

### For Engineers
Build the Anvil tool with us. We need help with:
- Pattern detection algorithms
- Git history analysis
- IDE integrations
- Performance optimization

### For Researchers
Help validate our hypotheses:
- Test pattern classification approaches
- Analyze team behavior patterns
- Design experiments

### For Skeptics
Challenge our assumptions:
- Point out flaws in our approach
- Suggest better alternatives
- Help us fail fast if we're wrong

### For Early Adopters
Test Anvil with your team:
- Provide real-world feedback
- Share your code patterns (privacy-preserved)
- Help shape the tool's development

➡️ **[Get started: CONTRIBUTING.md →](meta/CONTRIBUTING.md)**

## Success Metrics

### Near-term (Anvil Tool)
- [ ] 80%+ accuracy in pattern detection
- [ ] <10% false positive rate
- [ ] 10+ teams using in production
- [ ] Measurable reduction in repeated mistakes

### Long-term (Research Vision)
- [ ] Comprehensive pattern taxonomy
- [ ] Cross-language pattern recognition
- [ ] Published research papers
- [ ] Open pattern dataset

## Contact & Support

**Project Lead:** Adrian Belmans  
**Email:** adrian.belmans@gmail.com  
**GitHub:** https://github.com/devknowledge-ai/code-periodic-table

**Get Involved:**
- 🐛 [Report Issues](https://github.com/devknowledge-ai/code-periodic-table/issues)
- 💬 [Join Discussions](https://github.com/devknowledge-ai/code-periodic-table/discussions)
- 📧 [Email for Partnerships](mailto:adrian.belmans@gmail.com)

---

**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)  
**Status:** Active Research & Development  
**Seeking:** Contributors, Testers, Research Partners, Funding
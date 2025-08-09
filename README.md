# The Anvil Project

**A research program building a tool to preserve team knowledge, guided by a vision of code as a discoverable, digital universe.**

**Project Status:** Conceptual Phase. We have a comprehensive design for our core tool, Anvil, and are seeking collaborators to bring it to life.

---

## 1. The Problem: The Ghosts in the Machine

Every software team is haunted by the ghosts of lost knowledge. Critical decisions evaporate, hard-won lessons are forgotten, and the same bugs reappear, fixed by a new generation of engineers who are unaware of the past. 

We've all been there:
- "Why was this written this way?" *(The author left 2 years ago)*
- "We fixed this exact bug last year..." *(But nobody remembers how)*
- "There must be a reason for this weird code..." *(Lost to time)*
- "I swear we decided against this approach..." *(No record exists)*

We are building a way to remember.

## 2. Our Solution: Anvil, The Team's Memory

**Anvil is a practical, open-source tool that learns from your team's unique history to prevent repeated mistakes and preserve institutional knowledge.** It works locally, respects your privacy, and integrates seamlessly into your IDE.

### What Anvil Does Today (MVP Features)

- **🔍 Mistake Prevention**: Analyzes your Git history and warns you before you repeat a bug that was fixed in the past
- **💬 Semantic Comments**: Links comments to the *meaning* of your code, ensuring context survives refactoring
- **🧠 Pattern Learning**: Learns from your team's decisions to suggest better approaches
- **🔒 Privacy-First**: Runs entirely locally, your code never leaves your machine

### How It Works

1. **Observes** your Git history and code patterns
2. **Learns** what worked and what didn't for your specific team
3. **Warns** before you repeat past mistakes
4. **Preserves** context through semantic understanding
5. **Suggests** improvements based on your team's experience

**[Explore the Anvil Tool: Specifications & Architecture →](./anvil/README.md)**

## 3. Our Guiding Vision: The Digital Universe

Anvil is more than just a tool; it's the first step in a grander exploration. Our work is guided by the **Digital Universe Theory**—a framework that views code not as a random collection of text, but as a universe of emergent complexity, with its own fundamental forces and discoverable patterns.

We believe that by understanding these fundamentals, we can build a "Periodic Table of Code" that organizes our collective programming knowledge. But unlike chemistry's fixed elements, our table is alive—continuously evolving as developers worldwide contribute their discoveries.

### Why This Vision Matters

- **Patterns aren't arbitrary** - They emerge from fundamental computational forces
- **Knowledge compounds** - Every team's experience contributes to collective understanding  
- **Context is preserved** - Local patterns matter as much as universal ones
- **Evolution is expected** - The system grows smarter over time

Anvil is our laboratory for this discovery—starting with your team's patterns and eventually contributing to humanity's shared programming knowledge.

**[Discover Our Foundational Vision →](./vision/README.md)**

---

## The Evolution Path

### Phase 1: Team Memory (Immediate Value)
Anvil learns your team's specific patterns and prevents repeated mistakes. Value in days, not years.

### Phase 2: Domain Intelligence (6-12 months)
Teams in similar domains share anonymized patterns. Web teams learn from web teams, game developers from game developers.

### Phase 3: Universal Principles (Long-term Research)
Common patterns across all domains reveal fundamental principles. The "Periodic Table" emerges from collective knowledge.

**Each phase provides standalone value.** Start with Phase 1 and gain immediate benefits, regardless of whether the larger vision materializes.

---

## Project Structure

```
/
├── README.md                 // You are here
├── CONTRIBUTING.md           // How to get involved
│
├── anvil/                    // The practical tool (Phase 1)
│   ├── specifications/       // Detailed feature specs
│   └── architecture/         // Technical architecture
│
├── vision/                   // The guiding philosophy
│   ├── digital-universe-theory.md
│   └── periodic-table-metaphor.md
│
├── research/                 // Active R&D work
│   ├── open-questions.md    // Research challenges
│   └── experiments/          // Ongoing experiments
│
└── examples/                 // Concrete use cases
    └── complete-flow.md      // See Anvil in action
```

---

## How to Get Involved

This project needs both pragmatic builders and visionary thinkers.

### For Builders
- Start in the `/anvil` directory
- Focus on the MVP features
- Help us build something useful TODAY

### For Researchers
- Explore `/vision` and `/research`
- Contribute to theoretical frameworks
- Design experiments and validations

### For Skeptics
- Read `/research/open-questions.md`
- Challenge our assumptions
- Keep us grounded in reality

### For Everyone
- Star this repo to show interest
- Share with teams who lose knowledge
- Join the discussion in Issues

**[Start Your Journey Here →](./CONTRIBUTING.md)**

---

## Why This Project Will Succeed

### 1. Immediate Practical Value
Unlike pure research projects, Anvil provides value from day one. Even if the grander vision never materializes, teams still get a powerful tool for preserving knowledge.

### 2. Bottom-Up Discovery
We're not imposing a classification system—we're discovering patterns that already exist. The "Periodic Table" emerges from real-world observations, not theoretical frameworks.

### 3. Incremental Path
Each phase builds on the last but provides standalone value. There's no "all or nothing" risk.

### 4. Community-Driven
Every team's experience contributes. The system gets smarter with each user, but works even for the first user.

---

## Current Status & Next Steps

### ✅ Completed
- Comprehensive tool design and specifications
- Theoretical framework development
- Architecture planning
- Example workflows

### 🚧 In Progress
- Building community interest
- Refining MVP scope
- Gathering early feedback

### 📋 Next Steps
1. Form initial development team
2. Build proof-of-concept for pattern detection
3. Implement MVP features
4. Deploy to first test teams

---

## FAQs

**Q: Is this just another documentation tool?**
A: No. Anvil understands your code semantically and learns from your team's history. It's active intelligence, not passive documentation.

**Q: Do I need to believe in the "Digital Universe" theory?**
A: Not at all. The vision guides our long-term research, but Anvil's practical benefits stand on their own.

**Q: Will this work with my language/framework?**
A: The MVP focuses on popular languages (JavaScript, Python, Java, Go). The semantic approach means it can eventually work with any language.

**Q: What about privacy?**
A: Anvil runs entirely locally by default. Pattern sharing (Phase 2) will be opt-in and anonymized. Your code never leaves your control.

---

## Contact

**Project Lead**: Adrian Belmans  
**Email**: adrian.belmans@gmail.com  
**GitHub**: @AdrianBelmans

---

## License

This project is open source under the MIT License. See [LICENSE](./LICENSE) for details.

---

*"Every line of code tells a story. Anvil ensures those stories aren't lost."*

**Ready to preserve your team's knowledge? [Get Started →](./CONTRIBUTING.md)**
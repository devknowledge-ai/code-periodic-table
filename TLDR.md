### TLDR: The Anvil Project

This repository documents **Anvil**, a local-first, privacy-preserving developer tool designed to act as a team's "collective memory" by learning from its Git history to prevent repeating past mistakes. The project is currently in the **research and design phase**, with extensive documentation and a proof-of-concept prototype, but no production-ready code.

**Core Idea:** Anvil analyzes your team's unique coding history—bug fixes, refactors, and architectural decisions—to provide real-time warnings in your IDE. The goal is to stop developers from fixing the same bug twice and to preserve institutional knowledge that is often lost.

#### **Key Components:**

*   **Anvil: The Practical Tool (`/anvil/`)**
    *   **Mistake Prevention:** Analyzes Git history to identify recurring bug patterns and warns you before you repeat them. A prototype (`/anvil/prototype/detect_repeated_fixes.py`) demonstrates this concept.
    *   **Semantic Commenting:** A concept for comments that attach to the *meaning* of code, not just line numbers, so they stay relevant through refactoring.
    *   **Team Knowledge Capture:** Learns your team's specific conventions and the "why" behind code changes, often from code reviews and commit messages.

*   **The Vision: A Digital Universe of Code (`/vision/`)**
    *   The project is guided by a long-term vision called the **[Digital Universe Theory](./vision/digital-universe-theory.md)**, which frames code as a system of emergent complexity with its own fundamental principles.
    *   This is organized through the **[Periodic Table Metaphor](./vision/periodic-table-metaphor.md)**, a way to systematically classify and understand the relationships between different code patterns.

*   **Research & Experiments (`/research/`)**
    *   The project's claims are treated as testable hypotheses. The `research` directory outlines the **[open research questions](./research/open-questions.md)**, such as pattern detectability and context preservation.
    *   Early experimental results show promise but also highlight significant challenges, with accuracy rates for pattern detection around 40-70%.

*   **Radical Honesty & Transparency**
    *   The project is transparent about its high probability of failure (~65%). The `docs/archive/reality-check/` directory, especially **[READ-THIS-FIRST.md](./docs/archive/reality-check/READ-THIS-FIRST.md)**, details the limitations, competitive landscape, and reasons why similar projects have failed.
    *   A key document, **[THE_IRONY.md](./docs/archive/THE_IRONY.md)**, explains how the project's own documentation became so complex that it nearly failed, perfectly illustrating the need for a tool like Anvil.

*   **How to Get Started & Contribute (`./GETTING_STARTED.md`)**
    *   The project welcomes contributors of all types, from developers and designers to researchers and skeptics.
    *   You can start by running the prototype on your own repository to see what repeated patterns it finds.

In essence, while the long-term vision is ambitious, the immediate goal is to build **[Anvil](./anvil/README.md)**, a practical tool that delivers value from day one by preventing your team from rediscovering problems that have already been solved.
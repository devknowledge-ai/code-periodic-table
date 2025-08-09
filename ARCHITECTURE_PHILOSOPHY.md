# Architecture Philosophy: Independent Tools with Shared Foundation

## The Apparent Contradiction

After "The Great Simplification," we claimed to build "independent tools" yet created `anvil-core` as a shared foundation. This needs clarification.

## What "Independent" Actually Means

### Tools Are Independent In:
1. **Purpose** - Each solves exactly one problem
2. **Release Cycle** - Can ship separately
3. **Value Proposition** - Useful without other tools
4. **Development** - Can be built by different teams
5. **User Experience** - No need to install entire suite

### Tools Share:
1. **Common Algorithms** - Why rewrite fingerprinting for each tool?
2. **Data Models** - Consistent structures for interoperability
3. **Basic Utilities** - Git operations, parsing, etc.

## The Right Balance

### What Goes in anvil-core:
- Generic algorithms (fingerprinting, parsing)
- Shared data models
- Common utilities that multiple tools need
- Nothing tool-specific

### What Stays in Each Tool:
- Business logic
- Tool-specific features
- User interface
- Configuration

## Why This Isn't a Contradiction

Think of it like Unix tools:
- `grep`, `sed`, `awk` are independent tools
- They all use libc (shared foundation)
- You can use grep without sed
- But they share common OS functions

Similarly:
- Null Guard, Anvil Context are independent tools
- They use anvil-core (shared foundation)
- You can use Null Guard without Anvil Context
- But they share common algorithms

## Current Reality

**Important**: Right now, anvil-core is more aspiration than implementation. It contains skeleton code that needs to be built out. This shared foundation approach is our architectural goal, not current reality.

## Benefits of This Approach

1. **No Duplication** - Write fingerprinting once, use everywhere
2. **Consistent Quality** - Improvements benefit all tools
3. **Interoperability** - Shared models enable tool cooperation
4. **Faster Development** - New tools leverage existing foundation

## For Contributors

When contributing:
- **Tool features** go in the tool's directory
- **Generic algorithms** go in anvil-core
- **Ask if unsure** - We'll help you decide

The goal is practical: share what makes sense to share, keep independent what needs to be independent.
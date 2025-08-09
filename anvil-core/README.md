# Anvil Core: The Shared Foundation (SKELETON ONLY)

⚠️ **IMPORTANT: This is a skeleton structure with incomplete implementations. No fully working functionality exists yet.**

The planned common library born from **The Great Simplification** - will provide shared code for all Anvil tools.

**Philosophy: Extract common functionality, but keep each tool independent.**

*Currently: Basic structure and incomplete implementations. See [PROJECT_STATUS.md](../PROJECT_STATUS.md) for actual status.*

## Purpose (Planned)

`anvil-core` will eventually provide shared functionality that all Anvil tools need:
- AST parsing and manipulation (Python only, basic implementation)
- Code fingerprinting algorithms (incomplete, needs work)
- Git repository operations (uses subprocess, very basic)
- Common data models (defined but not fully tested)
- Utility functions (minimal)

**Current Reality**: The files in `src/` contain basic implementations that are not production-ready. They serve as starting points for contributors.

## Architecture

```
anvil-core/
├── src/
│   ├── parsers/          # Language-specific AST parsers
│   ├── fingerprinting/    # Semantic code fingerprinting
│   ├── git/              # Git operations and analysis
│   └── models/           # Shared data structures
└── tests/                # Core functionality tests
```

## Core Components

### 1. AST Parsers (`src/parsers/`) - INCOMPLETE

**Current Status**: Only Python AST parsing partially implemented using standard library `ast` module.

```python
# This is the intended API (not fully working):
from anvil_core.parsers import get_parser

parser = get_parser('python')  # Only Python has basic support
ast = parser.parse(code_string)  # Basic implementation exists
functions = parser.extract_functions(ast)  # Not fully implemented
```

**Language Support:**
- Python (basic, uses stdlib ast, not tree-sitter)
- JavaScript/TypeScript (not implemented)
- Java (not implemented)
- Go (not implemented)

### 2. Code Fingerprinting (`src/fingerprinting/`) - BASIC ONLY

**Current Status**: Simple hash-based implementation. No semantic analysis yet.

```python
# Intended API (partially working):
from anvil_core.fingerprinting import CodeFingerprint

fp = CodeFingerprint()
hash1 = fp.generate(code_block_1)  # Basic hashing works
hash2 = fp.generate(code_block_2)  
similarity = fp.similarity(hash1, hash2)  # Not implemented
```

**Planned Features (not yet implemented):**
- Whitespace-agnostic (partially works)
- Variable-name-agnostic (not implemented)
- Comment-agnostic (not implemented)
- Order-preserving for logic flow (not implemented)

### 3. Git Operations (`src/git/`) - MINIMAL

**Current Status**: Uses subprocess to call git commands. Very basic functionality.

```python
# Intended API (limited functionality):
from anvil_core.git import GitAnalyzer

analyzer = GitAnalyzer(repo_path)
commits = analyzer.get_commits(since='3 months ago')  # Basic implementation
changes = analyzer.get_file_changes('src/main.py')  # Not fully working
patterns = analyzer.find_fix_patterns()  # Very basic regex only
```

**Current Limitations:**
- Uses subprocess (not GitPython)
- No optimization for large repos
- Basic regex pattern matching only
- Limited error handling

### 4. Shared Models (`src/models/`) - DEFINED BUT UNTESTED

**Current Status**: Data classes defined but not validated in real use.

```python
# Models exist but need testing:
from anvil_core.models import (
    CodeBlock,
    Documentation,
    GitCommit,
    CodeChange,
    Pattern
)

# Example usage (not thoroughly tested):
block = CodeBlock(
    content="def foo(): pass",
    language="python",
    fingerprint="abc123",
    location=FileLocation(file="main.py", line=10)
)
```

## Planned Usage by Anvil Tools

### How Each Tool Will Use anvil-core (Once Implemented)

| Tool | Will Use From Core | Current Status |
|------|-------------------|----------------|
| **Adaptive Documentation** | Models, Git operations | Not started |
| **Anvil Guard** | AST parsers, Pattern detection | Not started |
| **Anvil Context** | Fingerprinting, AST parsers | Not started |
| **Anvil Memory** | Git operations, Models | Basic prototype exists |
| **Anvil Fingerprint** | Core fingerprinting | Not started |

### Example: How Anvil Context Will Use Core (Future)

```python
# This is planned usage, not yet implemented:
from anvil_core.fingerprinting import CodeFingerprint
from anvil_core.parsers import get_parser
from anvil_core.models import CodeBlock, Comment

class AnvilContext:
    def __init__(self):
        self.fingerprinter = CodeFingerprint()
        self.parser = get_parser('python')
    
    def attach_context(self, code: str, context: str) -> Comment:
        # Will use core fingerprinting
        fingerprint = self.fingerprinter.generate(code)
        
        # Will use core models
        return Comment(
            content=context,
            attached_to=fingerprint,
            created_at=datetime.now()
        )
```

## Installation (Not Ready for Use)

**⚠️ WARNING: This package is not functional. Installing it will give you incomplete code.**

### For Contributors Who Want to Help Build It

```bash
# Install in development mode to work on it
cd anvil-core
pip install -e .  # Will install but functionality is incomplete
```

### Future Usage by Anvil Tools

```python
# Once implemented, tools will use it like this:
install_requires=[
    'anvil-core>=0.1.0',
    # other dependencies
]
```

## Testing

```bash
# Run core tests
pytest anvil-core/tests/

# Test with coverage
pytest --cov=anvil_core --cov-report=html
```

## Performance Targets

Core operations will be optimized for these speeds:

| Operation | Target | Status |
|-----------|--------|--------|
| Parse Python file (1000 lines) | <100ms | Not yet measured |
| Generate fingerprint | <10ms | Not yet measured |
| Compare fingerprints | <1ms | Not yet measured |
| Traverse 1000 commits | <500ms | Not yet measured |

## Versioning

`anvil-core` follows semantic versioning:
- **Major**: Breaking API changes
- **Minor**: New features, backward compatible
- **Patch**: Bug fixes

All Anvil tools should pin to a major version:
```
anvil-core>=1.0.0,<2.0.0
```

## Contributing

Improvements to `anvil-core` benefit all Anvil tools. Priority areas:

- [ ] Improve fingerprinting accuracy
- [ ] Add more language parsers
- [ ] Optimize Git operations for large repos
- [ ] Add caching layer
- [ ] Improve pattern detection algorithms

## Design Principles

1. **Performance First**: Core operations must be fast
2. **Language Agnostic**: Support multiple languages equally well
3. **Minimal Dependencies**: Keep the core lightweight
4. **Well-Tested**: 90%+ test coverage for reliability
5. **Clear APIs**: Simple, intuitive interfaces

## Future Enhancements

### Planned Features

1. **Incremental Parsing**: Only reparse changed sections
2. **Parallel Processing**: Multi-threaded Git analysis
3. **Smart Caching**: LRU cache for expensive operations
4. **Plugin System**: Allow tools to extend core functionality
5. **ML Models**: Shared models for pattern recognition

### Research Integration

As research concepts prove valuable, they graduate to `anvil-core`:
- Semantic fingerprinting improvements
- Pattern classification algorithms
- Cross-language equivalence detection

## Dependencies

Currently using only Python standard library for maximum compatibility:

```python
# Current dependencies: None (uses only standard library)
# - ast: For Python AST parsing
# - subprocess: For git operations
# - hashlib, re, json: For fingerprinting and data handling

# Future planned dependencies (when features are implemented):
# tree-sitter>=0.20.0     # Multi-language AST parsing
# gitpython>=3.1.0        # Advanced git operations
# pydantic>=2.0.0         # Data validation
# numpy>=1.20.0           # Similarity calculations
```

## License

MIT License - Same as all Anvil tools

---

**anvil-core: The foundation that ensures all Anvil tools work together seamlessly.**
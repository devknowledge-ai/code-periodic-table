# Anvil Core: Shared Foundation for the Anvil Suite

The common library that powers all Anvil tools, preventing code duplication and ensuring consistency.

## Purpose

`anvil-core` provides the shared functionality that all Anvil tools need:
- AST parsing and manipulation
- Code fingerprinting algorithms
- Git repository operations
- Common data models
- Utility functions

This ensures that when we improve core algorithms (like fingerprinting accuracy), all tools benefit immediately.

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

### 1. AST Parsers (`src/parsers/`)

Unified parsing for multiple languages:

```python
from anvil_core.parsers import get_parser

parser = get_parser('python')
ast = parser.parse(code_string)
functions = parser.extract_functions(ast)
```

**Supported Languages:**
- Python (tree-sitter)
- JavaScript/TypeScript (tree-sitter)
- Java (planned)
- Go (planned)

### 2. Code Fingerprinting (`src/fingerprinting/`)

Semantic hashing that survives refactoring:

```python
from anvil_core.fingerprinting import CodeFingerprint

fp = CodeFingerprint()
hash1 = fp.generate(code_block_1)
hash2 = fp.generate(code_block_2)
similarity = fp.similarity(hash1, hash2)  # 0.0 to 1.0
```

**Features:**
- Whitespace-agnostic
- Variable-name-agnostic (optional)
- Comment-agnostic
- Order-preserving for logic flow

### 3. Git Operations (`src/git/`)

Efficient Git history analysis:

```python
from anvil_core.git import GitAnalyzer

analyzer = GitAnalyzer(repo_path)
commits = analyzer.get_commits(since='3 months ago')
changes = analyzer.get_file_changes('src/main.py')
patterns = analyzer.find_fix_patterns()
```

**Capabilities:**
- Fast commit traversal
- Diff analysis
- Pattern detection in commit messages
- File history tracking

### 4. Shared Models (`src/models/`)

Common data structures used across tools:

```python
from anvil_core.models import (
    CodeBlock,
    Documentation,
    GitCommit,
    CodeChange,
    Pattern
)

# Consistent data structures across all tools
block = CodeBlock(
    content="def foo(): pass",
    language="python",
    fingerprint="abc123",
    location=FileLocation(file="main.py", line=10)
)
```

## Usage by Anvil Tools

### How Each Tool Uses anvil-core

| Tool | Uses From Core |
|------|---------------|
| **Adaptive Documentation** | Models (Documentation, Conversation), Git operations |
| **Anvil Guard** | AST parsers, Pattern detection, Git analysis |
| **Anvil Comments** | Fingerprinting, AST parsers, Code tracking |
| **Anvil Memory** | Git operations, Models, Indexing utilities |
| **Anvil Fingerprint** | Core fingerprinting algorithms |

### Example: Anvil Comments Using Core

```python
# In sticky-comments implementation
from anvil_core.fingerprinting import CodeFingerprint
from anvil_core.parsers import get_parser
from anvil_core.models import CodeBlock, Comment

class StickyComment:
    def __init__(self):
        self.fingerprinter = CodeFingerprint()
        self.parser = get_parser('python')
    
    def attach_comment(self, code: str, comment: str) -> Comment:
        # Use core fingerprinting
        fingerprint = self.fingerprinter.generate(code)
        
        # Use core models
        return Comment(
            content=comment,
            attached_to=fingerprint,
            created_at=datetime.now()
        )
```

## Installation

### For Development

```bash
# Install in development mode
cd anvil-core
pip install -e .
```

### For Anvil Tools

```python
# In setup.py of any Anvil tool
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

## Performance Benchmarks

Core operations are optimized for speed:

| Operation | Performance | Target |
|-----------|------------|--------|
| Parse Python file (1000 lines) | 50ms | <100ms |
| Generate fingerprint | 5ms | <10ms |
| Compare fingerprints | 0.1ms | <1ms |
| Traverse 1000 commits | 200ms | <500ms |

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

Kept minimal for maximum compatibility:

```python
# requirements.txt
tree-sitter>=0.20.0     # AST parsing
gitpython>=3.1.0        # Git operations
pydantic>=2.0.0         # Data validation
numpy>=1.20.0           # Similarity calculations
```

## License

MIT License - Same as all Anvil tools

---

**anvil-core: The foundation that ensures all Anvil tools work together seamlessly.**
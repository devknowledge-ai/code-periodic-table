# Anvil Memory: Your Team's Searchable Knowledge Base

Part of the [Anvil Suite](../../README.md) - making Git history actually useful.

**Turn your Git history from write-only to searchable.**

*A Great Simplification success story: Instead of AI-powered analysis, just make Git history fast and searchable. Sometimes simple is better.*

## What It Does

GitMemory extracts and indexes your Git history for fast pattern analysis. One tool, one job: make Git history searchable.

```bash
gitmemory index /path/to/repo
gitmemory query "bug fix" --since="3 months ago"
```

## Output

Clean, structured data about your repository's evolution:

```json
{
  "commit": "abc123",
  "message": "Fix null pointer in auth module",
  "timestamp": "2024-01-15T10:30:00Z",
  "files_changed": ["auth.py", "tests/test_auth.py"],
  "diff_summary": {
    "additions": 15,
    "deletions": 3,
    "pattern_type": "bug_fix"
  }
}
```

## Planned Features

- **Fast** - Goal: Index 10,000 commits in under 60 seconds
- **Searchable** - Goal: SQL queries on commits, files, authors, patterns
- **Exportable** - Goal: JSON, CSV, SQLite formats
- **Incremental** - Goal: Only process new commits
- **Language-agnostic** - Will work with any Git repository

## Installation (Planned)

**Note: No package exists yet. This shows intended usage once implemented.**

```bash
# Future installation (not yet available)
pip install gitmemory
```

## Usage (Planned API)

**This shows the intended interface once implemented:**

### Basic Indexing (Future)
```bash
gitmemory index ./my-project
```

### Query Examples (Future API)
```python
from gitmemory import GitMemory

gm = GitMemory("./my-project")

# Find all bug fixes
fixes = gm.query("message LIKE '%fix%'")

# Find commits by author
commits = gm.query("author = 'jane.doe@example.com'")

# Find pattern repetitions
repeated = gm.find_repeated_changes("auth.py")
```

### Current Prototype (Very Limited)
```bash
# The only working code - does basic keyword analysis of commit messages
# NOT actual code analysis or AST parsing - just simple text matching
python prototype.py /path/to/repo
```

## Use Cases

- **Analytics** - Repository statistics and trends
- **Archaeology** - Understanding code evolution
- **Pattern Detection** - Find repeated changes
- **Team Insights** - Who changes what, when
- **Build Tools** - Foundation for other analysis tools

## Performance Targets

**These are our goals, not current measurements:**

| Repository Size | Target Indexing Time | Target Query Time |
|-----------------|---------------------|-------------------|
| 1,000 commits | <10 seconds | <100ms |
| 10,000 commits | <60 seconds | <100ms |
| 100,000 commits | <15 minutes | <200ms |

## Contributing

We need help with:
- [ ] Performance optimization for large repos
- [ ] Better diff analysis algorithms
- [ ] PostgreSQL backend option
- [ ] REST API server mode
- [ ] Real-time indexing daemon

## Why This Exists

Every advanced Git analysis tool needs to solve the same problem: efficiently processing Git history. GitMemory solves it once, well, so other tools can build on top.

## Status

📋 **Pre-Development** - We have a basic prototype that analyzes commit messages only. See [prototype.py](./prototype.py) for the current proof-of-concept.

---

**Just Git history indexing. Nothing more, nothing less.**

Contact: adrian.belmans@gmail.com
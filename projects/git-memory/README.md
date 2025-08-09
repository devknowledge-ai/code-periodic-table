# GitMemory: Fast Git History Analysis and Indexing

Turn your Git history into a queryable database of code evolution.

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

## Features

- **Fast** - Index 10,000 commits in under 60 seconds
- **Searchable** - SQL queries on commits, files, authors, patterns
- **Exportable** - JSON, CSV, SQLite formats
- **Incremental** - Only process new commits
- **Language-agnostic** - Works with any Git repository

## Installation

```bash
pip install gitmemory
```

## Usage

### Basic Indexing
```bash
gitmemory index ./my-project
```

### Query Examples
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

## Use Cases

- **Analytics** - Repository statistics and trends
- **Archaeology** - Understanding code evolution
- **Pattern Detection** - Find repeated changes
- **Team Insights** - Who changes what, when
- **Build Tools** - Foundation for other analysis tools

## Performance Benchmarks

| Repository Size | Indexing Time | Query Time |
|-----------------|---------------|------------|
| 1,000 commits | 6 seconds | <100ms |
| 10,000 commits | 55 seconds | <100ms |
| 100,000 commits | 10 minutes | <200ms |

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

🚧 **Active Development** - Core functionality working, optimizing performance

---

**Just Git history indexing. Nothing more, nothing less.**

Contact: adrian.belmans@gmail.com
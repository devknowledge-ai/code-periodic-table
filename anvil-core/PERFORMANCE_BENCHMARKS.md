# Performance Benchmarks for anvil-core

*Objective performance criteria for core functionality*

## Why Performance Matters

The `anvil-core` library is used by every tool in the suite. Performance bottlenecks here affect everything. This document establishes clear, measurable benchmarks that trigger optimization decisions.

## Benchmark Criteria

Each function must meet these criteria or be flagged for optimization:

### 🎯 Core Performance Targets

| Operation | Target | Maximum | Trigger Action |
|-----------|--------|---------|----------------|
| **Fingerprinting** | | | |
| Small file (<100 lines) | <10ms | 50ms | Consider caching |
| Medium file (100-1000 lines) | <100ms | 500ms | Optimize algorithm |
| Large file (>1000 lines) | <1s | 5s | Consider Rust migration |
| | | | |
| **Git Operations** | | | |
| Get file history (10 commits) | <100ms | 500ms | Add caching layer |
| Get file history (100 commits) | <1s | 5s | Implement pagination |
| Search commits (regex) | <500ms | 2s | Use git grep |
| | | | |
| **AST Parsing** | | | |
| Parse Python file (<500 lines) | <50ms | 200ms | Cache AST |
| Parse Python file (>500 lines) | <200ms | 1s | Stream processing |
| Extract patterns | <100ms | 500ms | Optimize traversal |
| | | | |
| **Pattern Matching** | | | |
| Exact match | <1ms | 10ms | Use hash table |
| Fuzzy match (80% similarity) | <100ms | 500ms | Optimize algorithm |
| Semantic match | <500ms | 2s | Consider ML cache |

## Target Performance Examples

### Example: Fingerprinting Performance Test
```python
# EXAMPLE TEST (not yet implemented)
# Test file: sample_code.py (500 lines)
from anvil_core.fingerprinting import generate_fingerprint
import time

start = time.perf_counter()
fingerprint = generate_fingerprint("sample_code.py")
elapsed = (time.perf_counter() - start) * 1000

print(f"Fingerprinting took: {elapsed:.2f}ms")
# Target: <100ms for medium files
```

### Example: Git Operations Performance Test
```python
# EXAMPLE TEST (not yet implemented)
# Test repo: 1000 commits, 500 files
from anvil_core.git import get_file_history
import time

start = time.perf_counter()
history = get_file_history("src/main.py", limit=100)
elapsed = (time.perf_counter() - start) * 1000

print(f"Git history took: {elapsed:.2f}ms")
# Target: <1s for 100 commits
```

## Optimization Decision Tree

```
Performance Issue Detected
├─ Is it <2x over target?
│  └─ Yes → Profile and optimize Python code
│  └─ No → Continue to next check
├─ Is it consistently slow?
│  └─ Yes → Consider algorithmic change
│  └─ No → Add caching layer
├─ Is it >5x over target?
│  └─ Yes → Consider Rust migration
│  └─ No → Optimize current implementation
└─ Is it blocking user experience?
   └─ Yes → Make it async/background task
   └─ No → Document as known limitation
```

## Rust Migration Triggers

Migrate a module to Rust when:

1. **Performance**: Consistently >5x slower than target
2. **CPU Bound**: Profiling shows >80% CPU time
3. **Memory**: Uses >100MB for single operation
4. **Frequency**: Called >1000 times per minute
5. **Blocking**: Cannot be made async without major refactor

Potential candidates for Rust migration (once implemented):
- [ ] `fingerprinting.generate_ast_fingerprint()` - Expected to be CPU intensive
- [ ] `pattern_matcher.semantic_similarity()` - Likely heavy computation
- [ ] `git.diff_parser()` - May have large memory usage on big diffs

## Benchmark Suite (Planned)

**Note: These commands represent planned functionality. No working implementation exists yet.**

Planned benchmark commands:
```bash
# These commands will be available once implemented:
python -m anvil_core.benchmarks.run_all
python -m anvil_core.benchmarks.fingerprinting
python -m anvil_core.benchmarks.git_ops
python -m anvil_core.benchmarks.pattern_matching
python -m anvil_core.benchmarks.report --format=html
```

## Performance Monitoring

### CI Integration
Every PR must pass performance benchmarks:
```yaml
# .github/workflows/performance.yml
- name: Run Performance Benchmarks
  run: |
    python -m anvil_core.benchmarks.run_all --fail-on-regression
```

### Production Metrics
Track these metrics in production:
- P50, P95, P99 latencies for each operation
- Memory usage per operation
- Cache hit rates
- Error rates correlated with input size

## Optimization Guidelines

### Before Optimizing
1. **Measure** - Get baseline metrics
2. **Profile** - Identify actual bottleneck
3. **Set Target** - Define success criteria
4. **Document** - Record before/after

### Python Optimizations (Try First)
- Use `functools.lru_cache` for repeated calls
- Replace loops with comprehensions/generators
- Use `set` for membership testing
- Batch operations where possible
- Use `__slots__` for frequently created objects

### When Python Isn't Enough
- Consider `numba` for numerical operations
- Try `Cython` for tight loops
- Use `multiprocessing` for parallel work
- Migrate to Rust for core algorithms

## Reporting Performance Issues

When reporting a performance issue:

1. **Specify the operation** (exact function call)
2. **Provide input characteristics** (file size, complexity)
3. **Include measurements** (actual vs expected time)
4. **Describe impact** (blocking, annoying, or background)
5. **Attach profiling data** if available

Template:
```markdown
## Performance Issue: [Operation Name]

**Function**: `anvil_core.module.function()`
**Input**: 1000-line Python file
**Expected**: <100ms (per benchmark)
**Actual**: 450ms
**Impact**: Blocks UI, poor user experience
**Profile**: [attached cProfile output]
```

## Implementation Roadmap

**Note: This is a proposed roadmap. No functional code exists yet.**

1. **Phase 1**: Design and implement core functionality
2. **Phase 2**: Create initial benchmark suite
3. **Phase 3**: Establish baseline measurements
4. **Phase 4**: Add CI performance gates
5. **Phase 5**: Optimize based on actual measurements
6. **Future**: Consider Rust migration for proven bottlenecks

---

*Performance is a feature. These benchmarks ensure anvil-core remains fast as it grows.*
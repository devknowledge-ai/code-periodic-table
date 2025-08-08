# Rust Migration Guide

## When and How to Migrate Performance-Critical Code to Rust

This guide helps you migrate performance bottlenecks from prototype languages to Rust when benchmarks prove it's necessary.

## Table of Contents
1. [When to Migrate](#when-to-migrate)
2. [Migration Strategies](#migration-strategies)
3. [Python to Rust](#python-to-rust-migration)
4. [JavaScript to Rust](#javascript-to-rust-migration)
5. [Go to Rust](#go-to-rust-migration)
6. [Common Patterns](#common-patterns)
7. [Tools and Libraries](#tools-and-libraries)
8. [Getting Help](#getting-help)

## When to Migrate

### DO Migrate When:
- ✅ **Benchmarks show clear bottleneck** (>100ms for critical path)
- ✅ **Profile confirms hot path** (>50% time in specific function)
- ✅ **Memory usage excessive** (>2GB for simple operations)
- ✅ **Concurrency issues** (GIL limitations, race conditions)
- ✅ **User complaints** about performance

### DON'T Migrate When:
- ❌ **Performance is acceptable** (meets targets)
- ❌ **Prototype still evolving** (requirements changing)
- ❌ **Complexity isn't worth it** (10% improvement for 10x complexity)
- ❌ **Better algorithm exists** (O(n²) → O(n log n) first)

## Migration Strategies

### Strategy 1: Gradual Migration (Recommended)
Keep your existing code, migrate only hot paths.

```
[Python/JS App] → [Foreign Function Interface] → [Rust Library]
     90%                    Glue Code                  10%
```

### Strategy 2: Microservice Extraction
Move performance-critical component to separate service.

```
[Main App] → [HTTP/gRPC] → [Rust Service]
```

### Strategy 3: Full Rewrite (Last Resort)
Only when the entire component needs optimization.

## Python to Rust Migration

### Using PyO3 (Recommended)

#### Step 1: Identify the Bottleneck
```python
# Original Python - SLOW
def calculate_fingerprint(ast_nodes):
    fingerprint = []
    for node in ast_nodes:  # Hot path
        hash_val = expensive_computation(node)
        fingerprint.append(hash_val)
    return combine_hashes(fingerprint)

# Profile shows this takes 200ms per call
```

#### Step 2: Create Rust Module

```rust
// src/lib.rs
use pyo3::prelude::*;

#[pyfunction]
fn calculate_fingerprint(ast_nodes: Vec<String>) -> PyResult<String> {
    let mut fingerprint = Vec::new();
    
    for node in ast_nodes {
        let hash_val = expensive_computation(&node);
        fingerprint.push(hash_val);
    }
    
    Ok(combine_hashes(fingerprint))
}

#[pyfunction]
fn expensive_computation(node: &str) -> u64 {
    // Rust implementation - 100x faster
    let mut hasher = DefaultHasher::new();
    node.hash(&mut hasher);
    hasher.finish()
}

#[pymodule]
fn rust_fingerprint(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(calculate_fingerprint, m)?)?;
    Ok(())
}
```

#### Step 3: Build Configuration

```toml
# Cargo.toml
[package]
name = "rust-fingerprint"
version = "0.1.0"
edition = "2021"

[lib]
name = "rust_fingerprint"
crate-type = ["cdylib"]

[dependencies]
pyo3 = { version = "0.19", features = ["extension-module"] }
```

```python
# setup.py
from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="rust-fingerprint",
    rust_extensions=[
        RustExtension("rust_fingerprint", binding=Binding.PyO3)
    ],
    zip_safe=False,
)
```

#### Step 4: Use in Python

```python
# Python app
import rust_fingerprint  # Compiled Rust module

def process_file(file_path):
    ast_nodes = parse_file(file_path)  # Stay in Python
    
    # Call Rust for the expensive part
    fingerprint = rust_fingerprint.calculate_fingerprint(ast_nodes)
    
    store_result(fingerprint)  # Stay in Python
    
# Now takes 2ms instead of 200ms!
```

### Maturin for Easy Packaging

```bash
# Install maturin
pip install maturin

# Create new project
maturin new rust_fingerprint
cd rust_fingerprint

# Develop mode (rebuilds on change)
maturin develop

# Build wheel for distribution
maturin build --release
```

## JavaScript to Rust Migration

### Using WebAssembly (Browser/Node)

#### Step 1: Original JavaScript
```javascript
// Slow JavaScript
function matchPatterns(patterns, fingerprint) {
    const results = [];
    for (const pattern of patterns) {
        const similarity = calculateSimilarity(pattern, fingerprint);
        if (similarity > 0.75) {
            results.push({ pattern, similarity });
        }
    }
    return results;
}
```

#### Step 2: Rust Implementation
```rust
// src/lib.rs
use wasm_bindgen::prelude::*;
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize)]
pub struct Match {
    pattern: String,
    similarity: f32,
}

#[wasm_bindgen]
pub fn match_patterns(patterns: &str, fingerprint: &str) -> String {
    let patterns: Vec<String> = serde_json::from_str(patterns).unwrap();
    let mut results = Vec::new();
    
    for pattern in patterns {
        let similarity = calculate_similarity(&pattern, &fingerprint);
        if similarity > 0.75 {
            results.push(Match {
                pattern,
                similarity,
            });
        }
    }
    
    serde_json::to_string(&results).unwrap()
}
```

#### Step 3: Build and Use
```bash
# Install wasm-pack
cargo install wasm-pack

# Build WASM module
wasm-pack build --target nodejs  # or --target web

# This creates pkg/ directory with JS bindings
```

```javascript
// Use in Node.js
const { match_patterns } = require('./pkg/rust_matcher');

function findMatches(patterns, fingerprint) {
    const patternsJson = JSON.stringify(patterns);
    const resultJson = match_patterns(patternsJson, fingerprint);
    return JSON.parse(resultJson);
}
```

### Using Neon (Node.js Native)

```rust
// Native Node module (faster than WASM)
use neon::prelude::*;

fn match_patterns(mut cx: FunctionContext) -> JsResult<JsArray> {
    let patterns = cx.argument::<JsArray>(0)?;
    let fingerprint = cx.argument::<JsString>(1)?;
    
    // Process in Rust...
    
    Ok(results)
}

#[neon::main]
fn main(mut cx: ModuleContext) -> NeonResult<()> {
    cx.export_function("matchPatterns", match_patterns)?;
    Ok(())
}
```

## Go to Rust Migration

### Using CGO

#### Step 1: Rust Library
```rust
// src/lib.rs
#[no_mangle]
pub extern "C" fn process_patterns(
    patterns_ptr: *const u8,
    patterns_len: usize,
) -> *mut c_char {
    let patterns = unsafe {
        std::slice::from_raw_parts(patterns_ptr, patterns_len)
    };
    
    // Process patterns...
    
    CString::new(result).unwrap().into_raw()
}
```

#### Step 2: Go Wrapper
```go
package main

// #cgo LDFLAGS: -L./target/release -lrust_processor
// #include <stdlib.h>
// char* process_patterns(const char* patterns, size_t len);
import "C"
import "unsafe"

func ProcessPatterns(patterns []byte) string {
    result := C.process_patterns(
        (*C.char)(unsafe.Pointer(&patterns[0])),
        C.size_t(len(patterns)),
    )
    defer C.free(unsafe.Pointer(result))
    return C.GoString(result)
}
```

## Common Patterns

### Pattern 1: Keep Business Logic, Optimize Computation

```python
# Python - Business Logic
class PatternAnalyzer:
    def analyze(self, code):
        # Python handles workflow
        ast = self.parse(code)
        
        # Rust handles computation
        fingerprint = rust_lib.compute_fingerprint(ast)
        
        # Python handles results
        return self.format_results(fingerprint)
```

### Pattern 2: Batch Processing

```javascript
// JavaScript coordinates
async function processFiles(files) {
    // Batch files for efficiency
    const batches = chunk(files, 100);
    
    for (const batch of batches) {
        // Rust processes batch in parallel
        const results = await rustWorker.processBatch(batch);
        await saveResults(results);
    }
}
```

### Pattern 3: Hot Path Optimization

```go
func AnalyzeCode(code string) Result {
    // Go does most work
    tokens := tokenize(code)
    ast := parse(tokens)
    
    // Rust only for the bottleneck
    fingerprint := rustLib.GenerateFingerprint(ast)
    
    // Back to Go
    return classify(fingerprint)
}
```

## Tools and Libraries

### Python → Rust
- **PyO3**: Python bindings (recommended)
- **Maturin**: Build tool for PyO3
- **rust-cpython**: Alternative bindings
- **cffi**: C interface option

### JavaScript → Rust
- **wasm-pack**: WASM builder
- **wasm-bindgen**: JS bindings
- **Neon**: Native Node modules
- **napi-rs**: Node-API bindings

### Go → Rust
- **CGO**: C interop
- **rust-bindgen**: Generate bindings
- **cbindgen**: Generate C headers

### Profiling Tools
- **py-spy**: Python profiler
- **clinic**: Chrome DevTools for Node
- **pprof**: Go profiler
- **flamegraph**: Rust profiler

## Migration Checklist

- [ ] **Profile first** - Confirm the bottleneck
- [ ] **Benchmark baseline** - Record current performance
- [ ] **Start small** - Migrate one function first
- [ ] **Test thoroughly** - Ensure correctness
- [ ] **Benchmark again** - Verify improvement
- [ ] **Document** - Explain why Rust was needed
- [ ] **Monitor** - Watch for regressions

## Common Pitfalls

### 1. Unnecessary String Conversions
```rust
// BAD: Converting back and forth
let json_str = serde_json::to_string(&data)?;
let parsed: Data = serde_json::from_str(&json_str)?;

// GOOD: Keep in native format
let data = process_native(data);
```

### 2. Not Batching Operations
```rust
// BAD: Many small calls
for item in items {
    process_one(item);  // Overhead each call
}

// GOOD: Batch processing
process_batch(items);  // One call, parallel inside
```

### 3. Blocking the Runtime
```javascript
// BAD: Blocks Node event loop
const result = rust_lib.processSync(bigData);

// GOOD: Async processing
const result = await rust_lib.processAsync(bigData);
```

## Getting Help

### Resources
- **Rust Book**: https://doc.rust-lang.org/book/
- **PyO3 Guide**: https://pyo3.rs/
- **WASM Guide**: https://rustwasm.github.io/book/
- **Our Examples**: `/examples/migrations/`

### Community Support
- **Discord #rust-help**: Real-time help
- **Office Hours**: Tuesdays 2pm UTC
- **Pair Programming**: Book a session
- **Code Review**: Tag @rust-team

### Don't Know Rust?
**That's OK!** Options:
1. **Ask for help** - We'll pair with you
2. **Provide Python/JS** - Someone else can port
3. **Learn gradually** - Start with simple functions
4. **Focus elsewhere** - Plenty of non-Rust work

## Success Stories

### Example 1: Fingerprint Generator
- **Before**: Python, 200ms per file
- **After**: Rust via PyO3, 2ms per file
- **Effort**: 2 days
- **Code changed**: 5% (only hot path)

### Example 2: Pattern Matcher
- **Before**: JavaScript, 500ms for 1000 patterns
- **After**: WASM, 5ms for 1000 patterns  
- **Effort**: 1 week
- **Code changed**: One module

### Example 3: Stayed in Python!
- **Before**: Naive O(n²) algorithm
- **After**: Better algorithm O(n log n)
- **Effort**: 1 day
- **Lesson**: Algorithm first, language second

## Remember

> **Migrate to Rust only when benchmarks prove it's needed. Many performance problems are algorithmic, not language-related.**

The goal is working software that meets performance targets, not Rust everywhere.
# Semantic Fingerprint Examples

**Status: Demonstration of Cross-Language Pattern Matching**

## Overview

This directory contains examples demonstrating how semantic fingerprinting would work to identify similar patterns across different programming languages and implementations.

## Available Examples

### [Cross-Language Comparison](./cross-language-comparison.md)
Detailed comparison showing how the same semantic pattern appears in different languages and how fingerprinting identifies them as equivalent.

## What is a Semantic Fingerprint?

A semantic fingerprint captures the **meaning** of code, not its syntax:
- Control flow structure
- Data transformations
- Algorithmic approach
- Behavioral properties

## Example: Map-Filter-Reduce Pattern

### Different Languages, Same Fingerprint

#### Python
```python
result = reduce(
    lambda a, b: a + b,
    filter(lambda x: x > 10,
        map(lambda x: x * 2, numbers))
)
```

#### JavaScript
```javascript
const result = numbers
    .map(x => x * 2)
    .filter(x => x > 10)
    .reduce((a, b) => a + b);
```

#### Java
```java
int result = numbers.stream()
    .map(x -> x * 2)
    .filter(x -> x > 10)
    .reduce(0, Integer::sum);
```

#### Rust
```rust
let result: i32 = numbers.iter()
    .map(|x| x * 2)
    .filter(|x| x > 10)
    .sum();
```

### Unified Semantic Fingerprint
```yaml
fingerprint: MAP-FILTER-REDUCE-SUM
components:
  - operation: MAP
    transform: "multiply by 2"
  - operation: FILTER
    predicate: "greater than 10"
  - operation: REDUCE
    aggregation: "sum"
    
properties:
  functional: true
  side_effects: false
  complexity: O(n)
  parallelizable: true
  
similarity_scores:
  python_js: 0.95
  js_java: 0.97
  java_rust: 0.98
  overall: 0.96
```

## Example: Async Pattern Evolution

### Callback Pattern
```javascript
fetchUser(userId, (user) => {
    fetchPosts(user.id, (posts) => {
        renderPage(user, posts);
    });
});
```

### Promise Pattern
```javascript
fetchUser(userId)
    .then(user => fetchPosts(user.id)
        .then(posts => ({user, posts})))
    .then(({user, posts}) => renderPage(user, posts));
```

### Async/Await Pattern
```javascript
async function loadUserPage(userId) {
    const user = await fetchUser(userId);
    const posts = await fetchPosts(user.id);
    renderPage(user, posts);
}
```

### Semantic Fingerprint Comparison
```yaml
callback_fingerprint:
  pattern: NESTED-ASYNC-SEQUENCE
  nesting_depth: 2
  error_handling: implicit
  readability: low

promise_fingerprint:
  pattern: CHAINED-ASYNC-SEQUENCE
  nesting_depth: 1
  error_handling: propagated
  readability: medium

async_await_fingerprint:
  pattern: LINEAR-ASYNC-SEQUENCE
  nesting_depth: 0
  error_handling: try-catch
  readability: high

semantic_equivalence: 0.85  # All three do the same thing
```

## Example: Data Structure Operations

### Binary Tree Traversal

#### Python (Recursive)
```python
def inorder(node):
    if node:
        inorder(node.left)
        process(node.value)
        inorder(node.right)
```

#### Java (Iterative)
```java
void inorder(Node root) {
    Stack<Node> stack = new Stack<>();
    Node current = root;
    
    while (current != null || !stack.isEmpty()) {
        while (current != null) {
            stack.push(current);
            current = current.left;
        }
        current = stack.pop();
        process(current.value);
        current = current.right;
    }
}
```

#### JavaScript (Generator)
```javascript
function* inorder(node) {
    if (node) {
        yield* inorder(node.left);
        yield node.value;
        yield* inorder(node.right);
    }
}
```

### Unified Fingerprint
```yaml
fingerprint: BINARY-TREE-INORDER-TRAVERSAL
algorithm: depth-first
order: left-root-right
space_complexity:
  recursive: O(h)  # h = height
  iterative: O(h)
  generator: O(h)
time_complexity: O(n)

implementation_variants:
  - recursive: "call stack"
  - iterative: "explicit stack"
  - generator: "yield delegation"

semantic_similarity: 1.0  # Identical behavior
```

## Example: Design Pattern Recognition

### Observer Pattern Variants

#### Classic OOP
```java
class Subject {
    List<Observer> observers = new ArrayList<>();
    
    void attach(Observer o) { observers.add(o); }
    void notify(Event e) {
        for (Observer o : observers) {
            o.update(e);
        }
    }
}
```

#### Functional Reactive
```javascript
const subject = new Subject();
const subscription = subject
    .pipe(
        filter(e => e.type === 'important'),
        map(e => e.data)
    )
    .subscribe(data => process(data));
```

#### Event Emitter
```python
class EventEmitter:
    def __init__(self):
        self.events = defaultdict(list)
    
    def on(self, event, handler):
        self.events[event].append(handler)
    
    def emit(self, event, data):
        for handler in self.events[event]:
            handler(data)
```

### Pattern Fingerprint
```yaml
base_fingerprint: PUBLISH-SUBSCRIBE
variants:
  classic_oop:
    coupling: "interface-based"
    subscription: "explicit"
    filtering: "in-observer"
    
  functional_reactive:
    coupling: "stream-based"
    subscription: "declarative"
    filtering: "in-pipeline"
    
  event_emitter:
    coupling: "string-based"
    subscription: "dynamic"
    filtering: "in-handler"

core_similarity: 0.78
behavioral_equivalence: 0.92
```

## Fingerprint Generation Process

### Step 1: Parse to AST
```python
code = "result = [x*2 for x in data if x > 0]"
ast = parse(code)
# AST: ListComp(...)
```

### Step 2: Extract Semantic Features
```python
features = {
    'operation': 'list_comprehension',
    'transform': 'multiply',
    'filter': 'positive',
    'structure': 'functional'
}
```

### Step 3: Generate Vector
```python
vector = [
    0.8,  # functional style
    0.9,  # transformation present
    0.7,  # filtering present
    0.0,  # no side effects
    0.3   # low complexity
]
```

### Step 4: Create Fingerprint
```python
fingerprint = hash(normalize(vector))
# Result: "FP-TRANSFORM-FILTER-A3F2B9"
```

## Similarity Calculation

### Distance Metrics
```python
def semantic_similarity(fp1, fp2):
    structural = structural_similarity(fp1, fp2) * 0.4
    behavioral = behavioral_similarity(fp1, fp2) * 0.4
    complexity = complexity_similarity(fp1, fp2) * 0.2
    return structural + behavioral + complexity
```

### Example Calculation
```yaml
pattern_1: Iterator with filter
pattern_2: List comprehension with condition

structural_similarity: 0.7  # Different structure
behavioral_similarity: 0.95  # Same behavior
complexity_similarity: 0.9  # Similar complexity

overall_similarity: 0.84  # Highly similar
```

## Applications

### Code Search
Find semantically similar code across your codebase:
```bash
$ cpt search --similar-to "async data fetch with retry"
Found 3 similar patterns:
1. api_client.py:45 - Retry with exponential backoff (0.89)
2. data_loader.js:120 - Async fetch with fallback (0.85)
3. NetworkManager.java:200 - Resilient request handler (0.82)
```

### Code Review
Identify equivalent implementations:
```bash
$ cpt compare implementation1.py implementation2.js
Semantic similarity: 0.92
Both implement: Observer pattern with filtering
Differences: Language idioms only
Suggestion: Consider consolidating approach
```

### Learning
Understand patterns across languages:
```bash
$ cpt explain --pattern "map-reduce" --languages "python,js,java"
Showing equivalent implementations...
Core concept: Transform and aggregate data
Variations: Functional, imperative, stream-based
```

---

**Note:** These examples demonstrate the concept of semantic fingerprinting. The actual implementation is still in research phase with promising early results.
# NullGuard Prototype: Development Plan

**⚠️ IMPORTANT: This is a plan, not an active project. No code exists yet.**

*This document outlines how we could build a prototype to demonstrate the Anvil Suite's approach*

## The Goal (Aspirational)

We aim to build a standalone NullGuard that could achieve 70-80% accuracy in detecting null/None bugs. If successful, this would serve as:
1. **Proof of concept** for the Anvil approach
2. **Marketing tool** to attract contributors
3. **Test bed** for Adaptive Documentation integration

**Current Status**: Looking for contributors to start implementation. See [GETTING_STARTED.md](../../GETTING_STARTED.md).

## Prototype Architecture

```
nullguard-prototype/
├── core/
│   ├── detector.py        # Main detection logic
│   ├── patterns.py        # Known null patterns
│   └── analyzer.py        # AST analysis
├── data/
│   ├── training/          # Sample bugs with context
│   └── mock_context.json  # Simulated Adaptive Documentation
├── demo/
│   ├── web_ui.py          # Interactive demo
│   └── cli.py             # Command-line demo
└── tests/
    └── accuracy_test.py   # Measure detection rate
```

## Proposed Implementation Plan

**Note: These timelines are estimates for when development begins, not current activities.**

### Phase 1: Core Detection (Estimated: 1 week once started)
Goal: Build basic null detection with 70% accuracy:

```python
# core/detector.py
import ast
from typing import List, Tuple

class NullDetector:
    """Detects potential null/None reference bugs"""
    
    def __init__(self, context_db=None):
        self.context_db = context_db  # Future: Adaptive Documentation
        self.patterns = self.load_patterns()
    
    def detect(self, code: str) -> List[NullBug]:
        """Find potential null reference bugs in code"""
        tree = ast.parse(code)
        bugs = []
        
        # Pattern 1: Direct attribute access after function call
        # user = get_user(); user.name  # Dangerous!
        bugs.extend(self.find_unchecked_access(tree))
        
        # Pattern 2: Dictionary access without get()
        # data['key']  # Should be data.get('key')
        bugs.extend(self.find_unsafe_dict_access(tree))
        
        # Pattern 3: Chain calls without checks
        # response.data.user.name  # Any could be None
        bugs.extend(self.find_chain_access(tree))
        
        # Use context if available (shows future integration)
        if self.context_db:
            bugs = self.enhance_with_context(bugs)
        
        return bugs
```

### Phase 2: Pattern Library (Week 1-2)
Build library of common null patterns:

```python
# core/patterns.py
NULL_PATTERNS = {
    "unchecked_return": {
        "description": "Function return value used without null check",
        "example": "user = get_user(id)\nprint(user.name)",
        "fix": "user = get_user(id)\nif user:\n    print(user.name)",
        "confidence": 0.85
    },
    "dict_key_access": {
        "description": "Dictionary accessed with [] instead of .get()",
        "example": "value = data['key']",
        "fix": "value = data.get('key')",
        "confidence": 0.75
    },
    "chain_attribute": {
        "description": "Chained attribute access without checks",
        "example": "response.data.user.name",
        "fix": "if response and response.data and response.data.user:\n    name = response.data.user.name",
        "confidence": 0.70
    }
}
```

### Phase 3: Demo Interface (Week 2)
Create compelling demo:

```python
# demo/web_ui.py
from flask import Flask, render_template, request
from core.detector import NullDetector

app = Flask(__name__)
detector = NullDetector()

@app.route('/')
def index():
    return render_template('demo.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.json['code']
    bugs = detector.detect(code)
    
    return {
        'bugs': [bug.to_dict() for bug in bugs],
        'accuracy': {
            'without_context': 0.73,  # Current accuracy
            'with_context': 0.95       # Future with Adaptive Documentation
        }
    }
```

### Phase 4: Mock Context Integration (Week 2-3)
Simulate Adaptive Documentation data:

```json
// data/mock_context.json
{
  "patterns": [
    {
      "function": "get_user",
      "returns_null": true,
      "when": "user not found or inactive",
      "documented_by": "adaptive_documentation",
      "confidence": 0.95
    },
    {
      "function": "fetch_data", 
      "returns_null": false,
      "when": "always returns dict, empty if no data",
      "documented_by": "developer_comment",
      "confidence": 0.90
    }
  ]
}
```

## Success Metrics

### Accuracy Targets
- **Without context**: 70-75% detection rate
- **With mock context**: 85-90% detection rate
- **False positive rate**: <10%

### Demo Impact
- **Live demo**: nullguard.anvilsuite.com
- **CLI tool**: `pip install nullguard-prototype`
- **Video**: 2-minute showcase video
- **Blog post**: "How we achieved 70% accuracy in 2 weeks"

## Test Suite

```python
# tests/accuracy_test.py
import json
from core.detector import NullDetector

def test_accuracy():
    """Measure detection accuracy on known bugs"""
    
    with open('data/test_cases.json') as f:
        test_cases = json.load(f)
    
    detector = NullDetector()
    correct = 0
    total = len(test_cases)
    
    for case in test_cases:
        bugs = detector.detect(case['code'])
        if case['has_bug'] == (len(bugs) > 0):
            correct += 1
    
    accuracy = correct / total
    print(f"Accuracy: {accuracy:.1%}")
    assert accuracy >= 0.70, "Must achieve 70% accuracy"
```

## Marketing the Prototype

### The Story
"We built a null bug detector with 70% accuracy in 2 weeks. Here's how Adaptive Documentation will make it 95% accurate."

### Demo Flow
1. **Show the problem**: Common null bug examples
2. **Run detection**: Find bugs with 70% accuracy
3. **Add context**: Show mock Adaptive Documentation data
4. **Improved detection**: Jump to 90% accuracy
5. **Call to action**: "Help us build the real thing"

### Key Messages
- "This is just the beginning"
- "Imagine this for all bug types"
- "Context is the secret sauce"
- "Join us in building the future"

## Proposed Development Timeline

**This is a hypothetical timeline for when we have contributors and begin development:**

### Week 1 (Once Started)
- [ ] Core detection engine
- [ ] Basic pattern matching
- [ ] Target: 70% accuracy

### Week 2 (If Week 1 Successful)
- [ ] Web demo interface
- [ ] CLI tool
- [ ] Mock context integration

### Week 3 (If Resources Available)
- [ ] Polish and testing
- [ ] Documentation
- [ ] Demo site preparation

### Week 4 (If Ready for Launch)
- [ ] Community outreach
- [ ] Documentation completion
- [ ] Call for additional contributors

## How to Contribute

### Immediate Needs
1. **Pattern contributions**: Add more null bug patterns
2. **Test cases**: Real-world null bugs for testing
3. **UI/UX**: Improve demo interface
4. **Documentation**: Usage examples

### Get Started
```bash
git clone https://github.com/anvil-suite/nullguard-prototype
cd nullguard-prototype
pip install -e .
python -m pytest tests/
```

## The Bigger Picture

This prototype is:
1. **Marketing**: Shows what's possible
2. **Validation**: Proves the approach works
3. **Foundation**: Becomes the real NullGuard
4. **Catalyst**: Attracts contributors and partners

Success here drives success everywhere.

---

*"Ship a working demo. The rest will follow."*
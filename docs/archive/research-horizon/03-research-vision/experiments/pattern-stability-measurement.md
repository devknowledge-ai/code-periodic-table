# Pattern Stability Measurement: Experimental Framework

## Building a Geiger Counter for Code

Based on the [Unstable Patterns Theory](../UNSTABLE_PATTERNS_THEORY.md), this document outlines practical experiments to measure pattern stability and decay in real codebases.

---

## Core Hypothesis

**Code patterns exhibit measurable "half-lives" that predict their likelihood of decay (refactoring, bug fixes, or abandonment).**

---

## Experimental Design

### Experiment 1: Measuring Pattern Half-Lives

**Objective**: Determine the average lifespan of different patterns before they decay.

**Methodology**:
```python
def measure_pattern_half_life(repo_path: str, pattern_type: str) -> float:
    """
    Track a pattern from introduction to modification/removal
    """
    patterns = []
    
    for commit in git.get_commits(repo_path):
        # Find pattern introductions
        new_patterns = detect_patterns(commit.added_code, pattern_type)
        for pattern in new_patterns:
            patterns.append({
                'id': generate_fingerprint(pattern),
                'birth': commit.date,
                'death': None,
                'decay_type': None
            })
        
        # Find pattern deaths (modifications/removals)
        for pattern in patterns:
            if pattern['death'] is None:
                if pattern_modified(pattern['id'], commit):
                    pattern['death'] = commit.date
                    pattern['decay_type'] = classify_change(commit)
    
    # Calculate half-life (time when 50% of patterns have decayed)
    return calculate_half_life(patterns)
```

**Expected Results**:
| Pattern Type | Expected Half-Life | Decay Mode |
|--------------|-------------------|------------|
| Nested loops without bounds | 2-4 weeks | Performance fix |
| String concatenated SQL | 3-6 months | Security fix |
| God objects (>1000 lines) | 6-12 months | Refactoring |
| Callback pyramids | 1-2 years | Modernization |
| Manual memory management | 2-5 years | Language migration |

### Experiment 2: Context-Dependent Stability

**Objective**: Prove that the same pattern has different stability in different contexts.

**Test Pattern**: Singleton Pattern
```python
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

**Contexts to Test**:
```python
stability_measurements = {
    'desktop_app': measure_in_context(['pygame', 'tkinter', 'pyqt']),
    'web_app': measure_in_context(['django', 'flask', 'fastapi']),
    'microservice': measure_in_context(['kubernetes', 'docker', 'aws']),
    'embedded': measure_in_context(['micropython', 'arduino']),
    'data_pipeline': measure_in_context(['airflow', 'spark', 'pandas'])
}
```

**Expected Stability Scores** (0=instant decay, 1=perfectly stable):
- Embedded systems: 0.85 (stable - resource constraints)
- Desktop apps: 0.70 (mostly stable)
- Data pipelines: 0.40 (problematic - parallel processing)
- Web apps: 0.20 (unstable - scaling issues)
- Microservices: 0.05 (radioactive - violates principles)

### Experiment 3: Decay Cascade Detection

**Objective**: Demonstrate that one unstable pattern can trigger cascading failures.

**Methodology**:
```python
def track_decay_cascade(initial_bug_commit):
    """
    Track how fixing one bug leads to discovering others
    """
    cascade = [initial_bug_commit]
    time_window = timedelta(days=30)
    
    related_commits = get_commits_after(
        initial_bug_commit.date,
        initial_bug_commit.date + time_window
    )
    
    for commit in related_commits:
        if references_previous_fix(commit, cascade):
            cascade.append(commit)
            # Extend window to catch chain reactions
            time_window = commit.date - initial_bug_commit.date + timedelta(days=30)
    
    return {
        'initial_decay': classify_bug(initial_bug_commit),
        'cascade_length': len(cascade),
        'total_duration': cascade[-1].date - cascade[0].date,
        'decay_chain': [classify_bug(c) for c in cascade]
    }
```

**Example Cascade**:
```
1. Performance bug fix (nested loop O(n³))
   ↓ (2 days)
2. Memory leak discovered (caching added incorrectly)
   ↓ (1 week)
3. Race condition found (cache not thread-safe)
   ↓ (3 days)
4. Deadlock introduced (over-zealous locking)
   ↓ (2 weeks)
5. Complete refactor (pattern fundamentally unstable)
```

### Experiment 4: Stability Learning Curves

**Objective**: Measure how teams learn to avoid unstable patterns over time.

**Methodology**:
```python
def measure_team_learning(repo_path: str, pattern_type: str):
    """
    Track reduction in unstable pattern introduction over time
    """
    quarterly_stats = defaultdict(lambda: {'introduced': 0, 'fixed': 0})
    
    for commit in git.get_commits(repo_path):
        quarter = get_quarter(commit.date)
        
        # Count introductions
        if introduces_pattern(commit, pattern_type):
            quarterly_stats[quarter]['introduced'] += 1
        
        # Count fixes
        if fixes_pattern(commit, pattern_type):
            quarterly_stats[quarter]['fixed'] += 1
    
    # Calculate learning coefficient
    introduction_rate = [stats['introduced'] for stats in quarterly_stats.values()]
    return calculate_learning_curve(introduction_rate)
```

**Expected Learning Curves**:
```
Quarter 1: 45 null pointer bugs introduced
Quarter 2: 38 null pointer bugs introduced (-15%)
Quarter 3: 28 null pointer bugs introduced (-26%)
Quarter 4: 20 null pointer bugs introduced (-29%)
Quarter 5: 18 null pointer bugs introduced (-10%)
Quarter 6: 15 null pointer bugs introduced (-17%)
→ Learning coefficient: 0.72 (28% reduction per quarter)
```

### Experiment 5: Radioactivity Detection

**Objective**: Build a real-time "Geiger counter" that measures code radioactivity.

**Implementation**:
```python
class CodeGeigerCounter:
    def __init__(self):
        self.decay_signatures = load_decay_signatures()
        self.stability_model = load_trained_model()
    
    def measure_radioactivity(self, code_block):
        """
        Return radioactivity level (0-100 millirems)
        """
        factors = {
            'complexity': self.measure_complexity(code_block),
            'coupling': self.measure_coupling(code_block),
            'known_antipatterns': self.detect_antipatterns(code_block),
            'security_vulnerabilities': self.scan_vulnerabilities(code_block),
            'performance_risks': self.analyze_performance(code_block),
            'team_conventions': self.check_conventions(code_block)
        }
        
        # Weighted radioactivity score
        radioactivity = sum(
            factors[key] * DECAY_WEIGHTS[key]
            for key in factors
        )
        
        return {
            'millirems': radioactivity,
            'classification': self.classify_danger(radioactivity),
            'half_life': self.predict_half_life(factors),
            'recommended_action': self.suggest_action(radioactivity)
        }
    
    def classify_danger(self, millirems):
        if millirems < 10:
            return "STABLE"
        elif millirems < 30:
            return "BACKGROUND_RADIATION"
        elif millirems < 60:
            return "ELEVATED"
        elif millirems < 80:
            return "DANGEROUS"
        else:
            return "CRITICAL_MASS"
```

**Real-time IDE Integration**:
```python
@ide_hook('on_code_change')
def check_radioactivity(change_event):
    geiger = CodeGeigerCounter()
    reading = geiger.measure_radioactivity(change_event.code)
    
    if reading['millirems'] > 60:
        show_warning(
            f"⚠️ High radioactivity detected: {reading['millirems']} mR",
            f"Pattern half-life: {reading['half_life']}",
            f"Recommendation: {reading['recommended_action']}"
        )
```

---

## Validation Metrics

### Success Criteria

1. **Half-life Prediction Accuracy**: Within 20% of actual decay time for 70% of patterns
2. **Context Sensitivity**: Same pattern shows >50% stability variance across contexts
3. **Cascade Detection**: Identify 60% of cascade chains within 2 steps
4. **Learning Curve**: Teams show 25% reduction in unstable patterns after 6 months
5. **Real-time Detection**: Flag 80% of patterns that decay within 30 days

### Data Requirements

- **Minimum Repository Size**: 10,000+ commits
- **Time Span**: 2+ years of history
- **Active Development**: 10+ commits per week
- **Bug Fix Commits**: 20%+ of total commits
- **Multiple Contributors**: 5+ developers

---

## Experimental Timeline

### Phase 1: Data Collection (Months 1-2)
- Identify 50+ suitable repositories
- Extract pattern instances and decay events
- Build initial decay signature database

### Phase 2: Model Training (Months 3-4)
- Train stability prediction models
- Validate half-life calculations
- Tune radioactivity thresholds

### Phase 3: Real-world Testing (Months 5-6)
- Deploy Geiger counter to beta users
- Measure prediction accuracy
- Collect feedback on false positives

### Phase 4: Refinement (Months 7-8)
- Adjust models based on results
- Add context-specific tuning
- Improve real-time performance

---

## Expected Outcomes

### Scientific Contributions

1. **First empirical measurement of code pattern stability**
2. **Proof that context determines pattern viability**
3. **Quantification of technical debt accumulation rates**
4. **Evidence for cascade theory of bug propagation**

### Practical Applications

1. **IDE plugin that prevents 40% of future bugs**
2. **Code review tool highlighting radioactive patterns**
3. **Technical debt measurement in "decay risk" units**
4. **Team learning dashboard showing stability improvements**

### Industry Impact

- Shift from opinion-based to evidence-based best practices
- Quantifiable code quality metrics (half-life, radioactivity)
- Predictive maintenance for software systems
- Data-driven refactoring prioritization

---

## Risks and Mitigation

### Risk 1: Patterns Too Complex to Fingerprint
**Mitigation**: Start with simple, well-defined patterns

### Risk 2: Insufficient Decay Events for Training
**Mitigation**: Focus on high-frequency patterns with short half-lives

### Risk 3: Context Variables Too Numerous
**Mitigation**: Begin with broad context categories, refine over time

### Risk 4: Developer Rejection of "Radioactivity" Warnings
**Mitigation**: Extensive user testing of warning thresholds and messaging

---

## Conclusion

By treating code patterns as potentially unstable isotopes rather than fixed elements, we can build practical tools that measure and predict stability. This experimental framework will validate the Unstable Patterns Theory and create immediate value for developers through early detection of patterns destined to decay.

The key insight: **We don't need to understand why patterns decay, just recognize the signatures of instability and warn before the cascade begins.**

---

*"In software, as in nuclear physics, the most dangerous radioactivity is the kind you can't see until it's too late."*
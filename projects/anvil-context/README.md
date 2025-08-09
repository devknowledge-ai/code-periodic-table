# Anvil Context: Living Documentation for Code, Errors, and Crashes

*Formerly "Sticky Comments" - now a comprehensive context capture system*

Part of the [Anvil Suite](../../README.md) - capturing the "why" behind everything.

**Comments that attach to code patterns, runtime errors, and crash reports - preserving team knowledge forever.**

## The Evolution

We started with "comments that survive refactoring." Then we realized: **why stop at static code?**

Anvil Context now captures:
- 📝 **Code Comments** - Attached to semantic fingerprints
- 🐛 **Error Context** - Why specific errors happen and how they're fixed
- 💥 **Crash Reports** - Production failure context and resolutions
- 🎯 **Performance Notes** - Why certain code is slow and what's been tried

## Core Innovation

Traditional comments are attached to *locations*. Anvil Context attaches to *patterns*.

```python
# Traditional comment (breaks when code moves)
# Line 45: Check for null - user might be archived

# Anvil Context (survives everything)
@context(fingerprint="auth_user_fetch_v2")
"""
This getUser() can return null for archived users.
We handle at caller level to avoid breaking integrations.
ALWAYS check for null here.

Related crashes: PROD-2024-001, PROD-2024-017
Fix commit: a3b2c1d
Author: @jane, 2024-03-15
"""
```

## The Superpower: Integration

### With Anvil Guard
```python
# Anvil Guard warning becomes intelligent
⚠️ Potential null reference in user.profile.name

📚 Related Context (3 months ago by @jane):
"This crashes in production when user is archived.
See crash PROD-2024-001. Always check for null."

💡 Suggested fix (from history):
if user and user.profile:
    name = user.profile.name
```

### With Anvil Memory
```bash
# Search by error type
anvil-memory query --error "NullPointerException"

# Returns all code that ever caused this error
# PLUS all team context about how it was fixed
```

### With Adaptive Documentation
Context Notes become training data:
1. Developer adds note about a crash
2. Adaptive Documentation learns this pattern is error-prone
3. Next time similar code is written, it prompts for documentation

## Data Model

```python
@dataclass
class ContextNote:
    # Identity
    id: str
    fingerprint: str  # From anvil-core
    
    # Content
    type: Literal["code", "error", "crash", "performance"]
    content: str
    author: str
    timestamp: datetime
    
    # For errors/crashes
    error_type: Optional[str]
    stack_trace_hash: Optional[str]
    fix_commit: Optional[str]
    production_impact: Optional[str]
    
    # Metadata
    tags: List[str]
    upvotes: int  # Team can vote on helpful notes
    related_notes: List[str]
```

## Usage Examples

### Adding Code Context
```bash
# Attach a note to current function
anvil-context add --type code "This algorithm is O(n²) but that's acceptable because n < 100"

# Attach to specific pattern
anvil-context add --fingerprint abc123 "Security: This validates user input"
```

### Adding Error Context
```bash
# After fixing a bug
anvil-context add-error \
  --type "TypeError" \
  --fix-commit "a3b2c1d" \
  --note "Happens when API returns string instead of number. Added type coercion."
```

### Adding Crash Context
```bash
# Link Sentry crash to code
anvil-context add-crash \
  --sentry-id "PROD-2024-001" \
  --note "Race condition when two users update simultaneously. Fixed with optimistic locking."
```

### Viewing Context
```python
# In IDE (appears on hover)
def get_user(id):  # 🔍 3 context notes
    ...

# Via CLI
anvil-context show --file auth.py --line 45

# Output:
📚 Context Notes for get_user():

1. [ERROR] by @jane (3 months ago):
   "Returns null for archived users - handle at caller"
   Related crashes: 2
   
2. [PERFORMANCE] by @bob (1 month ago):
   "Don't add caching here - tried it, made things worse"
   
3. [CODE] by @alice (2 weeks ago):
   "Planning to refactor in Q2 - see RFC-123"
```

## Implementation Roadmap

### Phase 1: Code Comments (Weeks 1-3)
- [x] Semantic fingerprinting via anvil-core
- [ ] Comment storage (SQLite)
- [ ] Git tracking integration
- [ ] Basic CLI interface

### Phase 2: Error Integration (Weeks 4-6)
- [ ] Error fingerprinting algorithm
- [ ] Stack trace analysis
- [ ] Fix commit linking
- [ ] Error search capabilities

### Phase 3: Crash Report Integration (Weeks 7-9)
- [ ] Sentry integration
- [ ] Bugsnag integration
- [ ] Crash-to-code mapping
- [ ] Production impact tracking

### Phase 4: Full Suite Integration (Weeks 10-12)
- [ ] Anvil Guard enhancement
- [ ] Anvil Memory indexing
- [ ] Adaptive Documentation training
- [ ] IDE plugins (VSCode, IntelliJ)

## Why This Changes Everything

### Before Anvil Context
- Comments drift from code
- Error knowledge lives in tickets
- Crash context lost after fix
- Same bugs happen repeatedly

### After Anvil Context
- Comments follow code everywhere
- Error patterns have permanent notes
- Crash wisdom preserved forever
- Team learns from every failure

## Success Metrics

- **Coverage**: 80% of error-prone code has context notes
- **Retrieval**: <100ms to find relevant context
- **Usage**: Context viewed 10+ times per developer per day
- **Impact**: 30% reduction in repeat bugs

## The Bigger Picture

Anvil Context isn't just about comments. It's about creating a **living knowledge base** that:

1. **Captures context** at the moment of highest clarity (during fixes)
2. **Preserves wisdom** across team changes
3. **Surfaces knowledge** exactly when needed
4. **Trains AI tools** with high-signal human insight

This is how we achieve the Anvil Suite's mission: **Teams never repeat the same mistake twice.**

## Get Involved

### High-Priority Tasks
1. **Error Fingerprinting**: Design algorithm for matching errors to code
2. **Crash Integration**: Build Sentry/Bugsnag connectors
3. **IDE Plugins**: VSCode extension for viewing/adding context
4. **Search Interface**: Full-text search across all context notes

### Quick Wins
- Add example context notes to the demo
- Design the UI for displaying context
- Write integration tests
- Document the API

## Technical Architecture

```
anvil-context/
├── core/
│   ├── storage.py       # SQLite/PostgreSQL storage
│   ├── fingerprint.py   # Uses anvil-core
│   └── tracker.py       # Git integration
├── integrations/
│   ├── sentry.py        # Crash report integration
│   ├── bugsnag.py       # Alternative crash reporter
│   └── github.py        # Issue tracking
├── api/
│   ├── rest.py          # REST API for IDEs
│   └── cli.py           # Command-line interface
└── plugins/
    ├── vscode/          # VSCode extension
    └── intellij/        # IntelliJ plugin
```

## Example: Real-World Impact

```python
# A real production bug that happened 3 times before Anvil Context

def process_payment(user, amount):
    account = user.account  # 💥 Crashes if user is None
    account.charge(amount)

# After first crash, developer adds context:
@context(type="crash", sentry_id="PROD-001")
"""
CRITICAL: user can be None when called from webhook
Check: if not user or not user.account: return error
This has caused $10K in failed transactions
"""

# Now, Anvil Guard warns future developers:
"⚠️ Similar pattern caused crash PROD-001 - $10K impact"

# Result: Bug never happens again
```

## FAQ

**Q: How is this different from code comments?**
A: Comments are static text. Context Notes are structured data that integrates with all Anvil tools.

**Q: What about sensitive information?**
A: Context notes can be encrypted and access-controlled. Production data should never be included.

**Q: How does this scale?**
A: Fingerprinting ensures O(1) lookup. Storage is append-only. Old notes can be archived.

**Q: Can I use this without the other Anvil tools?**
A: Yes! Anvil Context is valuable standalone, but more powerful when integrated.

---

*"Every bug fixed is a lesson learned. Anvil Context ensures those lessons are never forgotten."*
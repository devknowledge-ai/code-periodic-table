# Anvil Context Integration Specification

*How Anvil Context enhances every tool in the suite*

## Core Integration API

```python
from typing import List, Optional
from dataclasses import dataclass

class AnvilContextAPI:
    """Central API for all Anvil tools to access context"""
    
    def get_context_for_fingerprint(
        self, 
        fingerprint: str,
        types: Optional[List[str]] = None
    ) -> List[ContextNote]:
        """Get all context notes for a code fingerprint"""
        pass
    
    def get_context_for_error(
        self,
        error_type: str,
        stack_trace: Optional[str] = None
    ) -> List[ContextNote]:
        """Get context for specific error types"""
        pass
    
    def add_context(
        self,
        note: ContextNote,
        auto_link: bool = True
    ) -> str:
        """Add new context, optionally auto-link to related code"""
        pass
    
    def search_context(
        self,
        query: str,
        filters: Optional[dict] = None
    ) -> List[ContextNote]:
        """Full-text search across all context"""
        pass
```

## Integration with Anvil Guard

### Enhanced Warning Messages

```python
# anvil-guard/src/enhancer.py
from anvil_context import AnvilContextAPI

class WarningEnhancer:
    def __init__(self):
        self.context_api = AnvilContextAPI()
    
    def enhance_warning(self, warning: Warning) -> EnhancedWarning:
        """Add historical context to warnings"""
        
        # Get fingerprint of problematic code
        fingerprint = self.get_fingerprint(warning.location)
        
        # Fetch relevant context
        context_notes = self.context_api.get_context_for_fingerprint(
            fingerprint,
            types=["error", "crash", "code"]
        )
        
        # Find similar error patterns
        error_context = self.context_api.get_context_for_error(
            warning.error_type
        )
        
        return EnhancedWarning(
            original=warning,
            historical_context=context_notes,
            similar_errors=error_context,
            suggested_fix=self.extract_fix_from_context(context_notes)
        )
```

### Example Output

```
⚠️ Null Reference Warning at auth.py:45

📚 Historical Context (3 notes):
1. [CRASH] 2024-03-15 by @jane:
   "User can be None when called from webhook"
   Production Impact: $10K in failed transactions
   Fix: Check user exists before accessing

2. [ERROR] 2024-02-01 by @bob:
   "TypeError here when user is archived"
   
3. [CODE] 2024-01-15 by @alice:
   "TODO: Add proper null checking"

💡 Suggested Fix (from history):
if user and user.account:
    process_payment(user.account)
```

## Integration with Anvil Memory

### Enriched Search Index

```python
# anvil-memory/src/indexer.py
from anvil_context import AnvilContextAPI

class EnhancedIndexer:
    def __init__(self):
        self.context_api = AnvilContextAPI()
    
    def index_repository(self, repo_path: str):
        """Index repo with context notes"""
        
        # Standard Git indexing
        commits = self.index_git_history(repo_path)
        
        # Enhance with context
        for commit in commits:
            # Get fingerprints for changed code
            fingerprints = self.get_commit_fingerprints(commit)
            
            # Fetch all related context
            for fp in fingerprints:
                context = self.context_api.get_context_for_fingerprint(fp)
                commit.context_notes = context
            
            # Index for search
            self.search_index.add({
                'commit': commit,
                'context': context,
                'searchable_text': self.extract_text(commit, context)
            })
```

### New Search Capabilities

```bash
# Search by error type
anvil-memory search --error "NullPointerException"

# Search by crash ID
anvil-memory search --crash "PROD-2024-001"  

# Search context notes
anvil-memory search --context "race condition"

# Combined search
anvil-memory search --query "payment" --has-crashes --fixed
```

## Integration with Adaptive Documentation

### Learning from Context

```python
# adaptive-documentation/src/learner.py
from anvil_context import AnvilContextAPI

class ContextLearner:
    def __init__(self):
        self.context_api = AnvilContextAPI()
    
    def learn_from_context(self):
        """Analyze context notes to identify documentation needs"""
        
        # Find patterns with many error/crash notes
        problematic_patterns = self.context_api.search_context(
            filters={'type': ['error', 'crash']}
        )
        
        # Group by fingerprint
        pattern_issues = self.group_by_fingerprint(problematic_patterns)
        
        # Identify patterns needing documentation
        for fingerprint, issues in pattern_issues.items():
            if len(issues) > 3:  # Multiple issues
                self.mark_for_documentation(
                    fingerprint,
                    priority='high',
                    reason=f"{len(issues)} production issues"
                )
    
    def generate_prompt(self, fingerprint: str) -> str:
        """Generate documentation prompt based on context"""
        
        context = self.context_api.get_context_for_fingerprint(fingerprint)
        
        if self.has_crashes(context):
            return "This pattern has caused production crashes. Please document edge cases and error handling."
        elif self.has_performance_issues(context):
            return "This code has performance implications. Please document complexity and optimization considerations."
        else:
            return "Please document the key decisions and trade-offs in this implementation."
```

## Integration with Anvil Fingerprint

### Context-Aware Fingerprinting

```python
# anvil-fingerprint/src/fingerprinter.py
from anvil_context import AnvilContextAPI

class ContextAwareFingerprinter:
    def __init__(self):
        self.context_api = AnvilContextAPI()
    
    def generate_fingerprint(self, code: str) -> FingerprintWithContext:
        """Generate fingerprint with context metadata"""
        
        # Standard fingerprinting
        base_fingerprint = self.compute_fingerprint(code)
        
        # Check for existing context
        existing_context = self.context_api.get_context_for_fingerprint(
            base_fingerprint
        )
        
        # Create enhanced fingerprint
        return FingerprintWithContext(
            id=base_fingerprint,
            has_context=len(existing_context) > 0,
            error_prone=self.has_error_context(existing_context),
            crash_history=self.count_crashes(existing_context),
            last_modified_context=self.get_latest_context(existing_context)
        )
```

## Database Schema

```sql
-- Core context notes table
CREATE TABLE context_notes (
    id UUID PRIMARY KEY,
    fingerprint VARCHAR(64) NOT NULL,
    type VARCHAR(20) NOT NULL,
    content TEXT NOT NULL,
    author VARCHAR(100) NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    
    -- Error/crash specific
    error_type VARCHAR(100),
    stack_trace_hash VARCHAR(64),
    fix_commit VARCHAR(40),
    production_impact TEXT,
    
    -- Metadata
    tags TEXT[],
    upvotes INTEGER DEFAULT 0,
    
    -- Indexes
    INDEX idx_fingerprint (fingerprint),
    INDEX idx_type (type),
    INDEX idx_error (error_type),
    INDEX idx_timestamp (timestamp)
);

-- Relationships between notes
CREATE TABLE context_relationships (
    note_id UUID REFERENCES context_notes(id),
    related_note_id UUID REFERENCES context_notes(id),
    relationship_type VARCHAR(20),
    PRIMARY KEY (note_id, related_note_id)
);

-- Full-text search
CREATE INDEX context_search_idx ON context_notes 
USING GIN(to_tsvector('english', content));
```

## REST API for IDEs

```yaml
openapi: 3.0.0
info:
  title: Anvil Context API
  version: 1.0.0

paths:
  /context/{fingerprint}:
    get:
      summary: Get context for fingerprint
      parameters:
        - name: fingerprint
          in: path
          required: true
          schema:
            type: string
      responses:
        200:
          description: Context notes
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/ContextNote'
    
  /context:
    post:
      summary: Add new context note
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ContextNote'
      responses:
        201:
          description: Created
          
  /context/search:
    get:
      summary: Search context notes
      parameters:
        - name: q
          in: query
          schema:
            type: string
        - name: type
          in: query
          schema:
            type: string
            enum: [code, error, crash, performance]
```

## Performance Considerations

### Caching Strategy
```python
class ContextCache:
    """LRU cache for frequently accessed context"""
    
    def __init__(self, max_size: int = 1000):
        self.cache = LRUCache(max_size)
        self.ttl = timedelta(minutes=5)
    
    def get_context(self, fingerprint: str) -> Optional[List[ContextNote]]:
        return self.cache.get(fingerprint)
    
    def set_context(self, fingerprint: str, notes: List[ContextNote]):
        self.cache.set(fingerprint, notes, ttl=self.ttl)
```

### Indexing Strategy
- Fingerprints are indexed for O(1) lookup
- Full-text search uses PostgreSQL GIN indexes
- Recent context cached in Redis
- Background job indexes new context asynchronously

## Security Considerations

### Access Control
```python
class ContextSecurity:
    def can_read_context(self, user: User, note: ContextNote) -> bool:
        """Check read permissions"""
        # Public by default within organization
        return user.organization == note.organization
    
    def can_write_context(self, user: User, fingerprint: str) -> bool:
        """Check write permissions"""
        # Any developer can add context
        return user.role in ['developer', 'lead', 'admin']
    
    def sanitize_content(self, content: str) -> str:
        """Remove sensitive data"""
        # Remove credentials, PII, etc.
        return self.redact_sensitive(content)
```

## Migration from Existing Tools

### Import from JIRA/GitHub Issues
```bash
# Import context from existing issue trackers
anvil-context import --source jira --project MYAPP
anvil-context import --source github --repo myorg/myapp
```

### Export for Backup
```bash
# Export all context as JSON
anvil-context export --format json > context-backup.json

# Export specific date range
anvil-context export --since 2024-01-01 --until 2024-12-31
```

---

*This specification ensures Anvil Context becomes the knowledge backbone of the entire Anvil Suite.*
# Integration API Specification

## Minimum Viable API for AI Tool Integration

This document defines the minimal API surface needed for AI coding assistants to integrate with Adaptive Documentation.

## Core Data Structures

### Conversation Format

```typescript
interface Message {
  role: 'user' | 'assistant' | 'system';
  content: string;
  timestamp: Date;
  metadata?: {
    model?: string;
    temperature?: number;
    tool_calls?: ToolCall[];
  };
}

interface Conversation {
  id: string;
  messages: Message[];
  startTime: Date;
  endTime?: Date;
  metadata: {
    tool: string;  // 'aider', 'cline', 'roo-code', etc.
    version: string;
    session_type: 'chat' | 'command' | 'autonomous';
  };
}
```

### Code Change Format

```typescript
interface CodeChange {
  file: string;
  language: string;
  diff: string;  // unified diff format
  before: string;  // full file before
  after: string;   // full file after
  lineRanges: {
    start: number;
    end: number;
  }[];
}

interface AcceptedCode {
  conversationId: string;
  messageIndex: number;  // which assistant message generated this
  changes: CodeChange[];
  accepted: boolean;
  acceptedAt: Date;
  modifiedBeforeAccepting?: boolean;
}
```

### Documentation Output

```typescript
interface ExtractedDocumentation {
  summary: string;
  purpose: string;
  approach: string;
  decisions: Decision[];
  alternatives: string[];
  caveats: string[];
  testingNotes?: string;
  performanceNotes?: string;
  securityNotes?: string;
}

interface Decision {
  description: string;
  rationale: string;
  alternatives_considered: string[];
  timestamp: Date;
}
```

## Required Integration Points

### Level 1: Basic Export (Minimum)

```typescript
interface BasicIntegration {
  // Export current conversation
  exportConversation(): Conversation;
  
  // Export accepted code changes
  exportAcceptedChanges(): AcceptedCode[];
}
```

**Implementation Example (Aider)**:
```python
# In aider/main.py
def export_session(self):
    return {
        "conversation": self.messages,
        "changes": self.applied_changes,
        "metadata": {
            "tool": "aider",
            "version": __version__,
            "model": self.model_name
        }
    }
```

### Level 2: Real-time Hooks

```typescript
interface RealtimeIntegration extends BasicIntegration {
  // Fired when code is generated
  onCodeGenerated(callback: (code: CodeChange, context: Message[]) => void): void;
  
  // Fired when code is accepted
  onCodeAccepted(callback: (code: AcceptedCode) => void): void;
  
  // Fired when code is rejected/modified
  onCodeRejected(callback: (code: CodeChange, reason?: string) => void): void;
  
  // Fired before commit
  onPreCommit(callback: () => CommitContext): void;
}
```

**Implementation Example (Cline)**:
```typescript
// In extension.ts
export class ClineAdaptiveDoc {
  constructor(private adaptiveDoc: AdaptiveDocAPI) {
    vscode.workspace.onDidSaveTextDocument((doc) => {
      if (this.isAIGenerated(doc)) {
        const context = this.getConversationContext();
        this.adaptiveDoc.captureContext(doc, context);
      }
    });
  }
}
```

### Level 3: Deep Integration

```typescript
interface DeepIntegration extends RealtimeIntegration {
  // Modify conversation based on documentation needs
  injectDocumentationPrompt(prompt: string): void;
  
  // Get suggested documentation based on conversation
  getSuggestedDocumentation(): ExtractedDocumentation;
  
  // Link code to conversation segments
  linkCodeToConversation(code: string): Message[];
  
  // Learn from outcomes
  reportOutcome(change: CodeChange, outcome: 'bug' | 'success' | 'refactored'): void;
}
```

## Standard Extraction Functions

These can be shared across all integrations:

```typescript
class DocumentationExtractor {
  static extractPurpose(conversation: Conversation): string {
    // Analyze first user message for intent
    const patterns = [
      /fix (.*)/i,
      /implement (.*)/i,
      /add (.*)/i,
      /refactor (.*)/i
    ];
    // ... extraction logic
  }
  
  static extractDecisions(conversation: Conversation): Decision[] {
    // Look for decision keywords
    const decisionMarkers = [
      'decided to', 'chose', 'went with', 
      'better to', 'instead of'
    ];
    // ... extraction logic
  }
  
  static generateCommitMessage(
    doc: ExtractedDocumentation,
    changes: CodeChange[]
  ): string {
    // Generate conventional commit message
    const type = this.inferCommitType(doc.purpose);
    const scope = this.inferScope(changes);
    const subject = this.summarize(doc.summary, 50);
    
    return `${type}(${scope}): ${subject}\n\n${doc.approach}`;
  }
}
```

## Language-Specific Adapters

For command-line tools like Aider:

### Python Adapter

```python
# adaptive_doc_adapter.py
class AdaptiveDocAdapter:
    def __init__(self, tool_name):
        self.tool_name = tool_name
        self.conversation = []
        self.changes = []
    
    def capture_message(self, role, content):
        self.conversation.append({
            'role': role,
            'content': content,
            'timestamp': datetime.now().isoformat()
        })
    
    def capture_change(self, file, diff):
        self.changes.append({
            'file': file,
            'diff': diff,
            'conversation_index': len(self.conversation) - 1
        })
    
    def export_session(self):
        return {
            'tool': self.tool_name,
            'conversation': self.conversation,
            'changes': self.changes
        }
    
    def generate_documentation(self):
        # Call extraction service
        return extract_documentation(self.export_session())
```

### TypeScript Adapter (VS Code)

```typescript
// adaptiveDocAdapter.ts
export class AdaptiveDocAdapter {
  private conversation: Message[] = [];
  private changes: CodeChange[] = [];
  
  constructor(private toolName: string) {}
  
  captureMessage(role: 'user' | 'assistant', content: string) {
    this.conversation.push({
      role,
      content,
      timestamp: new Date()
    });
  }
  
  captureChange(document: vscode.TextDocument, range: vscode.Range) {
    // Capture the change
  }
  
  async generateCommitMessage(): Promise<string> {
    const doc = await this.extractDocumentation();
    return DocumentationExtractor.generateCommitMessage(doc, this.changes);
  }
}
```

## Integration Testing

### Test Harness

```typescript
class IntegrationTest {
  static async testBasicExport(tool: BasicIntegration) {
    // Test conversation export
    const conversation = tool.exportConversation();
    assert(conversation.messages.length > 0);
    assert(conversation.metadata.tool);
    
    // Test change export
    const changes = tool.exportAcceptedChanges();
    assert(Array.isArray(changes));
  }
  
  static async testDocumentationQuality(tool: BasicIntegration) {
    const conversation = tool.exportConversation();
    const doc = DocumentationExtractor.extract(conversation);
    
    // Quality metrics
    assert(doc.purpose.length > 10);
    assert(doc.summary.length > 20);
    assert(doc.decisions.length >= 0);
  }
}
```

## Privacy & Security Requirements

### Required Controls

```typescript
interface PrivacyControls {
  // User must explicitly opt-in
  enableDocumentationCapture(enabled: boolean): void;
  
  // Ability to exclude sensitive files
  excludePatterns(patterns: string[]): void;
  
  // Sanitize before export
  sanitizeData(data: Conversation): Conversation;
  
  // Local-only processing option
  setProcessingMode(mode: 'local' | 'cloud'): void;
}
```

### Data Handling

```typescript
class SecureDataHandler {
  static sanitize(conversation: Conversation): Conversation {
    return {
      ...conversation,
      messages: conversation.messages.map(msg => ({
        ...msg,
        content: this.removeSensitiveData(msg.content)
      }))
    };
  }
  
  private static removeSensitiveData(content: string): string {
    // Remove API keys, passwords, etc.
    const patterns = [
      /api[_-]?key[\s=:]+[\w-]+/gi,
      /password[\s=:]+[\w-]+/gi,
      /token[\s=:]+[\w-]+/gi
    ];
    
    let sanitized = content;
    patterns.forEach(pattern => {
      sanitized = sanitized.replace(pattern, '[REDACTED]');
    });
    
    return sanitized;
  }
}
```

## Reference Implementation

See [`mvp-manual.md`](./mvp-manual.md) for a complete minimal implementation that any tool can adopt.

## Success Metrics

Tools implementing this API should track:

```typescript
interface IntegrationMetrics {
  conversations_exported: number;
  documentation_generated: number;
  commit_messages_used: number;
  user_satisfaction: number;  // 1-5 scale
  performance_impact: number;  // milliseconds added
}
```

---

*This specification is designed to be tool-agnostic and incrementally adoptable. Start with Level 1, prove value, then expand.*
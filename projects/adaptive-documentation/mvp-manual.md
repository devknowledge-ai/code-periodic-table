# MVP: Manual Documentation Capture

## Start Simple. Prove Value. Then Add Magic.

### The Hypothesis We Must Test First

**Can we prove that captured context is valuable BEFORE trying to capture it automatically?**

## Phase 1: The "Dumb" Button (Weeks 1-2)

### VS Code Extension - Manual Capture Only

```typescript
// The simplest possible implementation
class ManualDocCapture {
  constructor() {
    // Add a status bar button
    this.button = vscode.window.createStatusBarItem();
    this.button.text = "$(comment) Document This";
    this.button.command = "manualDoc.capture";
  }

  async captureDocumentation() {
    // Just a simple form
    const why = await vscode.window.showInputBox({
      prompt: "Why did you make this change?",
      placeHolder: "Fixed null pointer when user is deleted"
    });

    if (!why) return;

    // Save to a simple JSON file
    this.saveContext({
      timestamp: new Date(),
      file: vscode.window.activeTextEditor?.document.fileName,
      line: vscode.window.activeTextEditor?.selection.active.line,
      documentation: why,
      trigger: "manual_user_initiated"
    });

    // Track usage metrics
    this.telemetry.record("manual_capture_used");
  }
}
```

### Git Hook - Explicit Prompt

```bash
#!/bin/bash
# .git/hooks/pre-commit

echo "You changed 3+ files. Add context for your team? (y/n)"
read response

if [ "$response" = "y" ]; then
  echo "Brief explanation (one line):"
  read explanation
  echo "$explanation" > .git/COMMIT_CONTEXT
fi
```

### Metrics to Track

```python
metrics = {
    "button_clicks": 0,
    "documentation_provided": 0,
    "documentation_skipped": 0,
    "average_response_length": 0,
    "time_to_respond": [],
    "abandonment_rate": 0
}
```

## Phase 2: LLM Session Save (Weeks 3-4)

### Browser Extension for Web LLMs

```javascript
// For ChatGPT, Claude.ai, etc.
class LLMSessionCapture {
  captureSession() {
    // Add button to ChatGPT interface
    const button = document.createElement('button');
    button.textContent = 'Save to IDE';
    button.onclick = () => {
      const conversation = this.extractConversation();
      // Send to local VS Code via localhost server
      fetch('http://localhost:7659/save-session', {
        method: 'POST',
        body: JSON.stringify(conversation)
      });
    };
  }

  extractConversation() {
    // Parse the DOM to get conversation
    const messages = document.querySelectorAll('.message');
    return Array.from(messages).map(msg => ({
      role: msg.dataset.role,
      content: msg.textContent
    }));
  }
}
```

### Local IDE Server

```python
# Simple Flask server running in VS Code extension
from flask import Flask, request
app = Flask(__name__)

@app.route('/save-session', methods=['POST'])
def save_session():
    session = request.json
    # Link to currently open file
    link_to_active_file(session)
    return {"status": "saved"}
```

## Phase 3: Measurement (Weeks 5-6)

### Key Questions to Answer

1. **Adoption Rate**
   - What % of developers use the manual button at least once?
   - What % continue using it after 1 week?

2. **Value Validation**
   - Do code reviewers find the documentation helpful?
   - Can we correlate documented changes with fewer review questions?

3. **Friction Points**
   - Average time between prompt and response?
   - Abandonment rate when prompted?
   - Most common reason for not documenting?

### User Interviews

```markdown
## Interview Questions

1. "Why didn't you click the Document This button?"
   - [ ] Didn't notice it
   - [ ] In the middle of something
   - [ ] Didn't see the value
   - [ ] Change was self-explanatory

2. "What would make you more likely to document?"
   - [ ] Faster input method (voice?)
   - [ ] Better timing (when?)
   - [ ] More value demonstration
   - [ ] Team requirement

3. "Would you share your LLM conversations?"
   - [ ] Yes, automatically
   - [ ] Yes, but I want to review first
   - [ ] Only specific parts
   - [ ] Never
```

## Success Criteria for Continuing

### Minimum Viable Metrics

| Metric | Target | Abandon If Below |
|--------|--------|------------------|
| Week 1 Adoption | 20% try it | 5% |
| Week 2 Retention | 10% still using | 2% |
| Documentation Quality | 60% "useful" rating | 30% |
| User Sentiment | Neutral or positive | Strongly negative |

### Go/No-Go Decision Tree

```
IF manual_adoption > 10% THEN
  → Proceed to git hooks
  → Test batch prompting (end of day)
  → Prototype simple triggers
ELSE IF browser_extension_adoption > 20% THEN
  → Focus on LLM integration path
  → Abandon smart prompting
  → Build platform-specific tools
ELSE
  → Pivot entirely
  → Consider passive analysis only
  → Reduce accuracy claims
END
```

## The Honest Timeline

**Weeks 1-2**: Build manual capture  
**Weeks 3-4**: Add LLM session save  
**Weeks 5-6**: Measure and interview  
**Week 7**: Go/No-Go decision  

**Only if successful**:  
**Weeks 8-12**: Start researching "smart" triggering  
**Weeks 13-20**: Prototype adaptive timing  
**Weeks 21+**: The "magic" version  

## Key Insight

**We're testing the foundation before building the house.**

If developers won't manually document with a simple button, they definitely won't respond to "intelligent" prompts.

If they won't share LLM sessions via copy-paste, automatic capture is pointless.

Start with the simplest thing that could possibly work. Only add complexity after proving value.

---

*"Make it work, then make it smart, then make it magical."*
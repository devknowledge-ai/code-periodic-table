# VS Code Inline Warning Mockup

## Visual Design

```
┌─────────────────────────────────────────────────────────────┐
│ authentication.py                                    VS Code │
├─────────────────────────────────────────────────────────────┤
│ 23  def process_login(username, password):                  │
│ 24      user = database.get_user(username)                  │
│ 25      if user['password'] == hash(password):  ░░░░░░░░░░  │
│         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   │
│ 26          return create_session(user)                      │
│                                                               │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ ⚠️ Anvil: Potential null reference (High confidence)    │ │
│ │                                                          │ │
│ │ This pattern caused 3 previous crashes:                 │ │
│ │ • 2024-01-15: "Fix: Check if user exists"              │ │
│ │ • 2023-11-02: "Handle null user gracefully"            │ │
│ │ • 2023-08-19: "Bugfix: Login crash"                    │ │
│ │                                                          │ │
│ │ Previous fix by @sarah:                                 │ │
│ │ ┌──────────────────────────────────────────┐           │ │
│ │ │ if user and user.get('password'):         │           │ │
│ │ │     if user['password'] == hash(password):│           │ │
│ │ └──────────────────────────────────────────┘           │ │
│ │                                                          │ │
│ │ [Apply Fix] [View History] [Ignore] [Report Issue]      │ │
│ └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## Interaction States

### 1. Default State
- Code appears normal
- No visual distraction

### 2. Pattern Detected (Typing)
```python
user['password']  # As soon as typed
     ~~~~~~~~~~   # Subtle amber underline appears
```

### 3. Hover State
- After 500ms hover → Show detailed popup
- Popup appears below/above line (space permitting)
- Semi-transparent background
- Escape key or click outside dismisses

### 4. Click Actions

#### "Apply Fix"
```python
# Before
if user['password'] == hash(password):

# After (automatically applied)
if user and user.get('password') == hash(password):
```

#### "View History"
Opens sidebar with:
- Full commit history of this pattern
- Diffs showing previous fixes
- Developer notes/comments

#### "Ignore"
- Removes warning for this instance
- Logs feedback for threshold adjustment
- Option to ignore pattern globally

#### "Report Issue"
Quick form:
```
[ ] False positive - this is correct code
[ ] Wrong suggestion - different fix needed
[ ] Too aggressive - lower sensitivity
[ ] Other: ________________
```

## Visual Specifications

### Underline Styles
```css
.anvil-hint {
  border-bottom: 1px dotted #FFA500;
  opacity: 0.6;
}

.anvil-warning {
  border-bottom: 2px wavy #FFA500;
  opacity: 0.8;
}

.anvil-error {
  border-bottom: 2px solid #FF4444;
  opacity: 1.0;
}
```

### Popup Styling
```css
.anvil-popup {
  background: rgba(30, 30, 30, 0.95);
  border: 1px solid #FFA500;
  border-radius: 4px;
  padding: 12px;
  max-width: 500px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
  font-size: 13px;
}

.anvil-code-block {
  background: rgba(0, 0, 0, 0.3);
  padding: 8px;
  border-radius: 3px;
  font-family: 'Consolas', 'Monaco', monospace;
}
```

## Responsive Behavior

### Small Screens / Split Views
- Popup width adjusts (min: 300px, max: 500px)
- Buttons stack vertically if needed
- Code examples truncated with "..." if too long

### Keyboard Navigation
- `Tab` - Cycle through buttons
- `Enter` - Activate focused button
- `Escape` - Dismiss popup
- `Ctrl+Shift+A` - Show all Anvil warnings in file

## Animation

### Appearance
```css
@keyframes anvil-fade-in {
  from { opacity: 0; transform: translateY(-5px); }
  to { opacity: 1; transform: translateY(0); }
}

.anvil-popup {
  animation: anvil-fade-in 200ms ease-out;
}
```

### Underline Pulse (High Priority Only)
```css
@keyframes anvil-pulse {
  0%, 100% { opacity: 0.8; }
  50% { opacity: 1.0; }
}

.anvil-error {
  animation: anvil-pulse 2s infinite;
}
```

## Accessibility

### Screen Reader Support
```html
<div role="alert" aria-live="polite" aria-label="Anvil warning">
  <h4>Potential null reference detected</h4>
  <p>This pattern has caused 3 previous crashes in your codebase.</p>
  <div role="group" aria-label="Actions">
    <button aria-label="Apply suggested fix">Apply Fix</button>
    <button aria-label="View pattern history">View History</button>
    <button aria-label="Ignore this warning">Ignore</button>
  </div>
</div>
```

### Color Blind Support
- Don't rely on color alone
- Use icons: ⚠️ ❌ ℹ️
- Different underline styles (dotted, wavy, straight)

## Performance Considerations

- Detection runs debounced (500ms after typing stops)
- Popup content lazy-loaded
- History fetched only when requested
- Maximum 5 warnings shown simultaneously

## User Preferences

Settings available in VS Code preferences:
```json
{
  "anvil.enableInlineWarnings": true,
  "anvil.warningDelay": 500,
  "anvil.maxWarningsPerFile": 5,
  "anvil.confidenceThreshold": 0.7,
  "anvil.showPreviousFixes": true,
  "anvil.animationEnabled": true
}
```

---

## Implementation Notes

### VS Code Extension API
```typescript
// Register hover provider
vscode.languages.registerHoverProvider('python', {
  provideHover(document, position) {
    const pattern = detectPattern(document, position);
    if (pattern) {
      return new vscode.Hover(createAnvilWarning(pattern));
    }
  }
});

// Add decorations for underlines
const decorationType = vscode.window.createTextEditorDecorationType({
  borderBottom: '2px wavy #FFA500'
});
```

### React Component Structure
```jsx
<AnvilWarning>
  <WarningHeader confidence={0.85} />
  <PreviousIncidents incidents={incidents} />
  <SuggestedFix code={fixCode} author="sarah" />
  <ActionButtons 
    onApply={handleApply}
    onIgnore={handleIgnore}
    onReport={handleReport}
  />
</AnvilWarning>
```

---

**Next Step**: Implement this mockup as working VS Code extension UI
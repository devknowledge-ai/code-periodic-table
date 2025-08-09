# Anvil UI/UX Mockups

Visual designs for how Anvil integrates into developer workflows.

## Core Interaction Principles

1. **Non-intrusive**: Never block the developer's flow
2. **Contextual**: Show information when and where needed
3. **Actionable**: Every warning has a clear resolution
4. **Learnable**: System improves from developer feedback

## Mockup Gallery

### 1. Inline Warning (VS Code)
![Inline Warning](./vscode-inline-warning.md)

**Scenario**: Developer writes code that matches a known bug pattern  
**Interaction**: Subtle underline appears, hovering shows details  
**Actions**: View previous fix, ignore warning, adjust sensitivity  

### 2. Sidebar Panel
![Sidebar Panel](./vscode-sidebar.md)

**Purpose**: Overview of all patterns in current file  
**Features**: 
- List of detected patterns
- Confidence scores
- Quick fixes
- History of similar issues

### 3. Git Commit Warning
![Commit Warning](./git-commit-warning.md)

**Scenario**: About to commit code with detected patterns  
**Options**:
- Proceed anyway
- Review warnings
- Auto-fix simple patterns

### 4. Feedback Widget
![Feedback Widget](./feedback-widget.md)

**Purpose**: Improve detection accuracy  
**Simple Interface**:
- "This was helpful" 👍
- "False positive" 👎
- "Report new pattern"

### 5. Configuration UI
![Configuration](./configuration-ui.md)

**Settings**:
- Sensitivity levels per pattern type
- Ignore rules
- Team-specific preferences
- Privacy controls

## Interaction Flow

```
Developer writes code
        ↓
Anvil detects pattern (100ms)
        ↓
Subtle visual indicator
        ↓
Developer hovers (optional)
        ↓
Contextual information shown
        ↓
Developer takes action:
├── Fixes the issue → Anvil learns
├── Ignores warning → Threshold adjusted
└── Reports false positive → Pattern refined
```

## Design Specifications

### Color Palette
- Warning: `#FFA500` (Amber - noticeable but not alarming)
- Error: `#FF4444` (Red - critical issues only)
- Success: `#00C851` (Green - pattern fixed)
- Info: `#33B5E5` (Blue - neutral information)

### Warning Levels
1. **Hint** (dotted underline): Low confidence, FYI only
2. **Warning** (wavy underline): Moderate confidence, should review
3. **Error** (straight underline): High confidence, likely bug

### Timing
- Detection: <100ms after typing stops
- Popup: 500ms hover delay
- Auto-dismiss: Never (user controls)

## Mockup Implementation Status

| Mockup | Status | Designer | Developer |
|--------|--------|----------|-----------|
| Inline Warning | ✅ Designed | @jane | Needed |
| Sidebar Panel | 🎨 In Progress | @jane | - |
| Commit Warning | 📋 Planned | Needed | - |
| Feedback Widget | 📋 Planned | Needed | - |
| Configuration UI | 📋 Planned | Needed | - |

## How to Contribute Mockups

1. **Designers**: Create mockups using Figma/Sketch
2. **Developers**: Implement as VS Code extension UI
3. **Users**: Provide feedback on usability

### Tools We Use
- Figma for design mockups
- VS Code Extension API for implementation
- Storybook for component development

## Accessibility Requirements

- Keyboard navigable
- Screen reader compatible
- High contrast mode support
- Configurable visual indicators

## User Research Findings

From developer interviews:
- **86%** want inline warnings (not popups)
- **72%** prefer hover for details (not automatic)
- **91%** need one-click dismissal
- **67%** want to see the previous fix

## Next Steps

1. Complete remaining mockups
2. Build interactive prototype
3. User test with 10 developers
4. Iterate based on feedback
5. Implement in VS Code extension

---

**Want to help design the UI?** [Join the discussion →](https://github.com/devknowledge-ai/anvil/discussions/ui-ux)
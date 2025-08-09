#!/usr/bin/env python3
"""
Prototype: LLM Context Capture for Adaptive Documentation
Extracts documentation from LLM-assisted coding sessions
"""

import json
import re
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum
import hashlib


class LLMTool(Enum):
    """Supported LLM tools"""
    CLAUDE_CODE = "claude_code"
    GITHUB_COPILOT = "github_copilot"
    CHATGPT = "chatgpt"
    CURSOR = "cursor"
    CODEIUM = "codeium"


@dataclass
class ConversationExchange:
    """Single exchange in conversation"""
    role: str  # 'user' or 'assistant'
    content: str
    timestamp: datetime
    has_code: bool = False
    code_blocks: List[str] = None


@dataclass
class ExtractedContext:
    """Extracted documentation context"""
    summary: str
    purpose: str
    approach: str
    decisions: List[Dict]
    alternatives: List[str]
    caveats: List[str]
    test_approach: Optional[str] = None


class LLMContextCapture:
    """Captures and processes LLM coding sessions"""
    
    def __init__(self):
        self.intent_patterns = [
            r"[Ii] need to (.*?) because (.*)",
            r"[Tt]he problem is (.*)",
            r"[Ww]e want to (.*?) in order to (.*)",
            r"[Ff]ix (.*?) that is causing (.*)",
            r"[Ii]mplement (.*?) for (.*)",
            r"[Aa]dd (.*?) to (.*)",
            r"[Cc]reate (.*?) that (.*)"
        ]
        
        self.decision_markers = [
            "should we", "better to", "i chose", "let's go with",
            "instead of", "rather than", "preferred", "decided to"
        ]
        
        self.alternative_markers = [
            "alternatively", "another option", "could also",
            "considered", "thought about", "other approach"
        ]
    
    def capture_session(self, session_file: str) -> Dict:
        """Capture and process an LLM session"""
        with open(session_file, 'r') as f:
            session_data = json.load(f)
        
        conversation = self.parse_conversation(session_data)
        context = self.extract_context(conversation)
        code_links = self.link_code_to_context(conversation)
        
        return {
            'session_id': self.generate_session_id(session_data),
            'timestamp': datetime.now().isoformat(),
            'tool': session_data.get('tool', 'unknown'),
            'conversation_summary': context.summary,
            'extracted_context': context.__dict__,
            'code_context_links': code_links,
            'metadata': self.extract_metadata(session_data)
        }
    
    def parse_conversation(self, session_data: Dict) -> List[ConversationExchange]:
        """Parse the conversation into structured exchanges"""
        exchanges = []
        
        for message in session_data.get('messages', []):
            exchange = ConversationExchange(
                role=message['role'],
                content=message['content'],
                timestamp=datetime.fromisoformat(message.get('timestamp', datetime.now().isoformat())),
                has_code=self.has_code_block(message['content']),
                code_blocks=self.extract_code_blocks(message['content'])
            )
            exchanges.append(exchange)
        
        return exchanges
    
    def extract_context(self, conversation: List[ConversationExchange]) -> ExtractedContext:
        """Extract structured documentation from conversation"""
        return ExtractedContext(
            summary=self.generate_summary(conversation),
            purpose=self.extract_purpose(conversation),
            approach=self.extract_approach(conversation),
            decisions=self.extract_decisions(conversation),
            alternatives=self.extract_alternatives(conversation),
            caveats=self.extract_caveats(conversation),
            test_approach=self.extract_test_approach(conversation)
        )
    
    def extract_purpose(self, conversation: List[ConversationExchange]) -> str:
        """Extract the 'why' from the conversation"""
        for exchange in conversation:
            if exchange.role == 'user':
                for pattern in self.intent_patterns:
                    match = re.search(pattern, exchange.content, re.IGNORECASE)
                    if match:
                        return self.clean_purpose(match.group(0))
        
        # Fallback: use first user message
        for exchange in conversation:
            if exchange.role == 'user':
                return self.summarize_intent(exchange.content)
        
        return "Purpose not explicitly stated"
    
    def extract_approach(self, conversation: List[ConversationExchange]) -> str:
        """Extract the implementation approach"""
        approach_keywords = ['implement', 'approach', 'solution', 'using', 'by']
        
        for exchange in conversation:
            if exchange.role == 'assistant':
                for keyword in approach_keywords:
                    if keyword in exchange.content.lower():
                        # Extract the sentence containing the keyword
                        sentences = exchange.content.split('.')
                        for sentence in sentences:
                            if keyword in sentence.lower():
                                return sentence.strip()
        
        return "Standard implementation approach"
    
    def extract_decisions(self, conversation: List[ConversationExchange]) -> List[Dict]:
        """Extract key decisions made during development"""
        decisions = []
        
        for exchange in conversation:
            content_lower = exchange.content.lower()
            for marker in self.decision_markers:
                if marker in content_lower:
                    decision = {
                        'type': 'design_decision' if exchange.role == 'assistant' else 'requirement_decision',
                        'context': self.extract_surrounding_context(exchange.content, marker),
                        'actor': exchange.role,
                        'timestamp': exchange.timestamp.isoformat()
                    }
                    decisions.append(decision)
        
        return decisions
    
    def extract_alternatives(self, conversation: List[ConversationExchange]) -> List[str]:
        """Extract alternative approaches discussed"""
        alternatives = []
        
        for exchange in conversation:
            for marker in self.alternative_markers:
                if marker in exchange.content.lower():
                    # Extract the sentence containing the alternative
                    sentences = exchange.content.split('.')
                    for sentence in sentences:
                        if marker in sentence.lower():
                            alternatives.append(sentence.strip())
        
        return alternatives
    
    def extract_caveats(self, conversation: List[ConversationExchange]) -> List[str]:
        """Extract warnings, limitations, and caveats"""
        caveat_keywords = [
            'warning', 'note', 'caution', 'limitation', 'caveat',
            'be aware', 'keep in mind', 'important', 'however'
        ]
        caveats = []
        
        for exchange in conversation:
            if exchange.role == 'assistant':
                for keyword in caveat_keywords:
                    if keyword in exchange.content.lower():
                        sentences = exchange.content.split('.')
                        for sentence in sentences:
                            if keyword in sentence.lower():
                                caveats.append(sentence.strip())
        
        return caveats
    
    def extract_test_approach(self, conversation: List[ConversationExchange]) -> Optional[str]:
        """Extract testing approach if discussed"""
        test_keywords = ['test', 'verify', 'validate', 'check', 'ensure']
        
        for exchange in conversation:
            for keyword in test_keywords:
                if keyword in exchange.content.lower():
                    sentences = exchange.content.split('.')
                    for sentence in sentences:
                        if keyword in sentence.lower() and len(sentence) > 20:
                            return sentence.strip()
        
        return None
    
    def link_code_to_context(self, conversation: List[ConversationExchange]) -> List[Dict]:
        """Link code blocks to their generating context"""
        links = []
        
        for i, exchange in enumerate(conversation):
            if exchange.has_code and exchange.code_blocks:
                for code_block in exchange.code_blocks:
                    # Find the user request that led to this code
                    request_context = self.find_preceding_request(conversation, i)
                    
                    link = {
                        'code_fingerprint': self.generate_code_fingerprint(code_block),
                        'exchange_index': i,
                        'request_context': request_context,
                        'explanation_context': self.extract_code_explanation(exchange.content, code_block),
                        'timestamp': exchange.timestamp.isoformat()
                    }
                    links.append(link)
        
        return links
    
    # Helper methods
    
    def has_code_block(self, content: str) -> bool:
        """Check if content contains code blocks"""
        return '```' in content or 'def ' in content or 'function ' in content
    
    def extract_code_blocks(self, content: str) -> List[str]:
        """Extract code blocks from content"""
        blocks = []
        
        # Extract markdown code blocks
        pattern = r'```[\w]*\n(.*?)\n```'
        matches = re.findall(pattern, content, re.DOTALL)
        blocks.extend(matches)
        
        # Extract inline code snippets (if substantial)
        inline_pattern = r'`([^`]{20,})`'
        inline_matches = re.findall(inline_pattern, content)
        blocks.extend(inline_matches)
        
        return blocks
    
    def generate_session_id(self, session_data: Dict) -> str:
        """Generate unique session ID"""
        content = json.dumps(session_data)
        return hashlib.sha256(content.encode()).hexdigest()[:12]
    
    def generate_code_fingerprint(self, code: str) -> str:
        """Generate fingerprint for code block"""
        # Remove whitespace and comments for consistent fingerprinting
        normalized = re.sub(r'\s+', '', code)
        normalized = re.sub(r'#.*', '', normalized)
        return hashlib.sha256(normalized.encode()).hexdigest()[:8]
    
    def extract_metadata(self, session_data: Dict) -> Dict:
        """Extract session metadata"""
        return {
            'message_count': len(session_data.get('messages', [])),
            'duration': session_data.get('duration'),
            'model': session_data.get('model', 'unknown'),
            'successful': session_data.get('successful', True)
        }
    
    def generate_summary(self, conversation: List[ConversationExchange]) -> str:
        """Generate conversation summary"""
        if not conversation:
            return "Empty conversation"
        
        # Use first user message as basis for summary
        for exchange in conversation:
            if exchange.role == 'user':
                return f"Session about: {exchange.content[:100]}..."
        
        return "Development session"
    
    def clean_purpose(self, text: str) -> str:
        """Clean and format purpose text"""
        # Remove common prefixes
        text = re.sub(r'^[Ii] need to ', '', text)
        text = re.sub(r'^[Ww]e want to ', '', text)
        
        # Capitalize first letter
        if text:
            text = text[0].upper() + text[1:]
        
        return text
    
    def summarize_intent(self, text: str) -> str:
        """Summarize user intent from first message"""
        # Take first sentence or first 100 chars
        first_sentence = text.split('.')[0]
        if len(first_sentence) > 100:
            return first_sentence[:97] + "..."
        return first_sentence
    
    def extract_surrounding_context(self, text: str, keyword: str) -> str:
        """Extract context around a keyword"""
        sentences = text.split('.')
        for sentence in sentences:
            if keyword in sentence.lower():
                return sentence.strip()
        return ""
    
    def find_preceding_request(self, conversation: List[ConversationExchange], index: int) -> str:
        """Find the user request that preceded this response"""
        for i in range(index - 1, -1, -1):
            if conversation[i].role == 'user':
                return conversation[i].content[:200]
        return "No preceding request found"
    
    def extract_code_explanation(self, content: str, code: str) -> str:
        """Extract explanation for specific code block"""
        # Look for explanation before or after code block
        lines = content.split('\n')
        code_start = None
        
        for i, line in enumerate(lines):
            if code[:50] in line:  # Find where code starts
                code_start = i
                break
        
        if code_start is not None:
            # Look for explanation in surrounding lines
            if code_start > 0 and lines[code_start - 1]:
                return lines[code_start - 1]
            elif code_start < len(lines) - 1 and lines[code_start + 1]:
                return lines[code_start + 1]
        
        return "Implementation code"


class DocumentationGenerator:
    """Generate documentation from extracted context"""
    
    def generate_commit_message(self, context: ExtractedContext) -> str:
        """Generate git commit message from context"""
        # Type of change
        if 'fix' in context.purpose.lower():
            prefix = 'fix'
        elif 'add' in context.purpose.lower() or 'implement' in context.purpose.lower():
            prefix = 'feat'
        elif 'refactor' in context.purpose.lower():
            prefix = 'refactor'
        else:
            prefix = 'chore'
        
        # Generate message
        message = f"{prefix}: {context.purpose[:50]}"
        
        if context.approach:
            message += f"\n\n{context.approach}"
        
        if context.alternatives:
            message += f"\n\nAlternatives considered:\n"
            for alt in context.alternatives[:3]:
                message += f"- {alt}\n"
        
        message += "\n\n[Generated from LLM session]"
        
        return message
    
    def generate_code_comment(self, context: ExtractedContext) -> str:
        """Generate code comment from context"""
        comment = f"""
    Purpose: {context.purpose}
    Approach: {context.approach}
    """
        
        if context.caveats:
            comment += f"    Note: {context.caveats[0]}\n"
        
        if context.test_approach:
            comment += f"    Testing: {context.test_approach}\n"
        
        comment += "    Source: LLM-assisted development"
        
        return comment
    
    def generate_markdown_doc(self, context: ExtractedContext) -> str:
        """Generate markdown documentation"""
        doc = f"""# {context.summary}

## Purpose
{context.purpose}

## Implementation Approach
{context.approach}
"""
        
        if context.decisions:
            doc += "\n## Key Decisions\n"
            for decision in context.decisions:
                doc += f"- {decision['context']}\n"
        
        if context.alternatives:
            doc += "\n## Alternatives Considered\n"
            for alt in context.alternatives:
                doc += f"- {alt}\n"
        
        if context.caveats:
            doc += "\n## Important Notes\n"
            for caveat in context.caveats:
                doc += f"- {caveat}\n"
        
        if context.test_approach:
            doc += f"\n## Testing\n{context.test_approach}\n"
        
        doc += "\n---\n*Documentation extracted from LLM-assisted development session*"
        
        return doc


def main():
    """Example usage"""
    
    # Example session data (would come from actual LLM tool)
    example_session = {
        'tool': 'claude_code',
        'model': 'claude-3-opus',
        'messages': [
            {
                'role': 'user',
                'content': 'I need to add rate limiting to our API endpoints because we\'re seeing some IPs making 1000+ requests per minute',
                'timestamp': '2024-01-15T10:00:00'
            },
            {
                'role': 'assistant',
                'content': '''I'll help you implement rate limiting for your API endpoints. Given the high request volume you're seeing, I'll use a token bucket algorithm instead of a simple fixed window approach, as it handles burst traffic better.

Here's the implementation:

```python
def rate_limit(tokens_per_second=10, bucket_size=100):
    # Token bucket implementation
    pass
```

Note that this approach has some memory overhead compared to fixed window, but provides smoother rate limiting. Alternatively, you could use a sliding window approach, but that has even higher memory requirements.

Important: Make sure to store the rate limit state in Redis or similar for distributed systems.''',
                'timestamp': '2024-01-15T10:01:00'
            }
        ]
    }
    
    # Save example session to file
    with open('example_session.json', 'w') as f:
        json.dump(example_session, f)
    
    # Capture and process the session
    capturer = LLMContextCapture()
    result = capturer.capture_session('example_session.json')
    
    print("=== Captured Context ===")
    print(json.dumps(result, indent=2, default=str))
    
    # Generate documentation
    context = ExtractedContext(**result['extracted_context'])
    generator = DocumentationGenerator()
    
    print("\n=== Generated Commit Message ===")
    print(generator.generate_commit_message(context))
    
    print("\n=== Generated Code Comment ===")
    print(generator.generate_code_comment(context))
    
    print("\n=== Generated Documentation ===")
    print(generator.generate_markdown_doc(context))


if __name__ == "__main__":
    main()
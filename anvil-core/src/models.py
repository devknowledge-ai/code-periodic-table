"""
Shared data models for the Anvil Suite
"""

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Dict, Any
from enum import Enum


class Language(Enum):
    """Supported programming languages"""
    PYTHON = "python"
    JAVASCRIPT = "javascript"
    TYPESCRIPT = "typescript"
    JAVA = "java"
    GO = "go"
    RUST = "rust"
    CPP = "cpp"


@dataclass
class FileLocation:
    """Location of code in a file"""
    file: str
    start_line: int
    end_line: int
    start_col: Optional[int] = None
    end_col: Optional[int] = None


@dataclass
class CodeBlock:
    """A block of code with metadata"""
    content: str
    language: Language
    fingerprint: str
    location: Optional[FileLocation] = None
    ast: Optional[Any] = None  # Language-specific AST
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


@dataclass
class Documentation:
    """Documentation extracted from various sources"""
    summary: str
    purpose: str
    approach: Optional[str] = None
    decisions: List[Dict[str, str]] = None
    alternatives: List[str] = None
    caveats: List[str] = None
    source: str = "unknown"  # 'manual', 'llm', 'comment', 'commit'
    confidence: float = 0.0
    
    def __post_init__(self):
        if self.decisions is None:
            self.decisions = []
        if self.alternatives is None:
            self.alternatives = []
        if self.caveats is None:
            self.caveats = []


@dataclass
class GitCommit:
    """Git commit information"""
    hash: str
    message: str
    author: str
    timestamp: datetime
    files_changed: List[str]
    additions: int
    deletions: int
    parent_hashes: List[str] = None
    
    def __post_init__(self):
        if self.parent_hashes is None:
            self.parent_hashes = []


@dataclass
class CodeChange:
    """A change to code"""
    file: str
    language: Language
    before: str
    after: str
    diff: str
    commit: Optional[GitCommit] = None
    documentation: Optional[Documentation] = None
    fingerprint_before: Optional[str] = None
    fingerprint_after: Optional[str] = None


@dataclass
class Pattern:
    """A code pattern detected across the codebase"""
    name: str
    description: str
    fingerprint: str
    occurrences: List[FileLocation]
    category: str  # 'bug', 'antipattern', 'convention', 'optimization'
    confidence: float
    first_seen: datetime
    last_seen: datetime
    fix_commits: List[GitCommit] = None
    
    def __post_init__(self):
        if self.fix_commits is None:
            self.fix_commits = []


@dataclass
class Comment:
    """A comment attached to code"""
    content: str
    attached_to: str  # fingerprint
    created_at: datetime
    updated_at: Optional[datetime] = None
    author: Optional[str] = None
    type: str = "inline"  # 'inline', 'block', 'doc', 'todo'
    tags: List[str] = None
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = []


@dataclass
class NullCheckPattern:
    """Pattern for null/None checking (used by Anvil Guard)"""
    function_name: str
    can_return_null: bool
    null_check_required: bool
    confidence: float
    evidence: List[GitCommit]
    last_updated: datetime


@dataclass
class LLMConversation:
    """Conversation with an LLM (used by Adaptive Documentation)"""
    id: str
    tool: str  # 'aider', 'cline', 'roo-coder', etc.
    messages: List[Dict[str, Any]]
    code_generated: List[CodeBlock]
    documentation_extracted: Optional[Documentation] = None
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()


@dataclass
class TeamKnowledge:
    """Aggregated team knowledge from multiple sources"""
    patterns: List[Pattern]
    conventions: Dict[str, str]
    common_bugs: List[Pattern]
    documentation: Dict[str, Documentation]  # fingerprint -> doc
    last_updated: datetime
    
    def add_pattern(self, pattern: Pattern):
        """Add a new pattern to team knowledge"""
        self.patterns.append(pattern)
        self.last_updated = datetime.now()
    
    def get_documentation_for(self, fingerprint: str) -> Optional[Documentation]:
        """Get documentation for a code fingerprint"""
        return self.documentation.get(fingerprint)
"""
Anvil Core - Shared foundation for the Anvil Suite

⚠️ IMPORTANT: This is a skeleton implementation with incomplete functionality.
Most methods are stubs or basic implementations that need significant work.
See PROJECT_STATUS.md for the actual state of the project.
"""

__version__ = "0.1.0"

# Make key components easily importable
from .fingerprinting import CodeFingerprint
from .parsers import get_parser
from .git import GitAnalyzer
from .models import (
    CodeBlock,
    Documentation,
    GitCommit,
    CodeChange,
    Pattern,
    Comment
)

__all__ = [
    'CodeFingerprint',
    'get_parser',
    'GitAnalyzer',
    'CodeBlock',
    'Documentation',
    'GitCommit',
    'CodeChange',
    'Pattern',
    'Comment',
]
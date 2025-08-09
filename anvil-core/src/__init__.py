"""
Anvil Core - Shared foundation for the Anvil Suite
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
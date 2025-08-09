"""
Language-specific AST parsers for the Anvil Suite
"""

import ast
from typing import Any, List, Dict, Optional
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class FunctionInfo:
    """Information about a function"""
    name: str
    parameters: List[str]
    start_line: int
    end_line: int
    docstring: Optional[str] = None
    complexity: int = 0


@dataclass
class ClassInfo:
    """Information about a class"""
    name: str
    methods: List[FunctionInfo]
    base_classes: List[str]
    start_line: int
    end_line: int
    docstring: Optional[str] = None


class BaseParser(ABC):
    """Abstract base class for language parsers"""
    
    @abstractmethod
    def parse(self, code: str) -> Any:
        """Parse code into AST"""
        pass
    
    @abstractmethod
    def extract_functions(self, tree: Any) -> List[FunctionInfo]:
        """Extract function information from AST"""
        pass
    
    @abstractmethod
    def extract_classes(self, tree: Any) -> List[ClassInfo]:
        """Extract class information from AST"""
        pass
    
    @abstractmethod
    def get_complexity(self, tree: Any) -> int:
        """Calculate cyclomatic complexity"""
        pass


class PythonParser(BaseParser):
    """Parser for Python code using built-in ast module"""
    
    def parse(self, code: str) -> ast.AST:
        """Parse Python code into AST"""
        return ast.parse(code)
    
    def extract_functions(self, tree: ast.AST) -> List[FunctionInfo]:
        """Extract all functions from Python AST"""
        functions = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_info = FunctionInfo(
                    name=node.name,
                    parameters=[arg.arg for arg in node.args.args],
                    start_line=node.lineno,
                    end_line=node.end_lineno or node.lineno,
                    docstring=ast.get_docstring(node),
                    complexity=self._calculate_complexity(node)
                )
                functions.append(func_info)
        
        return functions
    
    def extract_classes(self, tree: ast.AST) -> List[ClassInfo]:
        """Extract all classes from Python AST"""
        classes = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                methods = []
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        method_info = FunctionInfo(
                            name=item.name,
                            parameters=[arg.arg for arg in item.args.args],
                            start_line=item.lineno,
                            end_line=item.end_lineno or item.lineno,
                            docstring=ast.get_docstring(item)
                        )
                        methods.append(method_info)
                
                class_info = ClassInfo(
                    name=node.name,
                    methods=methods,
                    base_classes=[self._get_name(base) for base in node.bases],
                    start_line=node.lineno,
                    end_line=node.end_lineno or node.lineno,
                    docstring=ast.get_docstring(node)
                )
                classes.append(class_info)
        
        return classes
    
    def get_complexity(self, tree: ast.AST) -> int:
        """Calculate cyclomatic complexity of Python code"""
        return self._calculate_complexity(tree)
    
    def _calculate_complexity(self, node: ast.AST) -> int:
        """Calculate cyclomatic complexity for a node"""
        complexity = 1
        
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For)):
                complexity += 1
            elif isinstance(child, ast.ExceptHandler):
                complexity += 1
            elif isinstance(child, ast.BoolOp):
                complexity += len(child.values) - 1
        
        return complexity
    
    def _get_name(self, node: ast.AST) -> str:
        """Extract name from various AST node types"""
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            return f"{self._get_name(node.value)}.{node.attr}"
        else:
            return str(node)
    
    def find_patterns(self, tree: ast.AST, pattern_type: str) -> List[ast.AST]:
        """Find specific patterns in the AST"""
        patterns = []
        
        if pattern_type == 'null_check':
            # Find None comparisons
            for node in ast.walk(tree):
                if isinstance(node, ast.Compare):
                    for op in node.ops:
                        if isinstance(op, (ast.Is, ast.IsNot)):
                            for comp in node.comparators:
                                if isinstance(comp, ast.Constant) and comp.value is None:
                                    patterns.append(node)
        
        elif pattern_type == 'exception_handling':
            # Find try-except blocks
            for node in ast.walk(tree):
                if isinstance(node, ast.Try):
                    patterns.append(node)
        
        return patterns


class JavaScriptParser(BaseParser):
    """Parser for JavaScript/TypeScript code"""
    
    def __init__(self):
        # Note: Would use tree-sitter or similar for real implementation
        self.parser = None
    
    def parse(self, code: str) -> Any:
        """Parse JavaScript code into AST"""
        # Placeholder implementation
        return {"type": "Program", "body": []}
    
    def extract_functions(self, tree: Any) -> List[FunctionInfo]:
        """Extract functions from JavaScript AST"""
        # Placeholder implementation
        return []
    
    def extract_classes(self, tree: Any) -> List[ClassInfo]:
        """Extract classes from JavaScript AST"""
        # Placeholder implementation
        return []
    
    def get_complexity(self, tree: Any) -> int:
        """Calculate complexity of JavaScript code"""
        # Placeholder implementation
        return 1


# Parser factory
_PARSERS = {
    'python': PythonParser,
    'javascript': JavaScriptParser,
    'typescript': JavaScriptParser,  # Use same parser for now
}


def get_parser(language: str) -> BaseParser:
    """
    Get a parser for the specified language
    
    Args:
        language: Programming language name
        
    Returns:
        Parser instance for the language
        
    Raises:
        ValueError: If language is not supported
    """
    language = language.lower()
    
    if language not in _PARSERS:
        raise ValueError(f"Unsupported language: {language}. "
                        f"Supported: {list(_PARSERS.keys())}")
    
    parser_class = _PARSERS[language]
    return parser_class()


def detect_language(code: str, filename: Optional[str] = None) -> str:
    """
    Attempt to detect the programming language
    
    Args:
        code: Source code
        filename: Optional filename with extension
        
    Returns:
        Detected language name
    """
    if filename:
        ext = filename.split('.')[-1].lower()
        ext_map = {
            'py': 'python',
            'js': 'javascript',
            'ts': 'typescript',
            'java': 'java',
            'go': 'go',
            'rs': 'rust',
            'cpp': 'cpp',
            'c': 'c',
        }
        if ext in ext_map:
            return ext_map[ext]
    
    # Simple heuristics
    if 'def ' in code or 'import ' in code or 'class ' in code:
        return 'python'
    elif 'function ' in code or 'const ' in code or 'let ' in code:
        return 'javascript'
    elif 'public class' in code or 'private ' in code:
        return 'java'
    
    return 'unknown'
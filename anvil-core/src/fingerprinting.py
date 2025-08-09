"""
Semantic code fingerprinting algorithms
"""

import hashlib
import re
from typing import Optional, List, Tuple
import ast
from dataclasses import dataclass


@dataclass
class FingerprintOptions:
    """Options for fingerprint generation"""
    ignore_whitespace: bool = True
    ignore_comments: bool = True
    ignore_variable_names: bool = False
    ignore_string_literals: bool = False
    normalize_syntax: bool = True


class CodeFingerprint:
    """
    Generate semantic fingerprints for code blocks that survive refactoring
    """
    
    def __init__(self, options: Optional[FingerprintOptions] = None):
        self.options = options or FingerprintOptions()
    
    def generate(self, code: str, language: str = 'python') -> str:
        """
        Generate a fingerprint for a code block
        
        Args:
            code: The code to fingerprint
            language: Programming language (currently only Python supported)
            
        Returns:
            Hex string fingerprint
        """
        if language == 'python':
            return self._fingerprint_python(code)
        else:
            # Fallback to simple text-based fingerprinting
            return self._fingerprint_text(code)
    
    def _fingerprint_python(self, code: str) -> str:
        """Generate fingerprint for Python code using AST"""
        try:
            tree = ast.parse(code)
            normalized = self._normalize_python_ast(tree)
            return self._hash_string(ast.dump(normalized))
        except SyntaxError:
            # If parsing fails, fall back to text fingerprinting
            return self._fingerprint_text(code)
    
    def _normalize_python_ast(self, tree: ast.AST) -> ast.AST:
        """Normalize Python AST for consistent fingerprinting"""
        
        class Normalizer(ast.NodeTransformer):
            def __init__(self, options):
                self.options = options
                self.var_mapping = {}
                self.var_counter = 0
            
            def visit_Name(self, node):
                """Normalize variable names if requested"""
                if self.options.ignore_variable_names:
                    if node.id not in self.var_mapping:
                        self.var_mapping[node.id] = f"var_{self.var_counter}"
                        self.var_counter += 1
                    node.id = self.var_mapping[node.id]
                return node
            
            def visit_Constant(self, node):
                """Normalize string literals if requested"""
                if self.options.ignore_string_literals and isinstance(node.value, str):
                    node.value = "STRING"
                return node
        
        if self.options.normalize_syntax:
            normalizer = Normalizer(self.options)
            tree = normalizer.visit(tree)
        
        return tree
    
    def _fingerprint_text(self, code: str) -> str:
        """Simple text-based fingerprinting"""
        normalized = code
        
        if self.options.ignore_whitespace:
            # Remove extra whitespace but preserve structure
            normalized = re.sub(r'\s+', ' ', normalized)
            normalized = normalized.strip()
        
        if self.options.ignore_comments:
            # Remove common comment patterns
            normalized = re.sub(r'#.*$', '', normalized, flags=re.MULTILINE)
            normalized = re.sub(r'/\*.*?\*/', '', normalized, flags=re.DOTALL)
            normalized = re.sub(r'//.*$', '', normalized, flags=re.MULTILINE)
        
        return self._hash_string(normalized)
    
    def _hash_string(self, s: str) -> str:
        """Generate SHA-256 hash of a string"""
        return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]
    
    def similarity(self, fp1: str, fp2: str) -> float:
        """
        Calculate similarity between two fingerprints
        
        Returns:
            Float between 0.0 (different) and 1.0 (identical)
        """
        if fp1 == fp2:
            return 1.0
        
        # Simple character-based similarity for now
        # TODO: Implement more sophisticated similarity metrics
        matches = sum(c1 == c2 for c1, c2 in zip(fp1, fp2))
        return matches / max(len(fp1), len(fp2))
    
    def find_similar(self, target_fp: str, fingerprints: List[str], 
                    threshold: float = 0.8) -> List[Tuple[str, float]]:
        """
        Find fingerprints similar to target
        
        Args:
            target_fp: Target fingerprint
            fingerprints: List of fingerprints to search
            threshold: Minimum similarity (0.0 to 1.0)
            
        Returns:
            List of (fingerprint, similarity) tuples above threshold
        """
        results = []
        for fp in fingerprints:
            sim = self.similarity(target_fp, fp)
            if sim >= threshold:
                results.append((fp, sim))
        
        return sorted(results, key=lambda x: x[1], reverse=True)


class CrossLanguageFingerprint(CodeFingerprint):
    """
    Experimental: Generate fingerprints that work across languages
    """
    
    def generate_universal(self, code: str, language: str) -> str:
        """
        Generate a language-agnostic fingerprint
        
        This attempts to capture the semantic structure regardless of syntax
        """
        # Extract structural elements
        structure = self._extract_structure(code, language)
        
        # Create a normalized representation
        normalized = self._normalize_structure(structure)
        
        return self._hash_string(normalized)
    
    def _extract_structure(self, code: str, language: str) -> dict:
        """Extract language-agnostic structural elements"""
        structure = {
            'functions': [],
            'loops': 0,
            'conditionals': 0,
            'assignments': 0,
            'calls': []
        }
        
        # Language-specific extraction
        if language == 'python':
            try:
                tree = ast.parse(code)
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef):
                        structure['functions'].append(node.name)
                    elif isinstance(node, (ast.For, ast.While)):
                        structure['loops'] += 1
                    elif isinstance(node, ast.If):
                        structure['conditionals'] += 1
                    elif isinstance(node, ast.Assign):
                        structure['assignments'] += 1
                    elif isinstance(node, ast.Call):
                        if hasattr(node.func, 'id'):
                            structure['calls'].append(node.func.id)
            except:
                pass
        
        return structure
    
    def _normalize_structure(self, structure: dict) -> str:
        """Create a normalized string representation of structure"""
        parts = []
        
        if structure['functions']:
            parts.append(f"funcs:{','.join(sorted(structure['functions']))}")
        
        parts.append(f"loops:{structure['loops']}")
        parts.append(f"conds:{structure['conditionals']}")
        parts.append(f"assigns:{structure['assignments']}")
        
        if structure['calls']:
            # Only include unique calls
            unique_calls = sorted(set(structure['calls']))
            parts.append(f"calls:{','.join(unique_calls)}")
        
        return '|'.join(parts)
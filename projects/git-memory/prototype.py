#!/usr/bin/env python3
"""
Anvil Demo Prototype: Detect Repeated Bug Fixes in Git History

⚠️ THIS IS A CONCEPTUAL DEMO, NOT A WORKING PRODUCT

This simple script demonstrates the CONCEPT of detecting repeated patterns
by analyzing commit messages (not actual code). It's meant to illustrate
the idea, not provide real pattern detection functionality.

Real pattern detection would require:
- AST analysis of actual code changes
- Semantic fingerprinting
- Machine learning models
- Much more sophisticated algorithms

Usage:
    python detect_repeated_fixes.py /path/to/repo
"""

import sys
import os
import subprocess
import re
from collections import defaultdict
from datetime import datetime

class PatternDetector:
    """Simple pattern detection for repeated bug fixes"""
    
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.patterns = defaultdict(list)
        
    def analyze(self):
        """Main analysis pipeline"""
        print(f"Analyzing repository: {self.repo_path}")
        print("-" * 50)
        
        # Get commits that look like bug fixes
        fix_commits = self.get_fix_commits()
        print(f"Found {len(fix_commits)} bug fix commits")
        
        # Analyze each fix
        for commit_hash, message in fix_commits:
            self.analyze_commit(commit_hash, message)
        
        # Report findings
        self.report_patterns()
    
    def get_fix_commits(self):
        """Find commits that appear to be bug fixes"""
        # Keywords that indicate bug fixes
        fix_keywords = ['fix', 'bug', 'patch', 'resolve', 'crash', 'error', 'null']
        
        try:
            # Get commit history
            result = subprocess.run(
                ['git', 'log', '--oneline', '--no-merges', '-n', '500'],
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )
            
            fixes = []
            for line in result.stdout.split('\n'):
                if line:
                    # Check if commit message contains fix keywords
                    lower_line = line.lower()
                    if any(keyword in lower_line for keyword in fix_keywords):
                        parts = line.split(' ', 1)
                        if len(parts) == 2:
                            fixes.append((parts[0], parts[1]))
            
            return fixes
            
        except Exception as e:
            print(f"Error reading git history: {e}")
            return []
    
    def analyze_commit(self, commit_hash, message):
        """Analyze a single commit for patterns"""
        # Simple pattern recognition based on commit message
        patterns_found = []
        
        # Pattern 1: Null reference
        if any(word in message.lower() for word in ['null', 'undefined', 'none', 'missing']):
            patterns_found.append('null_reference')
            
        # Pattern 2: Race condition
        if any(word in message.lower() for word in ['race', 'concurrent', 'async', 'thread']):
            patterns_found.append('race_condition')
            
        # Pattern 3: Resource leak
        if any(word in message.lower() for word in ['leak', 'close', 'cleanup', 'release']):
            patterns_found.append('resource_leak')
            
        # Pattern 4: SQL/Injection
        if any(word in message.lower() for word in ['sql', 'injection', 'query', 'escape']):
            patterns_found.append('sql_injection')
        
        # Pattern 5: Authentication
        if any(word in message.lower() for word in ['auth', 'login', 'password', 'session']):
            patterns_found.append('authentication')
        
        # Store patterns with commit info
        for pattern in patterns_found:
            self.patterns[pattern].append({
                'hash': commit_hash,
                'message': message,
                'date': self.get_commit_date(commit_hash)
            })
    
    def get_commit_date(self, commit_hash):
        """Get the date of a commit"""
        try:
            result = subprocess.run(
                ['git', 'show', '-s', '--format=%ai', commit_hash],
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )
            return result.stdout.strip()
        except:
            return "Unknown"
    
    def report_patterns(self):
        """Report detected patterns"""
        print("\n" + "=" * 50)
        print("REPEATED BUG PATTERNS DETECTED:")
        print("=" * 50)
        
        if not self.patterns:
            print("No repeated patterns found. Your team is doing great!")
            return
        
        # Sort by frequency
        sorted_patterns = sorted(
            self.patterns.items(), 
            key=lambda x: len(x[1]), 
            reverse=True
        )
        
        for pattern_name, occurrences in sorted_patterns:
            if len(occurrences) > 1:  # Only show repeated patterns
                print(f"\n🔴 Pattern: {self.format_pattern_name(pattern_name)}")
                print(f"   Fixed {len(occurrences)} times")
                print(f"   First fix: {occurrences[-1]['date'][:10]}")
                print(f"   Last fix:  {occurrences[0]['date'][:10]}")
                print(f"   Recent fixes:")
                
                for fix in occurrences[:3]:  # Show last 3 fixes
                    print(f"   • {fix['hash'][:7]}: {fix['message'][:50]}")
                
                print(f"   Estimated time wasted: {len(occurrences) * 4} hours")
        
        # Summary
        total_repeated = sum(len(fixes) - 1 for fixes in self.patterns.values() if len(fixes) > 1)
        print("\n" + "=" * 50)
        print(f"SUMMARY: {total_repeated} bugs were fixed multiple times")
        print(f"Potential time saved with Anvil: {total_repeated * 4} hours")
        print("=" * 50)
    
    def format_pattern_name(self, pattern):
        """Format pattern name for display"""
        names = {
            'null_reference': 'Null Reference / Missing Value',
            'race_condition': 'Race Condition / Concurrency Issue',
            'resource_leak': 'Resource Leak / Unclosed Resource',
            'sql_injection': 'SQL Injection / Query Security',
            'authentication': 'Authentication / Session Issue'
        }
        return names.get(pattern, pattern.replace('_', ' ').title())


def main():
    """Main entry point"""
    if len(sys.argv) != 2:
        print("Usage: python detect_repeated_fixes.py /path/to/repo")
        print("\nExample: python detect_repeated_fixes.py ./my-project")
        sys.exit(1)
    
    repo_path = sys.argv[1]
    
    if not os.path.exists(repo_path):
        print(f"Error: Path '{repo_path}' does not exist")
        sys.exit(1)
    
    if not os.path.exists(os.path.join(repo_path, '.git')):
        print(f"Error: '{repo_path}' is not a git repository")
        sys.exit(1)
    
    # Run analysis
    detector = PatternDetector(repo_path)
    detector.analyze()
    
    print("\n✨ This is just a simple prototype.")
    print("The full Anvil will detect patterns in actual code changes,")
    print("not just commit messages, and provide real-time IDE warnings.")
    print("\nInterested? Join us: https://github.com/devknowledge-ai/anvil")


if __name__ == "__main__":
    main()
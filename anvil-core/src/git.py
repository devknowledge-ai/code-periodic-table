"""
Git repository operations and analysis
"""

import re
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
import subprocess
import json


@dataclass
class GitDiff:
    """Represents a git diff"""
    file: str
    additions: int
    deletions: int
    hunks: List[str]


class GitAnalyzer:
    """
    Efficient Git repository analysis
    """
    
    def __init__(self, repo_path: str):
        self.repo_path = repo_path
    
    def _run_git_command(self, args: List[str]) -> str:
        """Run a git command and return output"""
        cmd = ['git', '-C', self.repo_path] + args
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Git command failed: {e.stderr}")
    
    def get_commits(self, since: Optional[str] = None, 
                   until: Optional[str] = None,
                   max_count: int = 1000) -> List[Dict]:
        """
        Get commits from the repository
        
        Args:
            since: Start date (e.g., '3 months ago', '2024-01-01')
            until: End date
            max_count: Maximum number of commits to return
            
        Returns:
            List of commit dictionaries
        """
        args = ['log', '--format=format:%H|%an|%ae|%at|%s', f'--max-count={max_count}']
        
        if since:
            args.append(f'--since={since}')
        if until:
            args.append(f'--until={until}')
        
        output = self._run_git_command(args)
        commits = []
        
        for line in output.strip().split('\n'):
            if not line:
                continue
            
            parts = line.split('|', 4)
            if len(parts) >= 5:
                commits.append({
                    'hash': parts[0],
                    'author_name': parts[1],
                    'author_email': parts[2],
                    'timestamp': datetime.fromtimestamp(int(parts[3])),
                    'message': parts[4]
                })
        
        return commits
    
    def get_file_changes(self, file_path: str, max_commits: int = 100) -> List[Dict]:
        """
        Get the history of changes for a specific file
        
        Args:
            file_path: Path to the file
            max_commits: Maximum number of commits to analyze
            
        Returns:
            List of changes with commit info and diffs
        """
        args = ['log', '--follow', f'--max-count={max_commits}', 
                '--format=format:%H|%at|%s', '-p', '--', file_path]
        
        output = self._run_git_command(args)
        changes = []
        current_commit = None
        current_diff = []
        
        for line in output.split('\n'):
            if line.startswith('commit '):
                if current_commit and current_diff:
                    current_commit['diff'] = '\n'.join(current_diff)
                    changes.append(current_commit)
                    current_diff = []
                
                # Skip the 'commit' line, next line has our format
                continue
            
            elif '|' in line and not line.startswith(('+++', '---', '@@')):
                # This is our formatted commit info
                parts = line.split('|', 2)
                if len(parts) >= 3:
                    current_commit = {
                        'hash': parts[0],
                        'timestamp': datetime.fromtimestamp(int(parts[1])),
                        'message': parts[2],
                        'file': file_path
                    }
            
            elif current_commit:
                current_diff.append(line)
        
        # Don't forget the last commit
        if current_commit and current_diff:
            current_commit['diff'] = '\n'.join(current_diff)
            changes.append(current_commit)
        
        return changes
    
    def find_fix_patterns(self, keywords: Optional[List[str]] = None) -> List[Dict]:
        """
        Find commits that likely contain bug fixes
        
        Args:
            keywords: Keywords to search for (default: common fix keywords)
            
        Returns:
            List of commits that appear to be fixes
        """
        if keywords is None:
            keywords = ['fix', 'bug', 'patch', 'resolve', 'correct', 'repair']
        
        pattern = '|'.join(keywords)
        args = ['log', '--grep', pattern, '-i', 
                '--format=format:%H|%at|%s', '--max-count=500']
        
        output = self._run_git_command(args)
        fixes = []
        
        for line in output.strip().split('\n'):
            if not line:
                continue
            
            parts = line.split('|', 2)
            if len(parts) >= 3:
                fixes.append({
                    'hash': parts[0],
                    'timestamp': datetime.fromtimestamp(int(parts[1])),
                    'message': parts[2],
                    'type': self._classify_fix(parts[2])
                })
        
        return fixes
    
    def _classify_fix(self, message: str) -> str:
        """Classify the type of fix based on commit message"""
        message_lower = message.lower()
        
        if 'null' in message_lower or 'none' in message_lower:
            return 'null_reference'
        elif 'race' in message_lower or 'concurrent' in message_lower:
            return 'race_condition'
        elif 'memory' in message_lower or 'leak' in message_lower:
            return 'memory_issue'
        elif 'security' in message_lower or 'vulnerability' in message_lower:
            return 'security'
        elif 'performance' in message_lower or 'slow' in message_lower:
            return 'performance'
        else:
            return 'general'
    
    def get_diff(self, commit_hash: str) -> List[GitDiff]:
        """
        Get the diff for a specific commit
        
        Args:
            commit_hash: Git commit hash
            
        Returns:
            List of GitDiff objects
        """
        args = ['show', '--format=', '--numstat', commit_hash]
        output = self._run_git_command(args)
        
        diffs = []
        for line in output.strip().split('\n'):
            if not line:
                continue
            
            parts = line.split('\t')
            if len(parts) >= 3:
                try:
                    additions = int(parts[0]) if parts[0] != '-' else 0
                    deletions = int(parts[1]) if parts[1] != '-' else 0
                    file_path = parts[2]
                    
                    # Get the actual diff hunks
                    hunks = self._get_hunks(commit_hash, file_path)
                    
                    diffs.append(GitDiff(
                        file=file_path,
                        additions=additions,
                        deletions=deletions,
                        hunks=hunks
                    ))
                except ValueError:
                    continue
        
        return diffs
    
    def _get_hunks(self, commit_hash: str, file_path: str) -> List[str]:
        """Get the diff hunks for a specific file in a commit"""
        args = ['show', commit_hash, '--', file_path]
        output = self._run_git_command(args)
        
        hunks = []
        current_hunk = []
        
        for line in output.split('\n'):
            if line.startswith('@@'):
                if current_hunk:
                    hunks.append('\n'.join(current_hunk))
                current_hunk = [line]
            elif current_hunk:
                current_hunk.append(line)
        
        if current_hunk:
            hunks.append('\n'.join(current_hunk))
        
        return hunks
    
    def find_repeated_changes(self, min_occurrences: int = 2) -> List[Dict]:
        """
        Find files that have been changed multiple times for similar reasons
        
        Args:
            min_occurrences: Minimum number of similar changes
            
        Returns:
            List of patterns with their occurrences
        """
        # Get all commits
        commits = self.get_commits(max_count=1000)
        
        # Group by files and look for patterns
        file_changes = {}
        
        for commit in commits:
            # Get files changed in this commit
            args = ['show', '--name-only', '--format=', commit['hash']]
            output = self._run_git_command(args)
            
            for file_path in output.strip().split('\n'):
                if not file_path:
                    continue
                
                if file_path not in file_changes:
                    file_changes[file_path] = []
                
                file_changes[file_path].append(commit['message'])
        
        # Find repeated patterns
        repeated = []
        for file_path, messages in file_changes.items():
            if len(messages) >= min_occurrences:
                # Look for similar messages
                patterns = self._find_message_patterns(messages)
                for pattern, count in patterns.items():
                    if count >= min_occurrences:
                        repeated.append({
                            'file': file_path,
                            'pattern': pattern,
                            'occurrences': count,
                            'messages': [m for m in messages if pattern.lower() in m.lower()]
                        })
        
        return repeated
    
    def _find_message_patterns(self, messages: List[str]) -> Dict[str, int]:
        """Find common patterns in commit messages"""
        patterns = {}
        
        # Common keywords to look for
        keywords = ['fix', 'bug', 'update', 'refactor', 'optimize', 
                   'null', 'error', 'crash', 'performance']
        
        for keyword in keywords:
            count = sum(1 for m in messages if keyword in m.lower())
            if count > 0:
                patterns[keyword] = count
        
        return patterns